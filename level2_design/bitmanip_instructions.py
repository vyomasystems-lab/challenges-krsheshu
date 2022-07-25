# See LICENSE.iitm for details
# See LICENSE.vyoma for details


class Bitmanip_Instructions():

    def __init__( self ):

        # -- Logical Operations ---
        self.nb_op_logical                  = 6
        self.opcode_logical                 = [  0b0110011 ] * self.nb_op_logical

        self.logical_f3                     = [     0b111,      0b110,      0b100,      0b111,      0b110,      0b100 ]
        self.logical_f7                     = [ 0b0000000,  0b0000000,  0b0000000,  0b0100000,  0b0100000,  0b0100000 ]
        self.logical_f3_msbPos              = 14-3+1
        self.logical_f7_msbPos              = 31-7+1

        # -- Shift Operations ---
        self.nb_op_shift                    = 7
        self.opcode_shift                   = [  0b0110011 ] * self.nb_op_shift

        self.shift_f3                       = [     0b001,      0b101,      0b101,      0b001,      0b101,      0b001,      0b101 ]
        self.shift_f7                       = [ 0b0000000,  0b0000000,  0b0100000,  0b0010000,  0b0010000,  0b0110000,  0b0110000 ]
        self.shift_f3_msbPos                = 14-3+1
        self.shift_f7_msbPos                = 31-7+1


        # -- Singlebit Operations ---
        self.nb_op_singlebit                = 6
        self.opcode_singlebit               = [  0b0110011 ] * self.nb_op_singlebit

        self.singlebit_f3                   = [     0b001,      0b001,      0b001,      0b101,      0b101,      0b101 ]
        self.singlebit_f7                   = [ 0b0100100,  0b0010100,  0b0110100,  0b0100100,  0b0010100,  0b0110100 ]
        self.singlebit_f3_msbPos            = 14-3+1
        self.singlebit_f7_msbPos            = 31-7+1


        # -- Shift Immediate Operations ---
        self.nb_op_shift_imm                = 6
        self.opcode_shift_imm               = [  0b0010011 ] * self.nb_op_shift_imm

        self.shift_imm_f3                   = [     0b001,      0b101,      0b101,      0b001,      0b101,      0b101 ]
        self.shift_imm_f5                   = [   0b00000,    0b00000,    0b01000,    0b00100,    0b00100,    0b01100 ]
        self.shift_imm_f3_msbPos            = 14-3+1
        self.shift_imm_f5_msbPos            = 31-5+1

        # -- Singlebit Immediate Operations ---
        self.nb_op_singlebit_imm            = 6
        self.opcode_singlebit_imm           = [  0b0010011 ] * self.nb_op_singlebit_imm

        self.singlebit_imm_f3               = [     0b001,      0b001,      0b001,      0b101,      0b101,      0b101 ]
        self.singlebit_imm_f5               = [   0b01001,    0b00101,    0b01101,    0b01001,    0b00101,    0b01101 ]
        self.singlebit_imm_f3_msbPos        = 14-3+1
        self.singlebit_imm_f5_msbPos        = 31-5+1


        # -- Ternary bitmanip Operations ---
        self.nb_op_ternary                  = 4
        self.opcode_ternary                 = [  0b0110011 ] * self.nb_op_ternary

        self.ternary_f3                     = [     0b001,      0b101,      0b001,      0b101 ]
        self.ternary_f2                     = [      0b11,       0b11,       0b10,       0b10 ]
        self.ternary_f3_msbPos              = 14-3+1
        self.ternary_f2_msbPos              = 26-2+1

        # -- Ternary bitmanip Immediate Operations ---
        self.nb_op_ternary_imm              = 1
        self.opcode_ternary_imm             = [  0b0010011 ] * self.nb_op_ternary_imm

        self.ternary_imm_f3                 = [     0b101 ]
        self.ternary_imm_f1                 = [       0b1 ]
        self.ternary_imm_f3_msbPos          = 14-3+1
        self.ternary_imm_f1_msbPos          = 26-1+1

        self.logical_instructions           = []
        self.shift_instructions             = []
        self.singlebit_instructions         = []
        self.shift_imm_instructions         = []
        self.singlebit_imm_instructions     = []
        self.ternary_instructions           = []
        self.ternary_imm_instructions       = []
        self.all_instructions               = []

    def get_instructions_logical ( self ):

        self.logical_instructions           = []
        for i in range ( self.nb_op_logical ):
            instr = self.logical_f7[i] << self.logical_f7_msbPos | self.logical_f3[i] << self.logical_f3_msbPos | self.opcode_logical[i]
            self.logical_instructions.append( instr )

        return self.logical_instructions


    def get_instructions_shift ( self ):

        self.shift_instructions           = []
        for i in range ( self.nb_op_shift ):
            instr = self.shift_f7[i] << self.shift_f7_msbPos | self.shift_f3[i] << self.shift_f3_msbPos | self.opcode_shift[i]
            self.shift_instructions.append( instr )

        return self.shift_instructions


    def get_instructions_singlebit ( self ):

        self.singlebit_instructions           = []
        for i in range ( self.nb_op_singlebit ):
            instr = self.singlebit_f7[i] << self.singlebit_f7_msbPos | self.singlebit_f3[i] << self.singlebit_f3_msbPos | self.opcode_singlebit[i]
            self.singlebit_instructions.append( instr )

        return self.singlebit_instructions


    def get_instructions_shift_imm ( self ):

        self.shift_imm_instructions           = []
        for i in range ( self.nb_op_shift_imm ):
            instr = self.shift_imm_f5[i] << self.shift_imm_f5_msbPos | self.shift_imm_f3[i] << self.shift_imm_f3_msbPos | self.opcode_shift_imm[i]
            self.shift_imm_instructions.append( instr )

        return self.shift_imm_instructions


    def get_instructions_singlebit_imm ( self ):

        self.singlebit_imm_instructions           = []
        for i in range ( self.nb_op_singlebit_imm ):
            instr = self.singlebit_imm_f5[i] << self.singlebit_imm_f5_msbPos | self.singlebit_imm_f3[i] << self.singlebit_imm_f3_msbPos | self.opcode_singlebit_imm[i]
            self.singlebit_imm_instructions.append( instr )

        return self.singlebit_imm_instructions


    def get_instructions_ternary ( self ):

        self.ternary_instructions           = []
        for i in range ( self.nb_op_ternary ):
            instr = self.ternary_f2[i] << self.ternary_f2_msbPos | self.ternary_f3[i] << self.ternary_f3_msbPos | self.opcode_ternary[i]
            self.ternary_instructions.append( instr )

        return self.ternary_instructions


    def get_instructions_ternary_imm ( self ):

        self.ternary_imm_instructions           = []
        for i in range ( self.nb_op_ternary_imm ):
            instr = self.ternary_imm_f1[i] << self.ternary_imm_f1_msbPos | self.ternary_imm_f3[i] << self.ternary_imm_f3_msbPos | self.opcode_ternary_imm[i]
            self.ternary_imm_instructions.append( instr )

        return self.ternary_imm_instructions


    def get_instructions_all ( self ):

        self.all_instructions = []
        self.all_instructions.extend(self.get_instructions_logical())
        self.all_instructions.extend(self.get_instructions_shift())
        self.all_instructions.extend(self.get_instructions_singlebit())
        self.all_instructions.extend(self.get_instructions_shift_imm())
        self.all_instructions.extend(self.get_instructions_singlebit_imm())
        self.all_instructions.extend(self.get_instructions_ternary())
        self.all_instructions.extend(self.get_instructions_ternary_imm())

        return self.all_instructions
