a=int(input())
b=list(map(int,input().split()))
count1=0
for i in b:
    c=b.count(i)
    if(i==c):
        count1+=1
        if(c>1):
            b.remove(i)
print(count1)