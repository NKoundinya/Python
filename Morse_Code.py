str=raw_input("Enter Str: ")
new=[".",".",".",".",".","_","_","_","_","_"]
numbers="0123456789"
newnumbers=""
encrypt=input("E (to Encrypt) = ")
for i in range(encrypt,len(numbers)):
    newnumbers+=numbers[i]
for j in range(0,encrypt):
    newnumbers+=numbers[j]
def morse(numbers,str,new):
    for i in range(0,len(str)):
        
        for j in range(0,len(numbers)):
            if numbers[j]==str[i]:
                if j==5:
                    print new[0:5]

                elif j==0:
                    print new[5:10]
                elif j<5:
                    print new[0:j],new[5+(j-1):9]
                else:
                    print new[5:j],new[0:10-j]
morse(newnumbers,str,new)
print "\n"
if(raw_input("Decrypt[Y/N]? : ")=='y'):
    morse(numbers,str,new)
code=raw_input("Enter code: ")
def read_code(dup):
    c=0
    k=0
    for i in range(0,len(dup)):
        if(i<len(dup)):
            if code[i]==" ":
                break
            elif dup[0]==new[0]:
                if dup[i]==new[0]:
                    c+=1
            else:
                if dup[i]==new[8]:
                    k+=1
    if k>0 and k!=5:
        print numbers[k+5]
    else:
        print numbers[c]
for i in range(0,len(code),6):
    read_code(code[i:i+5])
