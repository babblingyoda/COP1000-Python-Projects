import math


userinput = []
while True:
    imp = int(input("Enter a value: "))
    userinput.append(imp)
    if imp == 0:
        break
del userinput[-1]
print(userinput)
print (userinput)
def sums():
    total = sum(userinput)
    print (total)
print("the sum is:")
sums()
def products():
    total2 = math.prod(userinput)
    print (total2)
print ("the product is:")
products()
