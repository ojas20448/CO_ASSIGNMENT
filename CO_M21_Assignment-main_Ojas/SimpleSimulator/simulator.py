import sys


def initialize(memory):
    for i in range(256):
        memory.append('0000000000000000')


# setup the memory
PC = 0
memory = []
initialize(memory)

# take inputs

# print(0)
instructions = sys.stdin.readlines()
# print('\n'+'0')
# print(instructions)
for i in range(len(instructions)):
    if i == len(instructions)-1:
        if(instructions[i].endswith('\n')):
            instructions[i] = instructions[i][:-2]
            break
        else:
            break
    instructions[i] = instructions[i][:-1]
if len(instructions[len(instructions)-1])<16:    
    instructions[len(instructions)-1]+='0'    
# print(instructions)    
# print(0)
counter = 0
for instruction in instructions:
    memory[counter] = instruction
    counter += 1

REGISTERS = []
FLAGS = ''
for i in range(16):
    FLAGS += '0'
for i in range(7):
    s = ""
    for j in range(16):
        s = s+'0'
    REGISTERS.append(s)



def add(instruction):
    # print(2)
    global FLAGS
    global REGISTERS
    global PC
    global memory
    # 00000_00_000_000_000
    flag_reset()
    # print(3)
    reg1 = REGISTERS[int(instruction[7:10], 2)]
    reg2 = REGISTERS[int(instruction[10:13], 2)]
    reg3 = REGISTERS[int(instruction[13:16], 2)]
    temp = bin(int(reg2, 2) + int(reg3, 2)).replace('0b', '')
    while(len(temp) < 16):
        temp = '0'+temp
    # print(4)
    if(int(temp, 2) > 65535):
        FLAGS = FLAGS[:-4]+'1000'
        pass
    # print(5)
    REGISTERS[int(instruction[7:10], 2)] = temp
    dump()
    # print(6)
    PC += 1


