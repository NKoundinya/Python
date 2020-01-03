n=input("Range: ")
array=[[0 for i in range(n)] for i in range(n)]
print array
for i in range(0,n):
    for j in range(0,n):
        array[i][j]=input()
for i in range(0,n):
    for j in range(0,n):
         array[j][i]
