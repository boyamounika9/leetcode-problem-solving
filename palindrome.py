x=int(input())
temp=x
reverse=0
if x<0:
    print("false")
while x!=0:
    digit=x%10
    reverse=reverse*10+digit
    x//=10
if temp==reverse:
    print("true")
else:
    print("false")
