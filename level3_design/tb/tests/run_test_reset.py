import cocotb
from tb.bfm.timer_bfm import clock_gen, reset_module
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer


RESET_TIME_NS = 197

# Reset Test
@cocotb.test()
async def run_test_reset(dut):

    # clock
    cocotb.fork(clock_gen(dut.clk_in))

    await reset_module(dut.rst_an_in, RESET_TIME_NS)

    try:
        assert dut.captured_out.value == 0
        cocotb.log.info( 'Resetting captured_out Successful! ' )
    except AssertionError:
        cocotb.log.error( 'Resetting captured_out failed! ' )

