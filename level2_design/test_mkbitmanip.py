# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock
import random

from bitmanip_instructions import Bitmanip_Instructions
from model_mkbitmanip import *

from itertools import permutations

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1)
        signal.value <= 1
        yield Timer(1)


# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10)
    dut.RST_N.value <= 1

    testpass                =   True
    nb_failures             =   0
    failed_instructions     =   []

    # Get all instructions for the Bitmanip coprocessor
    bitmanip_instructions           = Bitmanip_Instructions ()

    logical_instructions            = bitmanip_instructions.get_instructions_logical()
    shift_instructions              = bitmanip_instructions.get_instructions_shift()
    singlebit_instructions          = bitmanip_instructions.get_instructions_singlebit()
    shift_imm_instructions          = bitmanip_instructions.get_instructions_shift_imm()
    singlebit_imm_instructions      = bitmanip_instructions.get_instructions_singlebit_imm()
    ternary_instructions            = bitmanip_instructions.get_instructions_ternary()
    ternary_imm_instructions        = bitmanip_instructions.get_instructions_ternary_imm()
    all_instructions                = bitmanip_instructions.get_instructions_all()

    stimulus_set                    = [ -1*pow(2,31), pow(2,31)-1, -1*pow(2,31)>>1, (pow(2,31)-1)>>1, -1*pow(2,31)>>2, (pow(2,31)-1)>>2, 1, 0, -1 ]
    stimulus_permutations           = list(permutations(stimulus_set,3))

    tries            = 0
    for i in range(len(all_instructions)):
        print("\033[93m",end='\n')
        cocotb.log.info('-------------------------------------------------------')
        cocotb.log.info('Instruction {:02}: {:s}'.format(i,(hex(all_instructions[i])[2:]).zfill(8)))
        print("\033[00m",end='')

        instruction_nb_errors = 0
        ######### CTB : Modify the test to expose the bug #############
        for ii in range(len(stimulus_permutations)):

            tries += 1
            # input transaction
            mav_putvalue_src1   = stimulus_permutations [ii][0]
            mav_putvalue_src2   = stimulus_permutations [ii][1]
            mav_putvalue_src3   = stimulus_permutations [ii][2]
            mav_putvalue_instr  = all_instructions[i]

            # expected output from the model
            expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

            # driving the input transaction
            dut.mav_putvalue_src1.value = mav_putvalue_src1
            dut.mav_putvalue_src2.value = mav_putvalue_src2
            dut.mav_putvalue_src3.value = mav_putvalue_src3
            dut.EN_mav_putvalue.value = 1
            dut.mav_putvalue_instr.value = mav_putvalue_instr

            yield Timer(1)

            # obtaining the output
            dut_output = dut.mav_putvalue.value

            cocotb.log.info('src1: {}, src2: {}, src3: {}, instr: {}, DUT OUTPUT:{},  EXPECTED OUTPUT: {}'  \
                            .format( mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3, hex(mav_putvalue_instr), hex(dut_output), hex(expected_mav_putvalue) ) )

            # comparison
            error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
            try:
                assert dut_output == expected_mav_putvalue
            except AssertionError:
                testpass                =   False
                nb_failures             +=  1
                instruction_nb_errors   +=  1
                cocotb.log.error(error_message)

        if ( instruction_nb_errors > 0):
            failed_instructions.append(mav_putvalue_instr)

        try:
            assert instruction_nb_errors == 0
        except AssertionError:
            cocotb.log.error('Nb errors in {} tries: {}'.format(tries,instruction_nb_errors))

        print("\033[93m",end='')
        cocotb.log.info('-------------------------------------------------------')
        print("\033[00m",end='')

    print("\033[93m",end='')
    cocotb.log.info('Total nb instructions failures: {}'.format(nb_failures))
    print("\033[00m",end='')
    if ( nb_failures > 0 ):
        for i in range( len(failed_instructions) ):
            cocotb.log.error('{:02}: Failed on Instruction: 0x{}'.format(i,hex(failed_instructions[i])[2:].zfill(8)))
    assert testpass == True, cocotb.log.error('Test Failed')
