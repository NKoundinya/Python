n=input("Size:")
a=[input() for i in range(n)]
sum=0
min=sum
max=sum
for i in range(0,n):
    for j in range(0,n):
        sum+=a[j]
    sum=sum-a[i]
    if i==0:
        min=sum
        max=sum
    if sum<min:
        min=sum
    elif sum>max:
        max=sum
    sum=0
print min,max
