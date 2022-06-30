n=int(input())
a=list(map(int,input().split()))
x=[]
s=0
for i in a:
    b=a.count(i)
    if b==i:
        x.append(i)
        s=1
        if b>1:
            a.remove(i)
if s==0:
    print("-1")
else:
    print(min(x),max(x))