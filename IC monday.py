##speed code
print("enter first recorded speed of vehicle:")
x=int(input())
y=int(20)
if x>100:
    z=int(40)
print("enter second recorded speed of vehicle:")
a=int(input())
b=int(0)
if a<10:
    c=int(1)
speed=x+a
if speed>55 and speed<70:
    print("speed is normal")
else:
    (print("Not Going the Speed Limit"))
speedlist=[x,a]
print("the max speed is:")
if x>10 and a<100:
    print(max(speedlist))
else:
    print("not avalable")
##test score code
print("enter students test score:")
testscore=int(input())
print("enter students class rank:")
classrank=int(input())
if testscore>=90 and classrank<=25:
    print("Accepted")
elif testscore>=80 and classrank>=50:
    print("Accepted")
else:
    print("rejected")