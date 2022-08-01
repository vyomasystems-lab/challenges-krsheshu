//-------------------------------------------------------------
//  Tech Task 1
//  Reset Synchronizer Module
//  Async assert Sync Deasset Reset synchronizer
//-------------------------------------------------------------

module reset_synchronizer

        (
            input   wire                clk_i                     ,
            input   wire                rst_an_i                  ,

            output  wire                rst_as_n_o


        );

//-------------------------------------------------------------
//  Internal signals
//-------------------------------------------------------------

reg    [ 1:0 ]  ff_sync ;


//-------------------------------------------------------------
//  Outputs
//-------------------------------------------------------------

assign rst_as_n_o       =   ff_sync [1] ;



//-------------------------------------------------------------
//  Active Low Reset Synchronizer
//-------------------------------------------------------------

always @(posedge clk_i , negedge rst_an_i ) begin

    if ( rst_an_i == 1'b0 )
          ff_sync  <= 2'b0 ;
    else
          ff_sync  <= { ff_sync [0] , 1'b1 } ;

end


endmodule
