import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer

CLK_PERIOD  = 10
NB_CAPTURES = 10

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer( CLK_PERIOD, units='ns' )
        signal.value <= 1
        yield Timer( CLK_PERIOD, units='ns' )


async def reset_module(rst_n, time_ns):
    rst_n.value = 0
    cocotb.log.info('Asynchronously Resetting system...')
    await Timer( time_ns, units='ns' )
    cocotb.log.info('Releasing reset...')
    rst_n.value = 1
    await Timer( CLK_PERIOD, units='ns' )

