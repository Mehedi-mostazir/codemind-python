def prime(a):
    if a==1:
        return False
    for i in range(2,int(a**0.5)+1):
        if(a%i==0):
            return False
    return True
    


l=int(input())
h=int(input())
count=0
while l<=h:
    if prime(l):
        count+=1
    l+=1
print(count)