arr=list(map(int,input().split()))
ma=0
for i in range(len(arr)):
    for j in range(len(arr)):
        if(i!=j):
            pr=(arr[i]-1)*(arr[j]-1)
            if(ma<pr):
                ma=pr
print(ma)