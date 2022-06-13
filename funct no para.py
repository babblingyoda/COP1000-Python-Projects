def discount():
    print ("you are preregistered and qualify for a 5% discount")
def nodiscount():
    print ("Sorry, you did not preregister and do not quatify for a 5% discount")
print("Did you preregister")
acceptedanswers=["y","n"]
while True:
    x= input("Enter y or n: ")
    if x in acceptedanswers:
        break
    print("not accepted try again")
if x == "y":
    discount()
if x == "n":
    nodiscount()
