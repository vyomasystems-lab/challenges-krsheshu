import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer

CLK_PERIOD      = 20
TIMER_BITWIDTH  = 32
NB_CAPTURES     = 10

# Clock Generation
@cocotb.coroutine
def clock_gen( signal ):
    while True:
        signal.value = 0
        yield Timer( CLK_PERIOD/2, units='ns' )
        signal.value = 1
        yield Timer( CLK_PERIOD/2, units='ns' )


@cocotb.coroutine
def reset_module(rst_n, time_ns):
    rst_n.value = 0
    cocotb.log.info('Asynchronously Resetting system...')
    yield Timer( time_ns, units='ns' )
    cocotb.log.info('Releasing reset...')
    rst_n.value = 1
    yield Timer( CLK_PERIOD, units='ns' )


@cocotb.coroutine
def enable_start_in( time_ns, clk, signal ):
    yield Timer( time_ns, units='ns' )
    yield RisingEdge(clk)
    # Driving start_in
    signal.value = 1


@cocotb.coroutine
def disable_start_in( time_ns, clk, signal ):
    yield Timer( time_ns, units='ns' )
    yield RisingEdge(clk)
    # Driving start_in
    cocotb.log.info("Disabling start_in")
    signal.value = 0

@cocotb.coroutine
def enable_capture_in( time_ns, clk, signal ):
    yield Timer( time_ns, units='ns' )
    yield RisingEdge(clk)
    # Driving start_in
    cocotb.log.info("Enabling capture_in")
    signal.value = 1

@cocotb.coroutine
def disable_capture_in( time_ns, clk, signal ):
    yield Timer( time_ns, units='ns' )
    yield RisingEdge(clk)
    # Driving start_in
    cocotb.log.info("Disabling capture_in")
    signal.value = 0

@cocotb.coroutine
def enable_rst_capture_in( time_ns, clk, signal ):
    yield Timer( time_ns, units='ns' )
    yield RisingEdge(clk)
    # Driving start_in
    cocotb.log.info("Enabling rst_capture_in")
    signal.value = 1


@cocotb.coroutine
def disable_rst_capture_in( time_ns, clk, signal ):
    yield Timer( time_ns, units='ns' )
    yield RisingEdge(clk)
    # Driving start_in
    cocotb.log.info("Disabling rst_capture_in")
    signal.value = 0
