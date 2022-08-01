//-------------------------------------------------------------
//  Capture FSM Module
//  Author : Sheshu Ramanandan : krsheshu@gmail.com
//-------------------------------------------------------------

module capture_output_fsm

        (
            input   wire                clk_i                     ,
            input   wire                rst_an_i                  ,

            input   wire                start_in_rising_i         ,
            input   wire                capture_in_rising_i       ,
            input   wire                rst_capture_in_rising_i   ,

            output  wire  [ 31: 0 ]     captured_o                ,
            output  wire  [ 31: 0 ]     counter_o

        );

//-------------------------------------------------------------
//  Internal signals
//-------------------------------------------------------------

reg     [ 1:0  ]            capture_fsm_state                 ;
reg     [ 31:0 ]            counter                           ;
reg     [ 31:0 ]            captured_o_reg                    ;

localparam                  st_idle            = 2'd0         ;
localparam                  st_counting        = 2'd1         ;
localparam                  st_captured        = 2'd2         ;

//-------------------------------------------------------------
//----------------------- Outputs  ----------------------------
//-------------------------------------------------------------

assign counter_o        =   counter             ;
assign captured_o       =   captured_o_reg      ;

always @(posedge clk_i, negedge rst_an_i ) begin

  if ( rst_an_i == 1'b0 )
      captured_o_reg <=    32'b0;
  else if ( rst_capture_in_rising_i == 1'b1 )
      captured_o_reg  <=    32'b0;
  else if ( ( capture_fsm_state == st_counting ) && ( capture_in_rising_i == 1'b1 ) )
      captured_o_reg  <=    counter ;
end

//-------------------------------------------------------------
//-------------------- Internal Counter------------------------
//-------------------------------------------------------------

always @(posedge clk_i, negedge rst_an_i ) begin

  if ( rst_an_i == 1'b0 )
      counter   <=    32'b0;
  else if ( start_in_rising_i == 1'b1 )
      counter   <=    32'b0;
  else
      counter   <=    counter + 1'b1 ;
end

//-------------------------------------------------------------
//-------------------- State Machine --------------------------
//-------------------------------------------------------------

// States:  st_idle, st_counting, st_captured
// Inputs:  start_in_rising, capture_in_rising, rst_capture_in_rising
// Outputs:

always @(posedge clk_i, negedge rst_an_i  ) begin

  if ( rst_an_i    == 1'b0 )
      capture_fsm_state     <= st_idle  ;

  else if ( rst_capture_in_rising_i == 1'b1 )
      capture_fsm_state     <= st_idle  ;

  else begin
      case ( capture_fsm_state )

          st_idle               :     begin
                                        if (  start_in_rising_i == 1'b1 )
                                            capture_fsm_state <= st_counting;
                                      end

          st_counting           :     begin
                                        if (  capture_in_rising_i == 1'b0 )
                                            capture_fsm_state <= st_idle;
                                      end

          default               :     capture_fsm_state <= st_idle ;

      endcase
  end
end

//-------------------------------------------------------------


endmodule
