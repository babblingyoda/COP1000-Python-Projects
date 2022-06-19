number=[]
def main():
    while True:
        num=int(input("enter 5 numbers"))
        number.append(num)
        if len(number) == 5:
            print(sum(number))
            break
main()

mystring = "i am studying computer programming"
x = mystring.capitalize()
print (x)
x = mystring.casefold()
print (x)
x = mystring.title()
print (x)
print(mystring.count('m'))

dogs = ["shishu", "golden retreiver", "yorkie", "bulldog","pug"]
print (len(dogs))

        