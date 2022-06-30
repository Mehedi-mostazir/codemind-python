n=int(input())
a=list(map(int,input().split()))
sum=0
n=0
s=0
for i in a:
    b=a.count(i)
    if b==i:
        sum=sum+i
        n+=1
        s=1
        if b>1:
            a.remove(i)
if s==0:
    print("-1")
else:
    avg=sum/n
    print("%.2f"%avg)