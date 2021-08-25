def EvTypeA(instruction,typeA):
    index = list(typeA).index(instruction[0])
    opCodes = ['00000','00001','00110','01010','01011','01100']
    opcode = opCodes[index]
    if(len(instruction)!=4):
        print("Error: INVALID SYNTAX for",instruction[0],"evaluation.","in line","**"+str(line_no)+"**")
        return ""
    reg1 = instruction[1]
    reg2 = instruction[2]
    reg3 = instruction[3]
    registers123 = [reg1,reg2,reg3]
    # print(registers123)
    i=1
    for i in range(0,3):
        if registers123[i][0] != "R":
            # print(register)
            print("Error: INVALID SYNTAX, registers wrongly given","in line","**"+str(line_no)+"**")
            return ""   
        elif int(registers123[i][1])>=0 and int(registers123[i][1])<=6:
            s = bin(int(registers123[i][1]))
            registers123[i]=s[2:]
        while(len(registers123[i])!=3):
            registers123[i]='0'+registers123[i]    
        i+=1    
    binaryEncoding = opcode+"00"+registers123[0]+registers123[1]+registers123[2]                         
    return binaryEncoding        


def EvTypeB(instruction,typeB):
    opcodes=['01000','01001']
    index = list(typeB).index(instruction[0])
    opcode = instruction[index]
    register = instruction[1]
    if register[0]!='R':
        print("Error: invalid register given","in line","**"+str(line_no)+"**")
    try:
        s = bin(int(register[1]))
    except:
        print("Error: invalid register given","in line","**"+str(line_no)+"**")
        return    ""
    register = s[2:]
    
    val = instruction[2]
    print(val)
    if(val[0]!='$'):
        print("Error: $ sign was not used to initiate the immediate value","in line","**"+str(line_no)+"**")
        return ""
    try:
        val = int(val[1:])
        imm =bin(val)[2:]
        while(len(imm)!=8):
            imm = '0'+imm
    except:
        print("Error: Syntax error Invalid immediate value given","in line","**"+str(line_no)+"**")
        return  ""  
    while(len(register)!=3):
        register='0'+register    
    binaryEncoding = opcode+register+imm
    return binaryEncoding


def EvTypeC(instruction,typeC):
    if(len(instruction)!=3):
        print("Error: invalid Syntax","in line","**"+str(line_no)+"**")
        return ""
    index = list(typeC).index(instruction[0])
    opcodes=['00111','01101','01110']
    opcode = opcodes[index]
    registers12 = [instruction[1],instruction[2]]
    for i in range(0,2):
        if registers12[i][0]!='R':
            print("Error: Invalid registers used return","in line","**"+str(line_no)+"**")
            return ""
        try:
            registers12[i]= bin(int(registers12[i][1]))[2:]
        except:
            print("Error: Invalid registers used return","in line","**"+str(line_no)+"**")
            return ""
        while(len(registers12[i])!=3):
            registers12[i]="0"+registers12[i]    
    binaryEncoding=opcode+"00000"+registers12[0]+registers12[1]
    return binaryEncoding        


def EvTypeD(instruction,typeD,variables):
    if(len(instruction)!=3):
        print("Error: invalid Syntax","in line","**"+str(line_no)+"**")
        return ""
    index = list(typeD).index(instruction[0])
    opcodes=['00100','00101']
    opcode = opcodes[index]
    register = instruction[1]
    if register[0]!='R':
        print("Error: invalid register given","in line","**"+str(line_no)+"**")
        return  ""
    try:
        s = bin(int(register[1]))
    except:
        print("Error: invalid register given","in line","**"+str(line_no)+"**")
        return  ""  
    register = s[2:]
    memr_add = bin(int(variables[instruction[2]]))[2:]
    while(len(memr_add)!=8):
        memr_add = '0'+memr_add
    while(len(register)!=3):
        register='0'+register    
    while(len(register)!=3):
        register='0'+register    
    binaryEncoding=opcode+register+memr_add
    return binaryEncoding
    

def EvTypeE(instruction,typeE,labels):
    if(len(instruction)!=2):
        print("Error: invalid Syntax","in line","**"+str(line_no)+"**")
        return ""
    index = list(typeE).index(instruction[0])
    opcodes=['01111','10000','10001','10010']
    opcode = opcodes[index]
    memr_add = bin(int(labels[instruction[1]]))[2:]
    while(len(memr_add)!=8):
        memr_add = '0'+memr_add
    binaryEncoding=opcode+'000'+memr_add
    return binaryEncoding


def EvTypeF(instruction):
    if(len(instruction)!=1):
        print("Error: Invalid syntax","in line","**"+str(line_no)+"**")
        return ""
    opcode='10011'    
    binaryEncoding=opcode+'00000000000'
    return binaryEncoding

