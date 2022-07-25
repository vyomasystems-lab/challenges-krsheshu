# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')

    testpass = True

    for i in range(pow(2,5)-1):
        dut.sel.value     = i
        dut.inp0.value    = 1
        dut.inp1.value    = 2
        dut.inp2.value    = 3
        dut.inp3.value    = 0
        dut.inp4.value    = 1
        dut.inp5.value    = 2
        dut.inp6.value    = 3
        dut.inp7.value    = 0
        dut.inp8.value    = 1
        dut.inp9.value    = 2
        dut.inp10.value   = 3
        dut.inp11.value   = 0
        dut.inp12.value   = 1
        dut.inp13.value   = 2
        dut.inp14.value   = 3
        dut.inp15.value   = 0
        dut.inp16.value   = 1
        dut.inp17.value   = 2
        dut.inp18.value   = 3
        dut.inp19.value   = 0
        dut.inp20.value   = 1
        dut.inp21.value   = 2
        dut.inp22.value   = 3
        dut.inp23.value   = 0
        dut.inp24.value   = 1
        dut.inp25.value   = 2
        dut.inp26.value   = 3
        dut.inp27.value   = 0
        dut.inp28.value   = 1
        dut.inp29.value   = 2
        dut.inp30.value   = 3

        await Timer(2, units='ns')
        select          =   dut.sel.value
        if   select == 0:
            output_ref_val  =   dut.inp0.value
        elif select == 1:
            output_ref_val  =   dut.inp1.value
        elif select == 2:
            output_ref_val  =   dut.inp2.value
        elif select == 3:
            output_ref_val  =   dut.inp3.value
        elif select == 4:
            output_ref_val  =   dut.inp4.value
        elif select == 5:
            output_ref_val  =   dut.inp5.value
        elif select == 6:
            output_ref_val  =   dut.inp6.value
        elif select == 7:
            output_ref_val  =   dut.inp7.value
        elif select == 8:
            output_ref_val  =   dut.inp8.value
        elif select == 9:
            output_ref_val  =   dut.inp9.value
        elif select == 10:
            output_ref_val  =   dut.inp10.value
        elif select == 11:
            output_ref_val  =   dut.inp11.value
        elif select == 12:
            output_ref_val  =   dut.inp12.value
        elif select == 13:
            output_ref_val  =   dut.inp13.value
        elif select == 14:
            output_ref_val  =   dut.inp14.value
        elif select == 15:
            output_ref_val  =   dut.inp15.value
        elif select == 16:
            output_ref_val  =   dut.inp16.value
        elif select == 17:
            output_ref_val  =   dut.inp17.value
        elif select == 18:
            output_ref_val  =   dut.inp18.value
        elif select == 19:
            output_ref_val  =   dut.inp19.value
        elif select == 20:
            output_ref_val  =   dut.inp20.value
        elif select == 21:
            output_ref_val  =   dut.inp21.value
        elif select == 22:
            output_ref_val  =   dut.inp22.value
        elif select == 23:
            output_ref_val  =   dut.inp23.value
        elif select == 24:
            output_ref_val  =   dut.inp24.value
        elif select == 25:
            output_ref_val  =   dut.inp25.value
        elif select == 26:
            output_ref_val  =   dut.inp26.value
        elif select == 27:
            output_ref_val  =   dut.inp27.value
        elif select == 28:
            output_ref_val  =   dut.inp28.value
        elif select == 29:
            output_ref_val  =   dut.inp29.value
        elif select == 30:
            output_ref_val  =   dut.inp30.value
        else:
            output_ref_val  =   None

        try:
            print("\033[93m",end='')
            dut._log.info('Test: {:02}, select = {}, input: {} , output: {}'.format(i, select,output_ref_val,dut.out.value) )
            print("\033[00m",end='')
            assert dut.out.value == output_ref_val
        except AssertionError:
            dut._log.error('Test: {:02}, select = {}, input: {} , output: {} Failed!'.format(i, select,output_ref_val,dut.out.value) )
            testpass = False

    assert testpass == True
