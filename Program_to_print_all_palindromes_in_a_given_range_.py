def pal(a):
    temp=a
    sum=0
    while temp:
        sum=sum*10+temp%10
        temp//=10
    if(sum==a):
        print(sum,end=" ")
        

l=int(input())
h=int(input())

while l<=h:
    pal(l)
    l+=1