def EvTypeBorC(instruction):
    if str(instruction[2])[0]=='$':
        #it means its move immediate
        opcode='00010'
        register = instruction[1]
        if register[0]!='R':
            print("Error: invalid register given","in line","**"+str(line_no)+"**")
            return ""
        try:
            s = bin(int(register[1]))
        except:
            print("Error: invalid register given","in line","**"+str(line_no)+"**")
            return ""    
        register = s[2:]
        
        val = instruction[2]
        # print(instruction)
        # print(val)
        if(val[0]!='$'):
            print("Error: $ sign was not used to initiate the immediate value","in line","**"+str(line_no)+"**")
            return ""
        try:
            val = int(val[1:])
            imm =bin(val)[2:]
            while(len(imm)!=8):
                imm = '0'+imm

        except:
            print("Error: Syntax error Invalid immediate value given","in line","**"+str(line_no)+"**")
            return  ""  
        while(len(register)!=3):
            register='0'+register    
        binaryEncoding = opcode+register+imm
        return binaryEncoding
    else:
        #it is move register type c
        opcode='00011'
        registers12 = [instruction[1],instruction[2]]
        for i in range(0,2):
            try:
                if(registers12[i]=='FLAGS'):
                    registers12[i]='111'
                    continue

                registers12[i]= bin(int(registers12[i][1]))[2:]
            except:
                print(registers12)
                print("Error: Invalid registers used return","in line","**"+str(line_no)+"**")
                return ""
            while(len(registers12[i])!=3):
                registers12[i]='0'+registers12[i]    
        binaryEncoding=opcode+"00000"+registers12[0]+registers12[1]
        return binaryEncoding        


def assembler(command,variables,labels,isStarted,line_no,size,countVar,countLab):
    command = list(command)
    
    output_encoding = ""
    typeA = ['add','sub','mul','xor','or','and']
    typeB = ['rs','ls']
    typeC = ['div','not','cmp']
    typeD = ['ld','st']
    typeE = ['jmp','jlt','jgt','je']
    typeF =['hlt']
    typeBorC = ['mov']
    
    if command[0] == 'var':
        if(len(command)!=2):
            print("Error: Invalid Syntax, illegal declaretion of variable","in line","**"+str(line_no)+"**")
            return ""
        if(isStarted==False):
            variables[command[1]] = size-countLab-countVar+len(variables)
            output_encoding=bin(int(variables[command[1]]))[2:]
            return ""
        else:
            
            print("Error:invalid Syntax, illegal declaretion of variable","in line","**"+str(line_no)+"**") 
            return "" 
    else: 
        isStarted=True        
    if command[0] in typeA:
        output_encoding=(EvTypeA(command,typeA))
    elif command[0] in typeB:
        output_encoding=(EvTypeB(command,typeB))
    elif command[0] in typeC:
        output_encoding=(EvTypeC(command,typeC))
    elif command[0] in typeD:
        output_encoding=(EvTypeD(command,typeD,variables))
    elif command[0] in typeE:
        output_encoding=(EvTypeE(command,typeE,labels))
    elif command[0] in typeF:
        output_encoding=(EvTypeF(command))
    elif command[0] in typeBorC:
        output_encoding=EvTypeBorC(command)
    else:
        print("Error: Invalid instruction was given","in line","**"+str(line_no)+"**")
        return ""

    return output_encoding    
    

import sys
commands = sys.stdin.readlines()
for i in range(len(commands)):
    if i == len(commands)-1:
        if(commands[i].endswith('\n')):
            commands[i]=commands[i][:-2]
            break
        else:
            break
    commands[i]=commands[i][:-1]
# print(commands)

variables={} 
labels = {} 
output_encoding=""
line_no=1
size=len(commands)
countVar=0
for line in commands:
    c = line.split(" ")

    while (c[0]==" "):
        c.pop(0)
    if(c[0]!='var'):
        break
    countVar+=1
countLab=0
for line in commands:
    c = line.split(" ")

    while (c[0]==" "):
        c.pop(0)
    if c[0][-1] == ':' and c[0][-2]!=' ':
        countLab+=1
i=1        
for command in commands:
    c = command.split(' ')
    while (c[0]==" "):
        c.pop(0)
    if str(c[0]).endswith(':') and c[0][-1]!=' ':
            # labels
            if(len(c)<2):
                print("Error: Invalid Syntax, illegal declaretion of variable","in line","**"+str(i)+"**")
                break
            labels[c[0][:-1]]=size-countLab-countVar+len(labels)
            # print(i,size,countLab,countVar)
            c.pop(0)
            commands[i-1] = ' '.join(c)
    if str(c[0]).endswith(':') and c[0][-1]==' ':
        print("Error: Invalid Syntax, illegal declaretion of variable","in line","**"+str(i)+"**")
        break

    i+=1        
# print(labels)    
if commands[-1]!='hlt':
    # print("hlt not being used as the last instruction")
    print("Error: hlt was not used as the last instructor.")

for line in commands:
    c = line.split(" ")

    while (c[0]==" "):
        c.pop(0)

    # print(c)
    isStarted=False
    temp = assembler(c,variables,labels,isStarted,line_no,size,countVar,countLab)
    if temp != "":
        output_encoding+=(temp)+'\n'
    line_no+=1
    if len(c)==1 and c[0]=='hlt':
        break
    
print(output_encoding)
