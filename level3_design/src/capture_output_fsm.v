//-------------------------------------------------------------
//  Capture FSM Module
//-------------------------------------------------------------

module capture_output_fsm  #(
                  parameter TIMER_BITWIDTH    =   32  ,
                            NB_CAPTURES       =   10  )


        (
            input   wire                                          clk_i                     ,
            input   wire                                          rst_an_i                  ,

            input   wire                 [ NB_CAPTURES-1 : 0 ]    start_in_rising_i         ,
            input   wire                 [ NB_CAPTURES-1 : 0 ]    capture_in_rising_i       ,
            input   wire                 [ NB_CAPTURES-1 : 0 ]    rst_capture_in_rising_i   ,

            output  wire  [ TIMER_BITWIDTH*NB_CAPTURES -1: 0 ]    captured_o                ,
            output  wire  [ TIMER_BITWIDTH*NB_CAPTURES -1: 0 ]    counter_o

        );

//-------------------------------------------------------------
//  Internal signals
//-------------------------------------------------------------

reg     [ 1:0  ]                    capture_fsm_state           [ NB_CAPTURES-1 :0]       ;
reg     [ TIMER_BITWIDTH-1:0 ]      counter                     [ NB_CAPTURES-1 :0]       ;
reg     [ TIMER_BITWIDTH-1:0 ]      captured_o_reg              [ NB_CAPTURES-1 :0]       ;

localparam                  st_idle            = 2'd0         ;
localparam                  st_counting        = 2'd1         ;
localparam                  st_captured        = 2'd2         ;

genvar i ;

//-------------------------------------------------------------
//----------------------- Outputs  ----------------------------
//-------------------------------------------------------------

generate

    for ( i=0; i<NB_CAPTURES; i=i+1 )  begin
            assign captured_o [ (i*TIMER_BITWIDTH) +: TIMER_BITWIDTH ]    =  captured_o_reg [ i ];
            assign counter_o  [ (i*TIMER_BITWIDTH) +: TIMER_BITWIDTH ]    =  counter        [ i ];


    end

endgenerate

generate

    for ( i=0; i<NB_CAPTURES; i=i+1 ) begin

        always @(posedge clk_i, negedge rst_an_i ) begin

          if ( rst_an_i == 1'b0 )
              captured_o_reg  [i] <=    32'b0;
          else if ( rst_capture_in_rising_i [i] == 1'b1 )
              captured_o_reg  [i] <=    32'b0;
          else if ( ( capture_fsm_state [i] == st_counting ) && ( capture_in_rising_i [i]== 1'b1 ) )
              captured_o_reg  [i] <=    counter [i] ;
        end
    end
endgenerate

//-------------------------------------------------------------
//-------------------- Internal Counter------------------------
//-------------------------------------------------------------

generate

    for ( i=0; i<NB_CAPTURES; i=i+1 ) begin

        always @(posedge clk_i, negedge rst_an_i ) begin

          if ( rst_an_i == 1'b0 )
              counter  [i] <=    32'b0;
          else if ( start_in_rising_i [i] == 1'b1 )
              counter  [i] <=    32'b0;
          else
              counter  [i] <=    counter [i] + 1'b1 ;
        end
    end

endgenerate

//-------------------------------------------------------------
//-------------------- State Machine --------------------------
//-------------------------------------------------------------

// States:  st_idle, st_counting, st_captured
// Inputs:  start_in_rising, capture_in_rising, rst_capture_in_rising
// Outputs:

generate

    for ( i=0; i<NB_CAPTURES; i=i+1 ) begin

        always @(posedge clk_i, negedge rst_an_i  ) begin

            if ( rst_an_i    == 1'b0 )
                capture_fsm_state [i]     <= st_idle  ;

            else begin
                case ( capture_fsm_state [i] )

                    st_idle               :     begin
                                                  if (  start_in_rising_i [i] == 1'b1 )
                                                      capture_fsm_state [i] <= st_counting;
                                                end

                    st_counting           :     begin
                                                  if (  capture_in_rising_i [i] == 1'b1 )
                                                      capture_fsm_state [i] <= st_idle;
                                                end

                    default               :     capture_fsm_state [i] <= st_idle ;

                endcase

            end

        end

    end

endgenerate
//-------------------------------------------------------------


endmodule
