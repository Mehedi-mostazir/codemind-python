a=int(input())
arr=list(map(int,input().split()))
x=arr[0]
i=1
while i<a:
    if(arr[i]%x==0):
        i+=1
    else:
        x=arr[i]%x
print(x)