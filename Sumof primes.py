c=0
i=input()
for j in range(1,i+1):
    for k in range(1,j+1):
        if j%k==0:
            c+=1
        if c==2:
            print j
    c=0
        #sum=sum+i
#print sum
