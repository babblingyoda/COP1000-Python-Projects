import datetime

sale_total=[]
hpd= int(1000)
def name():
    name = input()
    classname = input()
    date = datetime.datetime.now()
    print (classname, classname, date)
def id():
    while True:
        ID= input("enter ID ")
        try:
            ID = int(ID)
            break
        except ValueError:
            print("try again")
            pass
def sold():
    while True:
        itsold = int(input("Enter Total Sales: /n"))
        sale_total.append(itsold)
        if itsold == 0:
            break
        print(sale_total)
def totalsold():
    totalitems = int(input())
    return totalitems
def higperf():
        print(sum(sale_total))
        if finalgty >= 200 or sum(sale_total) >= hpd:
            print("your a high performer")
        else:
            print("work harder")
name()
id()
sold()
finalgty = totalsold()
higperf()
        
