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

    ref_sequence                = 0b1011
    inp_sequence                = 0b11001101101101100110110101011111
    detected_seq                = 0b0000
    ref_sequence_seen           = 0
    at_least_one_ref_seq_seen   = 0
    nb_ref_sequence_found       = 0
    nb_sequence_detected        = 0

    testpass            = True

    for i in range(inp_sequence.bit_length()):

        await RisingEdge(dut.clk)
        dut.inp_bit.value = ( inp_sequence >> (inp_sequence.bit_length()-1-i) ) & 0b1

        await Timer(1,units='ns')

        if ( ref_sequence_seen == 1 ):

            at_least_one_ref_seq_seen   =   1
            nb_ref_sequence_found       +=  1

            try:
                assert dut.seq_seen.value == ref_sequence_seen
                print("\033[92m",end='')
                dut._log.info('Reference Sequence detected! Signal ref_sequence_seen : {}, Output signal dut_seq_seen : {}'  \
                                                        .format(ref_sequence_seen, dut.seq_seen.value) )
                print("\033[00m",end='')
                nb_sequence_detected    +=  1

            except AssertionError:
                dut._log.error('Sequence Seen Test Failed!, dut.seq_seen : {}, ref_sequence_seen : {}'  \
                                                            .format(dut.seq_seen.value, ref_sequence_seen) )
                testpass = False

            ref_sequence_seen = 0

        detected_seq =  ( (detected_seq << 1) |  dut.inp_bit.value ) & 0b01111
        ref_sequence_seen = 1 if  ( detected_seq == ref_sequence ) else ref_sequence_seen

        dut._log.info(  'Input bit: {}, Detected_sequence: {}, Ref_sequence_seen: {}, dut.seq_seen: {}, '   \
                        .format( dut.inp_bit.value, bin(detected_seq)[2:].zfill(4), ref_sequence_seen, dut.seq_seen.value ) )


    if at_least_one_ref_seq_seen == 0:
        testpass = False

    assert at_least_one_ref_seq_seen == 1, dut._log.error('Error No reference sequence found in the input data!')


    try:
        assert nb_ref_sequence_found == nb_sequence_detected
        print("\033[93m",end='')
        dut._log.info('Input overlapping sequence {}'.format(bin(inp_sequence)))
        print("\033[92m",end='')
        dut._log.info( 'nb_ref_sequence_found: {}, nb_sequence_detected: {}'.format(nb_ref_sequence_found, nb_sequence_detected) )
        print("\033[00m",end='')
    except AssertionError:
        print("\033[93m",end='')
        dut._log.info('Input overlapping sequence {}'.format(bin(inp_sequence)))
        print("\033[00m",end='')
        dut._log.error( 'Nb ref sequence found doesnot match with nb_sequence_detected! '  \
                        'nb_ref_sequence_found: {}, nb_sequence_detected: {}'.format(nb_ref_sequence_found, nb_sequence_detected) )

    assert testpass == True, dut._log.error('Test failed')
