n=int(input())
e=0
o=0
a=list(map(int,input().split()))
for i in range(n):
    if(i==0 or i%2==0):
        e+=a[i]
    else:
        o+=a[i]
if(e==o):
    print("YES")
else:
    print("NO")