//-------------------------------------------------------------
//  Tech Task 1
//  Alarm Generator Module
//-------------------------------------------------------------

module alarm_generator

        (
            input   wire                clk_i                   ,
            input   wire                rst_an_i                ,

            input   wire                alarm_en_i              ,
            input   wire  [ 31: 0 ]     alarm_i                 ,
            input   wire  [ 31: 0 ]     counter_i               ,

            output  reg                 alarm_o

        );

//-------------------------------------------------------------
//  Outputs
//-------------------------------------------------------------

always @( posedge clk_i, negedge rst_an_i ) begin
  if ( rst_an_i == 1'b0 )
      alarm_o         <=  1'b0            ;
  else if ( alarm_en_i == 1'b1 )
      alarm_o         <=    ( counter_i == alarm_i ) ? 1'b1 : 1'b0   ;
  else
      alarm_o         <=  1'b0            ;
end

//-------------------------------------------------------------

endmodule
