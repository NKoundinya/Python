s="I"
d="V"
t="X"
f="L"
e="C"
n="D"
t="M"
el="K"
n=input("NUMBER:")
def digits(k):
    l=0
    while k>0:
        k/=10
        l+=1
    return l
print digits(n)
