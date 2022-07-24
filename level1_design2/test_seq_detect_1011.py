# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')

    ref_sequence        = 0b1011
    inp_sequence        = 0b11011
    detected_seq        = 0b0000
    ref_sequence_seen   = 0

    for i in range(inp_sequence.bit_length()):
        await RisingEdge(dut.clk)
        dut.inp_bit.value = ( inp_sequence >> (inp_sequence.bit_length()-1-i) ) & 0b1
        await Timer(1,units='ns')
        detected_seq =  ( (detected_seq << 1) |  dut.inp_bit.value ) & 0b01111
        ref_sequence_seen = 1 if  ( detected_seq == ref_sequence ) else ref_sequence_seen
        dut._log.info(  'Input bit: {}, Detected_sequence: {:6}, Ref_sequence_seen: {}, dut.seq_seen: {}, '   \
                        .format( dut.inp_bit.value, bin(detected_seq), ref_sequence_seen, dut.seq_seen.value ) )

        if ( ref_sequence_seen == 1 ):
            await RisingEdge(dut.clk)
            await Timer(2,units='ns')
            dut._log.info('dut.seq_seen : {},  ref_sequence_seen : {}'.format(dut.seq_seen.value, ref_sequence_seen) )
            assert dut.seq_seen.value == ref_sequence_seen, 'Sequence Test Failed!, dut.seq_seen : {}, ref_sequence_seen : {}'  \
                                                            .format(dut.seq_seen.value, ref_sequence_seen)

    assert ref_sequence_seen == 1, 'Error No reference sequence found in the input data!'
