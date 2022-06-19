food=[]
def addtolist(food):
    myfood= input()
    food.append(myfood)
def printlist(food):
    print (food)
def removefromlist(food):
    rmfood = input()
    food.remove(rmfood)
def mylist():
    while True:
        print ("enter command")
        command = input()
        if command == "remove":
            print ("enter item to remove")
            removefromlist(food)
        elif command == "done":
            break
        elif command == "add":
            print ("enter item to add")
            addtolist(food)
        elif command == "print":
            printlist(food)
mylist()

