//-------------------------------------------------------------
//  2FF CDC Synchronizer
//-------------------------------------------------------------

module cdc_single_bit_synchronizer #( parameter     NB_PARALLEL_SINGLE_BIT_CDCS   = 10 ,
                                                    NB_REGISTERS                  =  2 )

        (
            input   wire                                                    clk_i                     ,
            input   wire    [ NB_PARALLEL_SINGLE_BIT_CDCS-1 : 0 ]           bit_i                     ,

            output  wire    [ NB_PARALLEL_SINGLE_BIT_CDCS-1 : 0 ]           bit_o


        );

//-------------------------------------------------------------
//  Internal signals
//-------------------------------------------------------------

reg    [ NB_REGISTERS-1: 0 ]  ff_sync [ NB_PARALLEL_SINGLE_BIT_CDCS-1 : 0 ];


//-------------------------------------------------------------
//  Outputs
//-------------------------------------------------------------

genvar i;

generate

    for ( i=0; i<NB_PARALLEL_SINGLE_BIT_CDCS; i=i+1 ) begin

        assign bit_o [i]        =   ff_sync [i] [NB_REGISTERS-1] ;

    end

endgenerate

//-------------------------------------------------------------
//  2FF Synchronizer
//-------------------------------------------------------------

generate

    for ( i=0; i<NB_PARALLEL_SINGLE_BIT_CDCS; i=i+1 ) begin

        always @( posedge clk_i )

                  ff_sync[i]  <= { ff_sync [i][0] , bit_i[i] } ;

    end

endgenerate

endmodule
