//-------------------------------------------------------------
//  Edge Detector Module
//  Author : Sheshu Ramanandan : krsheshu@gmail.com
//-------------------------------------------------------------

module edge_detector

        (
            input   wire                clk_i                   ,
            input   wire                rst_an_i                ,

            input   wire                rst_capture_i           ,
            input   wire                start_i                 ,
            input   wire                capture_i               ,

            output  wire                start_i_rising_o        ,
            output  wire                capture_i_rising_o      ,
            output  wire                rst_capture_i_rising_o

        );

//-------------------------------------------------------------
//  Internal signals
//-------------------------------------------------------------

reg                   start_i_r            ;
reg                   capture_i_r          ;
reg                   rst_capture_i_r      ;

//-------------------------------------------------------------
//  Edge Detectors
//-------------------------------------------------------------


assign start_i_rising_o        = ( ( start_i_r        == 1'b0 ) && ( start_i       == 1'b1 ) ) ? 1'b1 : 1'b0  ;
assign capture_i_rising_o      = ( ( capture_i_r      == 1'b0 ) && ( capture_i     == 1'b1 ) ) ? 1'b1 : 1'b0  ;
assign rst_capture_i_rising_o  = ( ( rst_capture_i_r  == 1'b0 ) && ( rst_capture_i == 1'b1 ) ) ? 1'b1 : 1'b0  ;


//-------------------------------------------------------------
//  Registers
//-------------------------------------------------------------

always @( posedge clk_i, negedge rst_an_i ) begin
  if ( rst_an_i == 1'b0 ) begin
      start_i_r        <=    1'b0             ;
      capture_i_r      <=    1'b0             ;
      rst_capture_i_r  <=    1'b0             ;
  end else
      start_i_r        <=    start_i          ;
      capture_i_r      <=    capture_i        ;
      rst_capture_i_r  <=    rst_capture_i    ;
end

//-------------------------------------------------------------

endmodule
