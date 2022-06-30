n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in a:
    b=a.count(i)
    if(b==k):
        print(i,end=' ')
        s=1
        if b>1:
            a.remove(i)
if s==0:
    print("-1")
    