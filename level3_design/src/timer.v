//-------------------------------------------------------------
//  Author : Sheshu Ramanandan : krsheshu@gmail.com
//-------------------------------------------------------------


module timer

        (
            input   wire                clk_in          ,
            input   wire                rst_an_in       ,

            input   wire                rst_capture_in  ,
            input   wire                start_in        ,
            input   wire                capture_in      ,

            output  wire  [ 31: 0 ]     captured_out

        );

//-------------------------------------------------------------
//  Internal signals
//-------------------------------------------------------------

wire                  rst_as_n              ;

wire                  start_i_rising        ;
wire                  capture_i_rising      ;
wire                  rst_capture_i_rising  ;

//-------------------------------------------------------------
//  Modules
//-------------------------------------------------------------

//  Async assert Sync Deasset Reset synchronizer

reset_synchronizer  rst_sync_inst

        (
              .clk_i              ( clk_in        ),
              .rst_an_i           ( rst_an_in     ),

              .rst_as_n_o         ( rst_as_n      )

        );


//-------------------------------------------------------------

//  Edge Detector

edge_detector   edge_detector_inst

        (
              .clk_i                        (  clk_in                   ),
              .rst_an_i                     (  rst_as_n                 ),

              .rst_capture_i                (  rst_capture_in           ),
              .start_i                      (  start_in                 ),
              .capture_i                    (  capture_in               ),

              .start_i_rising_o             (  start_i_rising           ),
              .capture_i_rising_o           (  capture_i_rising         ),
              .rst_capture_i_rising_o       (  rst_capture_i_rising     )

        );

//-------------------------------------------------------------

//  Capture Outputs FSM

capture_output_fsm   capture_output_fsm_inst

        (
              .clk_i                        ( clk_in                  ),
              .rst_an_i                     ( rst_as_n                ),

              .start_in_rising_i            ( start_i_rising          ),
              .capture_in_rising_i          ( capture_i_rising        ),
              .rst_capture_in_rising_i      ( rst_capture_i_rising    ),

              .captured_o                   ( captured_out            ),
              .counter_o                    ( counter_out             )

        );

//-------------------------------------------------------------

endmodule











