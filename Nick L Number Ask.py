print("enter your name")
name = input()
print("enter a number")
x = int(input())
if x > 10:
    print(("You win ") + name)
elif x<=10:
    print(("You Lose ")+name)