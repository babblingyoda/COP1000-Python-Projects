#print name code
print("enter your name:")
name=input()
print("Nice to meet you",name)
#sales tax code
print("enter sales tax rate")
taxrate=float(input())
print("enter price of item")
item=float(input())
itemtax=item/taxrate
print("tax amount for item")
print(itemtax)
total=item+itemtax
print("total for item with tax:")
print(total)
#batting code
hits=0
atBat=0
battingAverage=0
print("enter the plater's number of hits:")
hits=int(input())
print("enter how many times player was at bat:")
atBat=int(input())
battingAverage=hits/atBat
print("amount of hits:",hits)
print("amount of at bat's:",atBat)
print("batting average:",battingAverage)
