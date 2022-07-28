//-------------------------------------------------------------
//  Edge Detector Module
//-------------------------------------------------------------

module edge_detector  #(  parameter NB_CAPTURES       =   10  )

        (
            input   wire                                  clk_i                   ,
            input   wire                                  rst_an_i                ,

            input   wire       [ NB_CAPTURES-1 : 0]       rst_capture_i           ,
            input   wire       [ NB_CAPTURES-1 : 0]       start_i                 ,
            input   wire       [ NB_CAPTURES-1 : 0]       capture_i               ,

            output  wire       [ NB_CAPTURES-1 : 0]       start_i_rising_o        ,
            output  wire       [ NB_CAPTURES-1 : 0]       capture_i_rising_o      ,
            output  wire       [ NB_CAPTURES-1 : 0]       rst_capture_i_rising_o

        );

//-------------------------------------------------------------
//  Internal signals
//-------------------------------------------------------------

reg                   start_i_r            [ NB_CAPTURES-1 : 0] ;
reg                   capture_i_r          [ NB_CAPTURES-1 : 0] ;
reg                   rst_capture_i_r      [ NB_CAPTURES-1 : 0] ;

genvar i;

//-------------------------------------------------------------
//  Outputs
//-------------------------------------------------------------

generate

for ( i=0; i<NB_CAPTURES; i=i+1 ) begin
    assign start_i_rising_o         [i] = ( ( start_i_r       [i] == 1'b0 ) && ( start_i      [i] == 1'b1 ) ) ? 1'b1 : 1'b0  ;
    assign capture_i_rising_o       [i] = ( ( capture_i_r     [i] == 1'b0 ) && ( capture_i    [i] == 1'b1 ) ) ? 1'b1 : 1'b0  ;
    assign rst_capture_i_rising_o   [i] = ( ( rst_capture_i_r [i] == 1'b0 ) && ( rst_capture_i[i] == 1'b1 ) ) ? 1'b1 : 1'b0  ;
end

endgenerate

//-------------------------------------------------------------
//  Registers
//-------------------------------------------------------------

generate

for ( i=0; i<NB_CAPTURES; i=i+1 ) begin

    always @( posedge clk_i, negedge rst_an_i ) begin
      if ( rst_an_i == 1'b0 ) begin
          start_i_r       [i] <=    1'b0             ;
          capture_i_r     [i] <=    1'b0             ;
          rst_capture_i_r [i] <=    1'b0             ;
      end else
          start_i_r      [i]  <=    start_i        [i]  ;
          capture_i_r    [i]  <=    capture_i      [i]  ;
          rst_capture_i_r[i]  <=    rst_capture_i  [i]  ;
    end

end

endgenerate
//-------------------------------------------------------------

endmodule
