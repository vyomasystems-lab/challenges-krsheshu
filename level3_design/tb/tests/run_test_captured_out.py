import cocotb
from tb.bfm import timer_bfm
from cocotb.triggers import Timer, RisingEdge
import copy
import random

# rst_capture Test
@cocotb.test()
async def run_test_captuered_out(dut):

    # clock
    cocotb.fork( timer_bfm.clock_gen( dut.clk_in ) )
    # reset
    await timer_bfm.reset_module( dut.rst_an_in, 20*timer_bfm.CLK_PERIOD)

    await timer_bfm.disable_rst_capture_in( timer_bfm.CLK_PERIOD, dut.clk_in, dut.rst_capture_in  )

    random.seed( a = 0 )
    nb_failures     = 0
    nb_tests        = 100
    for _ in range(nb_tests):
        traveltime_in_clks = random.randint(0,1000)
        cocotb.log.info(f'Selected randomized traveltime (clks): {traveltime_in_clks}')

        await timer_bfm.disable_start_in      ( timer_bfm.CLK_PERIOD, dut.clk_in, dut.start_in        )
        await timer_bfm.disable_capture_in    ( timer_bfm.CLK_PERIOD, dut.clk_in, dut.capture_in      )


        await timer_bfm.enable_start_in      ( 10*timer_bfm.CLK_PERIOD, dut.clk_in, dut.start_in )

        await timer_bfm.enable_capture_in    ( traveltime_in_clks*timer_bfm.CLK_PERIOD, dut.clk_in, dut.capture_in)

        await RisingEdge(dut.clk_in)
        await RisingEdge(dut.clk_in)

        cocotb.log.info('Captured counter value : {},  Expected value: {}'
                    .format(int(dut.captured_out.value), int(traveltime_in_clks-1) ) )

        await Timer( 1, units='ns' )
        try:
            assert dut.captured_out.value == (traveltime_in_clks-1)
        except AssertionError:
            cocotb.log.error( f'captured_out {dut.captured_out.value} != random_travel_time{traveltime_in_clks}. Test Failed! ' )
            nb_failures += 1

    try:
        assert nb_failures == 0
        cocotb.log.info(f'All tests in this suite successful! Nb randomized tests: {nb_tests}')
    except AssertionError:
        cocotb.log.info(f'Tests in this suite failes!')
