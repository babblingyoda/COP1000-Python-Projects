print("enter store profit from the past 5 days")
x=int(input())
y=int(input())
z=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
ls=[x,y,z,a,b,c,d]
print("stores profit this week is:")
print(sum(ls))
print("here are the lowest to highest sales:")
ls.sort()
print(ls)
e=sum(ls)
if e<100:
    print("work harder we are losing profits")
elif e>100 and e<500:
    print("profits are ok but need inprovment try to push more upsells")
elif e>500 and e<1000:
    print("keep up the great work")
elif e>1000:
    print("excellent work everyone gets a %10 raise")