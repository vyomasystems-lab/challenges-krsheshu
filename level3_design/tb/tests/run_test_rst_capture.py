import cocotb
from tb.bfm import timer_bfm
from cocotb.triggers import Timer, RisingEdge
import copy

# rst_capture Test
@cocotb.test()
async def run_test_rst_capture(dut):

    # clock
    cocotb.fork( timer_bfm.clock_gen( dut.clk_in ) )
    # reset
    await timer_bfm.reset_module( dut.rst_an_in, 20*timer_bfm.CLK_PERIOD)

    await timer_bfm.disable_start_in      ( timer_bfm.CLK_PERIOD, dut.clk_in, dut.start_in        )
    await timer_bfm.disable_capture_in    ( timer_bfm.CLK_PERIOD, dut.clk_in, dut.capture_in      )
    await timer_bfm.disable_rst_capture_in( timer_bfm.CLK_PERIOD, dut.clk_in, dut.rst_capture_in  )


    await timer_bfm.enable_start_in      ( 10*timer_bfm.CLK_PERIOD, dut.clk_in, dut.start_in )

    await timer_bfm.enable_capture_in    ( 100*timer_bfm.CLK_PERIOD, dut.clk_in, dut.capture_in)

    await RisingEdge(dut.clk_in)
    await RisingEdge(dut.clk_in)
    sampled_capture_value = copy.copy(dut.captured_out.value)

    await timer_bfm.enable_rst_capture_in  ( timer_bfm.CLK_PERIOD, dut.clk_in, dut.rst_capture_in)
    await RisingEdge(dut.clk_in)
    await RisingEdge(dut.clk_in)
    cocotb.log.info('Before reset, captured_out: 0b{},  After reset, captured_out: 0b{}'
                .format(sampled_capture_value, dut.captured_out.value) )


    await Timer( 1, units='ns' )
    try:
        assert dut.captured_out.value == 0
    except AssertionError:
        cocotb.log.error( 'captured_out not reset. Test Failed! ' )

