import cocotb
from timer_bfm import clock_gen, reset_module

# Reset Test
@cocotb.test()
async def run_test_reset(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk_in))

    await reset_module(dut.rst_an_in, 197)

    try:
        assert dut.captured_out.value == 0
        cocotb.log.info( 'Resetting captured_out Successful! ' )
    except AssertionError:
        cocotb.log.error( 'Resetting captured_out failed! ' )
    try:
        assert dut.counter_out.value  == 0
        cocotb.log.info( 'Resetting counter_out Successful! ' )
    except AssertionError:
        cocotb.log.error( 'Resetting counter_out failed! ' )
    try:
        assert dut.alarm_out.value    == 0
        cocotb.log.info ( 'Resetting alarm_out Successful! ' )
    except AssertionError:
        cocotb.log.error( 'Reset alarm_out failed! ' )

