from turtle import goto


print("enter a color")
color1=input()
print("enter a second color")
color2=input()
colors=["red","blue","yellow"]
inputs=[color1,color2]
print("your result is:")
if (color1=="red" and color2=="blue") or (color1=="blue" and color2=="red"):
    print("Purple")
elif (color1=="red" and color2=="yellow") or (color1=="yellow" and color2=="red"):
    print("orange")
elif (color1=="blue" and color2=="yellow") or (color1=="yellow" and color2=="blue"):
    print("green")
elif (color1 == color2 =="red"):
    print("red")
elif (color1 == color2 == "blue"):
    print("blue")
elif (color1 == color2 == "yellow"):
    print("yellow")
elif  inputs not in colors:
    print("error")