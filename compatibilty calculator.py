print("enter the amounts you deposited in you bank account in the past two weeks")
print("enter first number")
x=int(input())
print("enter second number")
y=int(input())
print("your answer is:")
print(x+y)
x=(x+y)
if y<200:
    print("your cool")
elif y>200 and y<500:
    print("your ok")
elif y>500:
    print("get your ass outta here")