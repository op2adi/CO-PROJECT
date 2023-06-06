import sys
import math
dicttoholdval={'R0': '0000000000000000', 
               'R1': '0000000000000000',
               'R2': '0000000000000000',
               'R3': '0000000000000000',
               'R4': '0000000000000000',
               'R5': '0000000000000000',
               'R6': '0000000000000000',
               'FLAGS': '0000000000000000'} # dictionary to hold value set pairs with registers
tmpdict=[] # to store variables
dictregister={'000': 'R0', '001': 'R1', '010': 'R2', '011': 'R3', '100': 'R4', '101': 'R5', '110': 'R6', '111': 'FLAGS'}
# a='0'*16
# kpp=0
mem_addr=[str((x*0))*16 for x in range(0,128)]
# print(mem_addr)
# print(len(mem_addr))

def fl(): # resetting flag to its optimal value or we can say resetting flag
    dicttoholdval['FLAGS']='0'*16

l=[] # creating new list to add the series of intructions in stack form LIFO
c=0
fg=0
def stack(l,x): # stack Maintaing machine codes works on lifo order
    # print(x)
    l.append(x)
def printing(x): # helper function to print values checking errors
    print(x)
def binaryToDecimal(binary): # helper function to convert binary to decimal
 
    d=i=0
    while binary!=0:
        s=binary%10
        d+=(s*(2**i))
        binary//=10
        i+=1
    return d
def pc(programcounter):
    print((7-len(str(bin(programcounter))[2::]))*'0'+str(bin(programcounter))[2::],end='        ')
def printingofregisters():
    print(' '.join(list(dicttoholdval.values())))

count=-1
hlt_ct=0
lopi=[]
verdict=0
def decimal_to_binary_custom(decimal_number, integer_bits, fractional_bits):
    if decimal_number>31.5 or decimal_number<0.125:
        print("ILLEGAL VALUE")
        print("EITHER value is less or bigger")
        sys.exit(0)
    integer_part = int(decimal_number)
    fractional_part = decimal_number - integer_part

    # Convert integer part to binary
    binary_integer = bin(integer_part)[2:]

    # Convert fractional part to binary
    binary_fractional = ''
    # for _ in range(fractional_bits):
    #     fractional_part *= 2
    #     bit = int(fractional_part)
    #     binary_fractional += str(bit)
    #     fractional_part -= bit
    c=5
    # print(len(str(binary_integer)))
    while fractional_part!=1:
        if c<=len(str(binary_integer))-1:
            break
        # print(c,"loplop")
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fractional+=str(bit)
        fractional_part -=bit
        # print(binary_fractional)
        if fractional_part==0:
            fractional_part=1
        c-=1
    # print(len(binary_fractional))
    # print(binary_fractional)
    # binary_fractional=binary_fractional+'0'*(5-len(binary_fractional))
    binary_fractional=binary_integer[1::]+binary_fractional+'0'*(5-len(binary_integer[1::]+binary_fractional))
    # Add bias of 3 to the exponent part
    exponent_bias = 3
    exponent = len(binary_integer) -1 + exponent_bias
    if exponent>7:
        print("OVERFLOW ERROR")
        sys.exit()
    # Convert exponent to binary
    binary_exponent = bin(exponent)[2:].zfill(3)

    binary_number = binary_exponent+ binary_fractional
    return binary_number

def binaryfloatconverter(binary_number):
    # binary_number=binary_number[::-1]
    # binary_number=binary_number[0:8]
    # binary_number=binary_number[::-1]
    # print(binary_number)
    # binary_exponent = binary_number[:3]
    # exponent_bias = 3
    # exponent =binaryToDecimal(int(binary_exponent)) - exponent_bias

    # c=-1
    # decimal_number=0
    # for pot in binary_number[3::]:
    #     alu=2**c
    #     decimal_number+=int(pot)*alu
    # decimal_number=1+(decimal_number)
    # decimal_number=float(decimal_number)
    # print(exponent)
    # decimal_number=decimal_number*(10**exponent)
    # print(decimal_number)
    # return decimal_number
    binary_number=binary_number[::-1]
    binary_number=binary_number[0:8]
    binary_number=binary_number[::-1]
    # print(binary_number)
    exp=binary_number[0:3]
    exp=binaryToDecimal(int(exp))
    mant=binary_number[3:]
    # print(str(mant))
    fa=float('1.'+str(mant))
    if exp==2:
        fa=float('0.'+str(mant))
        exp=3
    # print(fa)
    # print(exp)
    fa=fa*(10**(int(exp)-3))
    kappa=str(fa).split('.')
    kappa[1]=kappa[1][0:5]
    # print(kappa)
    asdf=binaryToDecimal(int(kappa[0]))
    # print(asdf)
    udi=-1
    bdsm=0.0
    for popcorn in kappa[1]:
        wer=2**udi
        bdsm+=int(popcorn)*wer
        udi-=1
    # print(bdsm)
    # bdsm=binaryToDecimal(int(kappa[1]))
    # print(asdf+bdsm)
    return asdf+bdsm
    


