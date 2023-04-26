fh=open("testcase.txt",'r+')
dicttoholdval={'R0': '0000000000000000', 
               'R1': '0000000000000000',
               'R2': '0000000000000000',
               'R3': '0000000000000000',
               'R4': '0000000000000000',
               'R5': '0000000000000000',
               'R6': '0000000000000000',
               'FLAG': '0000000000000000'} # dictionary to hold value set pairs with registers
dictregister={'R0':'000','R1':'001','R2':'010','R3':'011',"R4":'100',"R5":'101','R6':'110','FLAGS':'111'}
l=[] # creating new list to add the series of intructions in stack form LIFO
def stack(l,x):
    # print(x)
    l.append(x)
def printing(x):
    print(x)
def binaryToDecimal(binary):
 
    d=i=0
    while binary!=0:
        s=binary%10
        d+=(s*(2**i))
        binary//=10
        i+=1
    return d
while True:
    k=fh.readline().split() # opening the file 
    if k[0]=='add':
        op=binaryToDecimal(int(dicttoholdval[k[2]]))+binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
        dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
        p='0000000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
        # printing(dicttoholdval[k[1]])
        stack(l,p)
    elif k[0]=='mov' and k[2].count('$')==1:
        dicttoholdval[k[1]]='0'*(16-len((str(bin(int(k[2][1::])))[2::])))+(str(bin(int(k[2][1::])))[2::])
        p='000100'+dictregister[k[1]]+('0'*(7-len((str(bin(int(k[2][1::])))[2::])))+(str(bin(int(k[2][1::])))[2::]))
        # printing(dicttoholdval[k[1]])
        stack(l,p)
    elif k[0]=='mov' and k[2].count('$'==0) :
        dicttoholdval[k[1]]=dicttoholdval[k[2]]
        op='0001100000'+dictregister[k[1]]+dictregister[k[2]]
        # printing(dicttoholdval[k[1]])
        stack(l,op)
    elif k[0]=='sub':
        op=binaryToDecimal(int(dicttoholdval[k[2]]))-binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
        dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
        p='0000100'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
        # printing(dicttoholdval[k[1]])
        stack(l,p)
    elif k[0]=='ld':
        p='001000'+dictregister[k[1]]+dicttoholdval[k[2]]
        dicttoholdval[k[1]]=dicttoholdval[k[2]]
        stack(l,p)
    elif k[0]=='st':
        dicttoholdval[k[2]]=dicttoholdval[k[1]]
        p='001010'+dictregister[k[1]]+dicttoholdval[k[1]][8:]
        stack(l,p)
    elif k[0]=='mul':
        op=binaryToDecimal(int(dicttoholdval[k[2]]))*binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
        dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
        p='0011000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
        # printing(dicttoholdval[k[1]])
        stack(l,p)
    elif k[0]=='div': # INCOMPLETE 
        if int(dicttoholdval[k[3]])==0:
            dicttoholdval['FLAG'][-4]=1
            
        op=binaryToDecimal(int(dicttoholdval[k[2]]))/binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
        dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
        p='0011000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
        # printing(dicttoholdval[k[1]])
        stack(l,p)
    elif k[0]=='xor':
        op=binaryToDecimal(int(dicttoholdval[k[2]]))*binaryToDecimal(int(dicttoholdval[k[3]]))
        op='0'*(16-len(str(op)))+str(op)
        dicttoholdval[k[1]]=op
        p='0101000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
        stack(l,p)
    elif k[0]=='rs' and k[2].count('$')==1:
        op=binaryToDecimal(int(dicttoholdval[k[1]])) # conversion to decimal takes place here
        op=op>>int(k[2][1::]) # Right shiing of bits 
        op=bin(op)[2::]
        op='0'*(16-len(str(op)))+str(op)
        dicttoholdval[k[1]]=op
        ty='0'*(7-len(str((bin(int(k[2][1::])))[2::])))+str((bin(int(k[2][1::])))[2::]) # conversion in seven bits binary of entered value
        p='010000'+dictregister[k[1]]+ty
        # print(p)
        stack(l,p)
    elif k[0]=='ls' and k[2].count('$')==1:
        op=binaryToDecimal(int(dicttoholdval[k[1]])) # conversion to decimal takes place here
        op=op<<int(k[2][1::]) # Left shiing of bits
        op=bin(op)[2::]
        op='0'*(16-len(str(op)))+str(op)
        dicttoholdval[k[1]]=op
        ty='0'*(7-len(str((bin(int(k[2][1::])))[2::])))+str((bin(int(k[2][1::])))[2::]) # conversion in seven bits binary of entered value
        p='010010'+dictregister[k[1]]+ty
        # print(p)
        stack(l,p)
    elif k[0]=='or':
        op1=binaryToDecimal(int(dicttoholdval[k[2]]))
        op2=binaryToDecimal(int(dicttoholdval[k[3]]))
        opi=op1|op2
        opi=bin(opi)[2::]
        op='0'*(16-len(str(opi)))+str(opi)
        # print(dicttoholdval)
        dicttoholdval[k[1]]=op
        p='0101100'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]]
        stack(l,p)
    elif k[0]=='and':
        op1=binaryToDecimal(int(dicttoholdval[k[2]]))
        op2=binaryToDecimal(int(dicttoholdval[k[3]]))
        opi=op1&op2
        opi=bin(opi)[2::]
        op='0'*(16-len(str(opi)))+str(opi)
        # print(dicttoholdval)
        dicttoholdval[k[1]]=op
        p='0110000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]]
        stack(l,p)
    elif k[0]=='not':
        pil,new_val=dicttoholdval[k[2]],''
        for i in pil:
            if i=='1':new_val+='0'
            else: new_val+='1'
        dicttoholdval[k[1]]=new_val
        p='0110100000'+dictregister[k[1]]+dictregister[k[2]]
        stack(l,p)
    elif k[0]=='hlt':
        break
print(l)
print(dicttoholdval)