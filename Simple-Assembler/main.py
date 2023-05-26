# have to ask gupta about some issues faced by me in jump statements
# fh=open(r"D:\CO PROJECT @)@#\testcase.txt",'r+')
import sys
dicttoholdval={'R0': '0000000000000000', 
               'R1': '0000000000000000',
               'R2': '0000000000000000',
               'R3': '0000000000000000',
               'R4': '0000000000000000',
               'R5': '0000000000000000',
               'R6': '0000000000000000',
               'FLAGS': '0000000000000000'} # dictionary to hold value set pairs with registers
tmpdict=[] # to store variables
dictregister={'R0':'000','R1':'001','R2':'010','R3':'011',"R4":'100',"R5":'101','R6':'110','FLAGS':'111'}
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
count=-1
hlt_ct=0
lopi=[]
verdict=0
while True:  # label handling and variable definations
    try:
        ap=input()
        pa=ap.split()
        lopi.append(pa)
        # print(pa)
        #print(pa)
        if pa==[]:
            pass
        elif ap.count(':')==1:
            dicttoholdval[pa[0]]='0'*(7-len(((str(bin(verdict)))[2::])))+((str(bin(verdict)))[2::])
        elif ap.count(':')>1:
            print("SYNTAX ERROR IN LABEL")
            sys.exit()
        elif pa[0]=='var':
            tmpdict.append(pa[1])
        if verdict>127:
            break
        if pa[0]!='var':
            verdict+=1
    except:
        break

    
# fh.seek(0,0)
fg=0
for j in range(len(lopi)):
    p=lopi[j]
    # print(p)
    if p==[]:
        pass
    elif p[0]!='var' and p!=[]:
        c+=1
    elif 'jmp' in p:
        op=i
        kop=c
        for k in range(i):
            poc= lopi[k]
            # print(poc)
            if poc==[]:
                pass
            elif poc[0][0:-1]==p[1]:
                break
            kop+=1
            if kop>127:
                break
        # print(kop)
        dicttoholdval[p[1]]='0'*(7-len(str(bin(kop))[2::]))+(str(bin(kop))[2::])
    elif 'jlt' in p:
        op=i
        kop=c
        for k in range(len(lopi)):
            poc= lopi[k]
            # print(poc)
            if poc==[]:
                pass
            elif poc[0][0:-1]==p[1]:
                break
            kop+=1
            if kop>127:
                break
        # print(kop)
        dicttoholdval[p[1]]='0'*(7-len(str(bin(kop))[2::]))+(str(bin(kop))[2::])
    elif 'jgt' in p:
        op=i
        kop=c
        for k in range(i):
            poc= lopi[k]
            # print(poc)
            if poc==[]:
                pass
            elif poc[0][0:-1]==p[1]:
                break
            kop+=1
            if kop>127:
                break
        # print(kop)
        dicttoholdval[p[1]]='0'*(7-len(str(bin(kop))[2::]))+(str(bin(kop))[2::])
    elif 'je' in p:
        op=i
        kop=c
        for k in range(len(lopi)):
            poc= lopi[k]
            # print(poc)
            if poc==[]:
                pass
            elif poc[0][0:-1]==p[1]:
                break
            kop+=1
            if kop>127:
                break
        # print(kop)
        dicttoholdval[p[1]]='0'*(7-len(str(bin(kop))[2::]))+(str(bin(kop))[2::])
    if 'hlt' in p:
        hlt_ct+=1
    if count>127:
        pass
    count+=1
