a=int(input())
arr1=list(map(int,input().split()))
b=int(input())
arr2=list(map(int,input().split()))
f=0
for i in arr1:
    if i in arr2:
        f=1
    else:
        f=0
        break
if f==1:
    print("True")
else:
    print("False")