integer_bits = 3
fractional_bits = 5
while True:  # label handling and variable definations
    try:
        ap=input().replace('\r','')
        lopi.append(ap)
    except:
        break

# DEFINING PROGRAM COUNTER
programcounter=-1
i=0
while i<len(lopi):
    # print(1)
    if lopi[i][0:5]=='00000':
        programcounter+=1
        a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]]))+binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
        # print(a)
        if a>2**16-1:
            dicttoholdval[dictregister[lopi[i][7:10]]]=16*'0'
            # print("Error: Program Counter Overflow")
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
        else:
            # print(dicttoholdval[dictregister[lopi[i][7:10]]])
            dicttoholdval[dictregister[lopi[i][7:10]]]=(16-len((str(bin(a))[2::])))*'0'+str(bin(a))[2::]
            fl()
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='00001':
        programcounter+=1
        a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]]))-binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
        if a<0:
            dicttoholdval[dictregister[lopi[i][7:10]]]=16*'0'
            # print("Error: Program Counter Overflow")
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            # print((7-len(str(bin(programcounter))[2::]))*'0'+str(bin(programcounter))[2::],end=' ')
            pc(programcounter)
            printingofregisters()
        else:
            dicttoholdval[dictregister[lopi[i][7:10]]]=(16-len((str(bin(a))[2::])))*'0'+str(bin(a))[2::]
            fl()
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='00010':
        programcounter+=1
        dicttoholdval[dictregister[lopi[i][6:9]]]=(16-len(lopi[i][9::]))*'0'+lopi[i][9::]
        fl()
        pc(programcounter)
        printingofregisters()
    elif lopi[i][0:5]=='00011':
        programcounter+=1
        dicttoholdval[dictregister[lopi[i][10:13]]]=dicttoholdval[dictregister[lopi[i][13:16]]]
        fl()
        pc(programcounter)
        printingofregisters()
    elif lopi[i][0:5]=='00100':
        programcounter+=1
        dicttoholdval[dictregister[lopi[i][6:9]]]=mem_addr[binaryToDecimal(int(lopi[i][9::]))]
        fl()
        pc(programcounter)
        printingofregisters()
        # fl()
    elif lopi[i][0:5]=='00101':
        programcounter+=1
        # dicttoholdval[dictregister[lopi[i][6:9]]]=(16-len(lopi[i][9::]))*'0'+lopi[i][9::]
        # lopi.append(dicttoholdval[dictregister[lopi[i][6:9]]])
        mem_addr[binaryToDecimal(int(lopi[i][9::]))]=dicttoholdval[dictregister[lopi[i][6:9]]]
        fl()
        pc(programcounter)
        printingofregisters()
        # fl()
    elif lopi[i][0:5]=='00110':
        programcounter+=1
        a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]]))*binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
        if a>2**16-1:
            dicttoholdval[dictregister[lopi[i][7:10]]]=16*'0'
            # print("Error: Program Counter Overflow")
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
        else:
            dicttoholdval[dictregister[lopi[i][7:10]]]=(16-len((str(bin(a))[2::])))*'0'+str(bin(a))[2::]
            fl()
            pc(programcounter)
            printingofregisters()
            # fl()
    elif lopi[i][0:5]=='00111':
        programcounter+=1
        try:
            a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]]))//binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
            dicttoholdval['R0']=(16-len(str(bin(a))[2::]))*'0'+str(bin(a))[2::]
            a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]]))%binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
            dicttoholdval['R1']=(16-len(str(bin(a))[2::]))*'0'+str(bin(a))[2::]
            fl()
            pc(programcounter)
            printingofregisters()
            # fl()
        except ZeroDivisionError:
            dicttoholdval['R0']=16*'0'
            # a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]]))%binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
            dicttoholdval['R1']=16*'0'
            # fl()
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='01000':
        programcounter+=1
        k=dicttoholdval[dictregister[lopi[i][6:9]]]
        l=binaryToDecimal(int(lopi[i][9::]))
        print(binaryToDecimal(int(k)))
        k=binaryToDecimal(int(k))>>l
        # print(k)
        # print(l)
        dicttoholdval[dictregister[lopi[i][6:9]]]=(16-len(str(bin(k))[2::]))*'0'+str(bin(k))[2::]
        fl()
        pc(programcounter)
        printingofregisters()
        # fl()
    elif lopi[i][0:5]=='01001':
        programcounter+=1
        k=dicttoholdval[dictregister[lopi[i][6:9]]]
        l=binaryToDecimal(int(lopi[i][9::]))
        print(binaryToDecimal(int(k)))
        k=binaryToDecimal(int(k))<<l
        # print(k)
        # print(l)
        dicttoholdval[dictregister[lopi[i][6:9]]]=(16-len(str(bin(k))[2::]))*'0'+str(bin(k))[2::]
        fl()
        pc(programcounter)
        printingofregisters()
        # fl()
    elif lopi[i][0:5]=='01010':
        programcounter+=1
        a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]]))^binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
        dicttoholdval[dictregister[lopi[i][7:10]]]=(16-len((str(bin(a))[2::])))*'0'+str(bin(a))[2::]
        fl()
        pc(programcounter)
        printingofregisters()
        # fl()
    elif lopi[i][0:5]=='01011':
        programcounter+=1
        a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]])) or binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
        dicttoholdval[dictregister[lopi[i][7:10]]]=(16-len((str(bin(a))[2::])))*'0'+str(bin(a))[2::]
        fl()
        pc(programcounter)
        printingofregisters()
        # fl()
    elif lopi[i][0:5]=='01100':
        programcounter+=1
        a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]])) and binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:17]]]))
        dicttoholdval[dictregister[lopi[i][7:10]]]=(16-len((str(bin(a))[2::])))*'0'+str(bin(a))[2::]
        fl()
        pc(programcounter)
        printingofregisters()
        # fl()
    elif lopi[i][0:5]=='01101':
        programcounter+=1
        pil,new_val=dicttoholdval[dictregister[lopi[i][13::]]],''
        for j in pil:
            if j=='1':new_val+='0'
            else: new_val+='1'
        dicttoholdval[dictregister[lopi[i][10:13]]]=new_val
        fl()
        pc(programcounter)
        printingofregisters()
        # fl()
    elif lopi[i][0:5]=='01110':
        programcounter+=1
        kp=dicttoholdval[dictregister[lopi[i][10:13]]]
        qw=dicttoholdval[dictregister[lopi[i][13::]]]
        if kp==qw:
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:15]+'1'
        elif kp<qw:
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:13]+'1'+dicttoholdval['FLAGS'][14::]
        else:
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:14]+'1'+dicttoholdval['FLAGS'][15]
        pc(programcounter)
        printingofregisters()
    elif lopi[i][0:5]=='01111':
        programcounter+=1
        i=binaryToDecimal(int(lopi[i][5::]))-1
        fl()
        pc(programcounter)
        printingofregisters()
        programcounter=i
        # fl()
    elif lopi[i][0:5]=='11100':
        programcounter+=1
        if dicttoholdval['FLAGS'][-3]=='1':
            i=binaryToDecimal(int(lopi[i][5::]))-1
            fl()
            pc(programcounter)
            printingofregisters()
            programcounter=i
        else:
            fl()
            pc(programcounter)
            printingofregisters()  
    elif lopi[i][0:5]=='11101':
        programcounter+=1
        if dicttoholdval['FLAGS'][-2]=='1':
            i=binaryToDecimal(int(lopi[i][5::]))-1
            fl()
            pc(programcounter)
            printingofregisters()
            programcounter=i
        else:
            fl()
            pc(programcounter)
            printingofregisters()  
            # fl()
    elif lopi[i][0:5]=='11111':
        programcounter+=1
        if dicttoholdval['FLAGS'][-1]=='1':
            i=binaryToDecimal(int(lopi[i][5::]))-1
            fl()
            pc(programcounter)
            printingofregisters()
            programcounter=i
            # fl()
        else:
            fl()
            pc(programcounter)
            printingofregisters() 
            # fl()
    elif lopi[i][0:5]=='10000':
        programcounter+=1
        # a=dicttoholdval[dictregister[lopi[i][7:10]]]
        # print([lopi[i][10:13]])
        # print(dicttoholdval[dictregister[lopi[i][10:13]]])
        # print(dicttoholdval[dictregister[lopi[i][13:16]]])
        b=binaryfloatconverter(dicttoholdval[dictregister[lopi[i][10:13]]])+binaryfloatconverter(dicttoholdval[dictregister[lopi[i][13:16]]])
        # print(b)
        if b>31.5:
            dicttoholdval[dictregister[lopi[i][7:10]]]='0'*16
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
        else:
            print('0'*8+decimal_to_binary_custom(b,3,5))
            dicttoholdval[dictregister[lopi[i][7:10]]]='0'*8+decimal_to_binary_custom(b,3,5)
            fl()
            # dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='10010':
        programcounter+=1
        decimal_number=lopi[i][8::]
        dicttoholdval[dictregister[lopi[i][5:8]]]='0'*8+(decimal_number)
        fl()
        pc(programcounter)
        printingofregisters()
    elif lopi[i][0:5]=='10001':
        programcounter+=1
        # a=dicttoholdval[dictregister[lopi[i][7:10]]]
        # print([lopi[i][10:13]])
        # print(dicttoholdval[dictregister[lopi[i][10:13]]])
        # print(dicttoholdval[dictregister[lopi[i][13:16]]])
        b=binaryfloatconverter(dicttoholdval[dictregister[lopi[i][10:13]]])-binaryfloatconverter(dicttoholdval[dictregister[lopi[i][13:16]]])
        # print(b)
        if b<0.125:
            dicttoholdval[dictregister[lopi[i][7:10]]]='0'*16
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
        else:
            print('0'*8+decimal_to_binary_custom(b,3,5))
            dicttoholdval[dictregister[lopi[i][7:10]]]='0'*8+decimal_to_binary_custom(b,3,5)
            fl()
            # dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='10011': # bonus 1 power calculator
        programcounter+=1
        a=binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][10:13]]]))**binaryToDecimal(int(dicttoholdval[dictregister[lopi[i][13:16]]]))
        if a>2**16-1:
            dicttoholdval[dictregister[lopi[i][7:10]]]='0'*16
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
        else:
            dicttoholdval[dictregister[lopi[i][7:10]]]='0'*(16-len(str(bin(a))[2::]))+str(bin(a))[2::]
            fl()
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='10100': # 2 add immidiate
        programcounter+=1
        a=dicttoholdval[dictregister[lopi[i][6:9]]]
        b=lopi[i][9::]
        # b='0'*(7-len(b))+b
        s=binaryToDecimal(int(a))+binaryToDecimal(int(b))
        if s>2**16-1:
            dicttoholdval[dictregister[lopi[i][6:9]]]='0'*16
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
        else:
            dicttoholdval[dictregister[lopi[i][6:9]]]='0'*(16-len(str(bin(s))[2::]))+str(bin(s))[2::]
            fl()
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='10101': # subtract immidiate
        programcounter+=1
        a=dicttoholdval[dictregister[lopi[i][6:9]]]
        b=lopi[i][9::]
        # b='0'*(7-len(b))+b
        s=binaryToDecimal(int(a))-binaryToDecimal(int(b))
        if s<0:
            dicttoholdval[dictregister[lopi[i][6:9]]]='0'*16
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
        else:
            dicttoholdval[dictregister[lopi[i][6:9]]]='0'*(16-len(str(bin(s))[2::]))+str(bin(s))[2::]
            fl()
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='10110': # 2 mul immidiate
        programcounter+=1
        a=dicttoholdval[dictregister[lopi[i][6:9]]]
        b=lopi[i][9::]
        # b='0'*(7-len(b))+b
        s=binaryToDecimal(int(a))*binaryToDecimal(int(b))
        if s>2**16-1:
            dicttoholdval[dictregister[lopi[i][6:9]]]='0'*16
            dicttoholdval['FLAGS']=dicttoholdval['FLAGS'][0:12]+'1'+dicttoholdval['FLAGS'][13::]
            pc(programcounter)
            printingofregisters()
        else:
            dicttoholdval[dictregister[lopi[i][6:9]]]='0'*(16-len(str(bin(s))[2::]))+str(bin(s))[2::]
            fl()
            pc(programcounter)
            printingofregisters()
    elif lopi[i][0:5]=='10111': # clears all registers and flags and all memory
        programcounter+=1
        dicttoholdval={'R0': '0000000000000000', 
               'R1': '0000000000000000',
               'R2': '0000000000000000',
               'R3': '0000000000000000',
               'R4': '0000000000000000',
               'R5': '0000000000000000',
               'R6': '0000000000000000',
               'FLAGS': '0000000000000000'} 
        mem_addr=[str((x*0))*16 for x in range(0,128)] # will not clean instructions memory
        fl()
        pc(programcounter)
        printingofregisters()
    elif lopi[i][0:5]=='11010':
        programcounter+=1
        fl()
        pc(programcounter)
        printingofregisters()
        cout=0
        for pk in lopi:
            print(pk)
            cout+=1
        for i in range(cout,128):
            print(mem_addr[i])
        fl()
        exit()
    i+=1




    
        

        
