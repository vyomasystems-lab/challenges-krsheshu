import cocotb
from timer_bfm import clock_gen, reset_module

# rst_capture Test
@cocotb.test()
async def run_test_rst_capture(dut):

    # clock
    cocotb.fork( clock_gen( dut.clk_in ) )
    # reset
    await reset_module( dut.rst_an_in, 40 )