# print(c)
aditya=0
for j in range(len(lopi)):
    if not(hlt_ct):
        print("HALT is missing")
        sys.exit()
        break
    if hlt_ct>1:
        print("MORE THAN 1 HALT INSTRUCTION IS THERE")
        sys.exit()
    try:
        k=lopi[j] # opening the file 
        # print(k)
        if k[0]=='add':
            fg=1
            if len(k)!=4:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()  
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)         
            op=binaryToDecimal(int(dicttoholdval[k[2]]))+binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
            dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
            p='0000000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
            # printing(dicttoholdval[k[1]])
            stack(l,p)
        elif k[0]=='mov' and str(k[2]).count('$')==1:
            fg=1
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            if int(str(k[2])[1::])>127 or int(str(k[2])[1::])<-128:
                print("ELEMENT GREATER THAN 7 BIT APOLOGY SORRY \U0001F622")
                sys.exit()
            dicttoholdval[k[1]]='0'*(16-len((str(bin(int(k[2][1::])))[2::])))+(str(bin(int(k[2][1::])))[2::])
            p='000100'+dictregister[k[1]]+('0'*(7-len((str(bin(int(k[2][1::])))[2::])))+(str(bin(int(k[2][1::])))[2::]))
            # printing(dicttoholdval[k[1]])
            stack(l,p)
        elif k[0]=='mov' and str(k[2]).count('$')==0 :
            fg=1
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            dicttoholdval[k[1]]=dicttoholdval[k[2]]
            op='0001100000'+dictregister[k[1]]+dictregister[k[2]]
            # printing(dicttoholdval[k[1]])
            stack(l,op)
        elif k[0]=='sub':
            fg=1
            if len(k)!=4:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            op=binaryToDecimal(int(dicttoholdval[k[2]]))-binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
            dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
            p='0000100'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
            # printing(dicttoholdval[k[1]])
            stack(l,p)
        elif k[0]=='ld':
            fg=1
            if k[2] not in tmpdict:
                print(f"VARIABLE {k[2]} IS NOT DEFINED PLEASE CHECK")
                sys.exit()
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)              
            dicttoholdval[k[2]]="0"*(16-len(str(bin(c))[2::]))+str(bin(c))[2::]
            p='001000'+dictregister[k[1]]+dicttoholdval[k[2]][9:]
            stack(l,p)
            c+=1
        elif k[0]=='st':
            fg=1
            if k[2] not in tmpdict:
                print(f"VARIABLE {k[2]} IS NOT DEFINED PLEASE CHECK")
                sys.exit()
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit() 
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)            
            dicttoholdval[k[2]]="0"*(16-len(str(bin(c))[2::]))+str(bin(c))[2::]
            p='001010'+dictregister[k[1]]+dicttoholdval[k[2]][9:]
            stack(l,p)
            c+=1
        elif k[0]=='mul':
            fg=1
            if len(k)!=4:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            op=binaryToDecimal(int(dicttoholdval[k[2]]))*binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
            dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
            p='0011000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
            # printing(dicttoholdval[k[1]])
            stack(l,p)
        elif k[0]=='div': # INCOMPLETE 
            fg=1
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            p='0011100000'+dictregister[k[1]]+dictregister[k[2]]
            stack(l,p)
        elif k[0]=='xor':
            fg=1
            if len(k)!=4:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            op=binaryToDecimal(int(dicttoholdval[k[2]]))*binaryToDecimal(int(dicttoholdval[k[3]]))
            op='0'*(16-len(str(op)))+str(op)
            dicttoholdval[k[1]]=op
            p='0101000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
            stack(l,p)
        elif k[0]=='rs' and k[2].count('$')==1:
            fg=1
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
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
            fg=1
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
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
            fg=1
            if len(k)!=4:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
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
            fg=1
            if len(k)!=4:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
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
            fg=1
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            pil,new_val=dicttoholdval[k[2]],''
            for i in pil:
                if i=='1':new_val+='0'
                else: new_val+='1'
            dicttoholdval[k[1]]=new_val
            p='0110100000'+dictregister[k[1]]+dictregister[k[2]]
            stack(l,p)
        elif k[0]=='cmp':
            fg=1
            if len(k)!=3:
                print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            p='0111000000'+dictregister[k[1]]+dictregister[k[2]]
            stack(l,p)
        elif k[0]=='jmp':
            fg=1
            if len(k)!=2:
                print("HAVE MORE than 1 label")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            p='011110000'+dicttoholdval[k[1]+':']
            stack(l,p)
        elif k[0]=='jlt':
            fg=1
            if len(k)!=2:
                print("HAVE MORE than 1 label")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            p='11100000'+dicttoholdval[k[1]+':']
            stack(l,p)
        elif k[0]=='jgt':
            fg=1
            if len(k)!=2:
                print("HAVE MORE than 1 label")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            p='111010000'+dicttoholdval[k[1]+':']
            stack(l,p)
        elif k[0]=='je':
            fg=1
            if len(k)!=2:
                print("HAVE MORE than 1 label")
                sys.exit()
            if 'FLAGS' in k:
                print("Illegal use of Flags")
                sys.exit(0)  
            p='111110000'+dicttoholdval[k[1]+':']
            stack(l,p)
        elif 'hlt' in k and k[0].count(':')==0:
            if len(k)!=1:
                print("HAVE MORE than 1 label")
                sys.exit()
            p='11010'+'0'*11
            stack(l,p)
            if lopi[j+1::]!=[]:
                print("TRACED AN ERROR\nFOUND SOME COMMAND AFTER HALT INSTRUCTION")
                sys.exit()
            break
        elif k[0]=='var':
            if (fg):
                print("Variable declaration must not be after instruction")
                sys.exit()
            pass
        elif k[0].count(':')==1:
            p=k.pop(0)
            if k[0]=='add':
                if len(k)!=4:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)             
                op=binaryToDecimal(int(dicttoholdval[k[2]]))+binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
                dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
                p='0000000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
                # printing(dicttoholdval[k[1]])
                stack(l,p)
            elif k[0]=='mov' and str(k[2]).count('$')==1:
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                if int(str(k[2])[1::])>127 or int(str(k[2])[1::])<-128:
                    print("ELEMENT GREATER THAN 7 BIT APOLOGY SORRY \U0001F622")
                    sys.exit()
                dicttoholdval[k[1]]='0'*(16-len((str(bin(int(k[2][1::])))[2::])))+(str(bin(int(k[2][1::])))[2::])
                p='000100'+dictregister[k[1]]+('0'*(7-len((str(bin(int(k[2][1::])))[2::])))+(str(bin(int(k[2][1::])))[2::]))
                # printing(dicttoholdval[k[1]])
                stack(l,p)
            elif k[0]=='mov' and str(k[2]).count('$')==0 :
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                dicttoholdval[k[1]]=dicttoholdval[k[2]]
                op='0001100000'+dictregister[k[1]]+dictregister[k[2]]
                # printing(dicttoholdval[k[1]])
                stack(l,op)
            elif k[0]=='sub':
                if len(k)!=4:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                op=binaryToDecimal(int(dicttoholdval[k[2]]))-binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
                dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
                p='0000100'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
                # printing(dicttoholdval[k[1]])
                stack(l,p)
            elif k[0]=='ld':
                if k[2] not in tmpdict:
                    print(f"VARIABLE {k[2]} IS NOT DEFINED PLEASE CHECK")
                    sys.exit()
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)              
                dicttoholdval[k[2]]="0"*(16-len(str(bin(c))[2::]))+str(bin(c))[2::]
                p='001000'+dictregister[k[1]]+dicttoholdval[k[2]][9:]
                stack(l,p)
                c+=1
            elif k[0]=='st':
                if k[2] not in tmpdict:
                    print(f"VARIABLE {k[2]} IS NOT DEFINED PLEASE CHECK")
                    sys.exit()
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)             
                dicttoholdval[k[2]]="0"*(16-len(str(bin(c))[2::]))+str(bin(c))[2::]
                p='001010'+dictregister[k[1]]+dicttoholdval[k[2]][9:]
                stack(l,p)
                c+=1
            elif k[0]=='mul':
                if len(k)!=4:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                op=binaryToDecimal(int(dicttoholdval[k[2]]))*binaryToDecimal(int(dicttoholdval[k[3]])) # storing the added values to a temp variable but in decimal 
                dicttoholdval[k[1]]='0'*(16-len(str(bin(op))[2::]))+str(bin(op))[2::] # here  the register gets updated to new added values in the added previous registers that have 
                p='0011000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
                # printing(dicttoholdval[k[1]])
                stack(l,p)
            elif k[0]=='div': # INCOMPLETE 
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                p='0011100000'+dictregister[k[1]]+dictregister[k[2]]
                stack(l,p)
            elif k[0]=='xor':
                if len(k)!=4:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                op=binaryToDecimal(int(dicttoholdval[k[2]]))*binaryToDecimal(int(dicttoholdval[k[3]]))
                op='0'*(16-len(str(op)))+str(op)
                dicttoholdval[k[1]]=op
                p='0101000'+dictregister[k[1]]+dictregister[k[2]]+dictregister[k[3]] # we have to store it in 16 bits 5 bits reservered for opcode
                stack(l,p)
            elif k[0]=='rs' and k[2].count('$')==1:
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
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
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
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
                if len(k)!=4:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
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
                if len(k)!=4:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
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
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                pil,new_val=dicttoholdval[k[2]],''
                for i in pil:
                    if i=='1':new_val+='0'
                    else: new_val+='1'
                dicttoholdval[k[1]]=new_val
                p='0110100000'+dictregister[k[1]]+dictregister[k[2]]
                stack(l,p)
            elif k[0]=='cmp':
                if len(k)!=3:
                    print("HAVE EITHER MORE ARGUEMENTS OR LESS ARGUEMENTS")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                p='0111000000'+dictregister[k[1]]+dictregister[k[2]]
                stack(l,p)
            elif k[0]=='jmp':
                if len(k)!=2:
                    print("HAVE MORE than 1 label")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                p='011110000'+dicttoholdval[k[1]+':']
                stack(l,p)
            elif k[0]=='jlt':
                if len(k)!=2:
                    print("HAVE MORE than 1 label")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                p='11100000'+dicttoholdval[k[1]+':']
                stack(l,p)
            elif k[0]=='jgt':
                if len(k)!=2:
                    print("HAVE MORE than 1 label")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                p='111010000'+dicttoholdval[k[1]+':']
                stack(l,p)
            elif k[0]=='je':
                if len(k)!=2:
                    print("HAVE MORE than 1 label")
                    sys.exit()
                if 'FLAGS' in k:
                    print("Illegal use of Flags")
                    sys.exit(0)  
                p='111110000'+dicttoholdval[k[1]+':']
                stack(l,p)
            elif 'hlt' in k:
                if len(k)!=1:
                    print("HAVE MORE than 1 label")
                    sys.exit()
                p='11010'+'0'*11
                stack(l,p)
                if lopi[j+1::]!=[]:
                    print("TRACED AN ERROR\nFOUND SOME COMMAND AFTER HALT INSTRUCTION")
                    sys.exit()
                break
            elif k[0]=='var':
                pass
            else:
                print("SYNTAX ERROR INSTRUCTION NAME HAS AN ERROR")
                sys.exit()
                break
        else:
            print("SYNTAX ERROR INSTRUCTION NAME HAS AN ERROR")
            sys.exit()
            break
        # aditya+=1
        # print(aditya)
        # print(l)
    except KeyError:
        if k[0]=='mov':
            if k[2].count('$')==0:
                print("either $ is missing of the register is not defined to hhold value")
                sys.exit()
        if k[1] not in dicttoholdval:
            print("Error: "+k[1]+" has some typo in it")
            fg=1
        elif k[0] in ['ld','st','jmp','je','jgt','je']:
            if k[1] not in dictregister:
                print(f"TYPO IN REGISTER NAME {k[1]} Or Label is not defined ")
                fg=1
            
            elif k[2] not in dicttoholdval:
                print(f'Either variable not defined or variable is greater than 127')
                fg=1
        else:
            if k[1] not in dictregister:
                print(f"TYPO IN REGISTER NAME {k[1]}")
                fg=1
            elif k[2] not in dictregister:
                print(f"TYPO IN REGISTER NAME {k[2]}")
                fg=1
            elif k[3] not in dictregister:
                print(f"TYPO IN REGISTER NAME {k[3]}")
                fg=1  
        if not(fg):
            print("SYNTAX ERROR IN NAMING THE COMMAND")      
        sys.exit()  
#file_assembler=open('Machine_code.txt','w')
for i in l:
    print(i)