def sub(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    # print(REGISTERS)
    reg1 = REGISTERS[int(instruction[7:10], 2)]
    reg2 = REGISTERS[int(instruction[10:13], 2)]
    reg3 = REGISTERS[int(instruction[13:16], 2)]
    temp = int(reg2, 2) - int(reg3, 2)
    flag_reset()
    if(temp < 0):
        FLAGS = FLAGS[:-4]+'1000'
        temp = 0
    temp = bin(temp).replace('0b', '')
    while(len(temp) < 16):
        
        temp = '0'+temp
    REGISTERS[int(instruction[7:10], 2)] = temp
    # print(REGISTERS)
    dump()
    PC += 1


def moveImm(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    value = int(instruction[8:16], 2)

    temp = bin(value).replace('0b', '0')
    while(len(temp) < 16):
        temp = '0'+temp
    REGISTERS[int(instruction[5:8], 2)] = temp
    dump()
    PC += 1


def moveReg(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    reg1 = REGISTERS[int(instruction[10:13], 2)]
    try:
        reg2 = REGISTERS[int(instruction[13:16], 2)]
    except:
        reg2 = FLAGS
    flag_reset()
    REGISTERS[int(instruction[10:13], 2)] = reg2
    dump()
    PC += 1


def load(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    reg1 = REGISTERS[int(instruction[5:8], 2)]
    index = int(instruction[8:16], 2)
    REGISTERS[int(instruction[5:8], 2)] = memory[index]
    dump()
    PC += 1


def store(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    reg1 = REGISTERS[int(instruction[5:8], 2)]
    index = int(instruction[8:16], 2)
    memory[index] = reg1
    dump()
    PC += 1


def mul(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    reg1 = REGISTERS[int(instruction[7:10], 2)]
    reg2 = REGISTERS[int(instruction[10:13], 2)]
    reg3 = REGISTERS[int(instruction[13:16], 2)]
    temp = bin(int(reg2, 2)*int(reg3, 2)).replace('0b', '')
    while(len(temp) < 16):
        temp = '0'+temp

    if(int(temp, 2) > 65535):
        FLAGS = FLAGS[:-4]+'1000'
        pass
    REGISTERS[int(instruction[7:10], 2)] = temp
    dump()
    PC += 1


def div(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    reg3 = REGISTERS[int(instruction[10:13], 2)]
    reg4 = REGISTERS[int(instruction[13:16], 2)]
    temp1 = bin(int(reg3, 2)//int(reg4, 2)).replace('0b', '')
    temp2 = bin(int(reg3, 2) % int(reg4, 2)).replace('0b', '')
    while(len(temp1) < 16):
        temp1 = '0'+temp1
    while(len(temp2) < 16):
        temp2 = '0'+temp2
    REGISTERS[0] = temp1
    REGISTERS[1] = temp2
    dump()
    PC += 1


def rs(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    value = int(instruction[8:16], 2)
    # >>
    reg = REGISTERS[int(instruction[5:8], 2)]
    temp = int(reg, 2) >> value
    temp = bin(temp).replace('0b', '')
    while(len(temp) < 16):
        temp = '0'+temp
    REGISTERS[int(instruction[5:8], 2)] = temp
    dump()
    PC += 1
    pass


def ls(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    value = int(instruction[8:16], 2)
    # >>
    reg = REGISTERS[int(instruction[5:8], 2)]
    temp = int(reg, 2) << value
    temp = bin(temp).replace('0b', '')
    while(len(temp) < 16):
        temp = '0'+temp
    REGISTERS[int(instruction[5:8], 2)] = temp
    dump()
    PC += 1
    pass


def Xor(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    reg1 = REGISTERS[int(instruction[7:10], 2)]
    reg2 = REGISTERS[int(instruction[10:13], 2)]
    reg3 = REGISTERS[int(instruction[13:16], 2)]
    temp = bin(int(reg2, 2) ^ int(reg3, 2)).replace('0b', '')
    while(len(temp) < 16):
        temp = '0'+temp

    REGISTERS[int(instruction[7:10], 2)] = temp
    dump()
    PC += 1
    pass


def Or(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    reg1 = REGISTERS[int(instruction[7:10], 2)]
    reg2 = REGISTERS[int(instruction[10:13], 2)]
    reg3 = REGISTERS[int(instruction[13:16], 2)]
    temp = bin(int(reg2, 2) | int(reg3, 2)).replace('0b', '')
    while(len(temp) < 16):
        temp = '0'+temp

    REGISTERS[int(instruction[7:10], 2)] = temp
    dump()
    PC += 1
    pass


def And(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    reg1 = REGISTERS[int(instruction[7:10], 2)]
    reg2 = REGISTERS[int(instruction[10:13], 2)]
    reg3 = REGISTERS[int(instruction[13:16], 2)]
    temp = bin(int(reg2, 2) & int(reg3, 2)).replace('0b', '')
    while(len(temp) < 16):
        temp = '0'+temp

    REGISTERS[int(instruction[7:10], 2)] = temp
    dump()
    PC += 1
    pass


def Not(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    reg1 = REGISTERS[int(instruction[10:13], 2)]
    reg2 = REGISTERS[int(instruction[13:16], 2)]
    temp = bin(~int(reg2, 2)).replace('0b', '')
    while(len(temp) < 16):
        temp = '0'+temp

    REGISTERS[int(instruction[10:13], 2)] = temp
    dump()
    PC += 1


def cmp(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    reg1 = REGISTERS[int(instruction[10:13], 2)]
    reg2 = REGISTERS[int(instruction[13:16], 2)]
    flag_reset()
    temp1 = int(reg1, 2)
    temp2 = int(reg2, 2)
    if(temp1 == temp2):  # equal tp flag
        FLAGS = FLAGS[:-1]+'1'
    elif(temp1 > temp2):
        FLAGS = FLAGS[:-2]+'10'
    else:
        FLAGS = FLAGS[:-3]+'100'
    # set flags here according to the register's values
    dump()
    PC += 1
    pass


def jmp(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    PC = int(instruction[9:16], 2)
    dump()
    pass


def jlt(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory

    if FLAGS[-3] == '1':
        PC = int(instruction[9:16], 2)
        flag_reset()
        dump()
    else:
        flag_reset()
        dump()
        PC += 1


def jgt(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    # according to flags
    if FLAGS[-2] == '1':
        PC = int(instruction[9:16], 2)
        flag_reset()
        dump()
    else:
        flag_reset()
        dump()
        PC += 1

    pass


def je(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    # according to flags
    if FLAGS[-1] == '1':
        PC = int(instruction[9:16], 2)
        flag_reset()
        dump()
    else:
        flag_reset()
        dump()
        PC += 1

    pass


def hlt():
    global FLAGS
    global REGISTERS
    global PC
    global memory
    flag_reset()
    dump()
    PC += 1
    pass


def flag_reset():
    global FLAGS
    global REGISTERS
    global PC
    global memory
    FLAGS = '0000000000000000'


def dump():
    global FLAGS
    global REGISTERS
    global PC
    global memory
    pc = bin(PC).replace('0b', '')
    while(len(pc) < 8):
        pc = '0'+pc
    print(pc, end=' ')
    for reg in REGISTERS:
        print(reg, end=" ")
    print(FLAGS)
    pass


def simulator(instruction):
    global FLAGS
    global REGISTERS
    global PC
    global memory
    opcodes = ['00000', '00001', '00010', '00011', '00100', '00101', '00110', '00111', '01000',
               '01001', '01010', '01011', '01100', '01101', '01110', '01111', '10000', '10001', '10010', '10011']
    index = opcodes.index(str(instruction)[0:5])
    index+=1
    if index == 1:
        # print(1)
        add(instruction)
        pass
    elif index == 2:
        sub(instruction)
        pass
    elif index == 3:
        moveImm(instruction)
        pass
    elif index == 4:
        moveReg(instruction)
        pass
    elif index == 5:
        load(instruction)
        pass
    elif index == 6:
        store(instruction)
        pass
    elif index == 7:
        mul(instruction)
        pass
    elif index == 8:
        div(instruction)
        pass
    elif index == 9:
        rs(instruction)
        pass
    elif index == 10:
        ls(instruction)
        pass
    elif index == 11:
        Xor(instruction)
        pass
    elif index == 12:
        Or(instruction)
        pass
    elif index == 13:
        And(instruction)
        pass
    elif index == 14:
        Not(instruction)
        pass
    elif index == 15:
        cmp(instruction)
        pass
    elif index == 16:
        jmp(instruction)
        pass
    elif index == 17:
        jlt(instruction)
        pass
    elif index == 18:
        jgt(instruction)
        pass
    elif index == 19:
        je(instruction)
        pass
    elif index == 20:
        hlt()
        pass


halt = False
# print(0)
while halt == False:
    # print(instructions[PC][0:5])
    if instructions[PC][0:5] == '10011':
        halt = True
    # print(1)
    simulator(instructions[PC])
    # if instruction is hlt
    # print(1)c
for m in memory:
    print(m)
