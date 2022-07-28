//-------------------------------------------------------------
//  Alarm Generator Module
//-------------------------------------------------------------

module alarm_generator  #(
                  parameter TIMER_BITWIDTH    =   32  ,
                            NB_CAPTURES       =   10  )

        (
            input   wire                                          clk_i        ,
            input   wire                                          rst_an_i     ,

            input   wire                 [ NB_CAPTURES -1 : 0 ]   alarm_en_i   ,
            input   wire  [ TIMER_BITWIDTH*NB_CAPTURES -1 : 0 ]   alarm_i      ,
            input   wire  [ TIMER_BITWIDTH*NB_CAPTURES -1 : 0 ]   counter_i    ,

            output  wire                  [ NB_CAPTURES-1 : 0 ]   alarm_o

        );

//-------------------------------------------------------------
//  Internal signals
//-------------------------------------------------------------

wire  [ TIMER_BITWIDTH-1: 0 ]     alarm         [ NB_CAPTURES-1 :0]           ;
wire  [ TIMER_BITWIDTH-1: 0 ]     counter       [ NB_CAPTURES-1 :0]           ;

genvar i;

generate


  for ( i=0; i<NB_CAPTURES; i=i+1 )  begin
          assign counter [i]  =  counter_i  [ (i*TIMER_BITWIDTH) +: TIMER_BITWIDTH ];
          assign alarm [i]    =  alarm_i    [ (i*TIMER_BITWIDTH) +: TIMER_BITWIDTH ];

  end

endgenerate


//-------------------------------------------------------------
//  Outputs
//-------------------------------------------------------------

generate

  for ( i=0; i<NB_CAPTURES; i=i+1 )  begin
      always @( posedge clk_i, negedge rst_an_i ) begin
        if ( rst_an_i == 1'b0 )
            alarm_o   [i]      <=  1'b0            ;
        else if ( alarm_en_i [i] == 1'b1 )
            alarm_o   [i]      <=    ( counter [i] == alarm [i] ) ? 1'b1 : 1'b0   ;
        else
            alarm_o   [i]      <=  1'b0            ;
      end
  end

endgenerate

//-------------------------------------------------------------

endmodule
