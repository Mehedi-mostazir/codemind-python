n=int(input())
for l in range(n):
    a=int(input())
    arr=list(map(int,input().split()))
    m=1
    while(True):
        f=0
        for i in range(a-1):
            if arr[i]==m:
                f=0
                break
            else:
                f=1
        if f==1:
            break
        else:
            m+=1
    print(m)