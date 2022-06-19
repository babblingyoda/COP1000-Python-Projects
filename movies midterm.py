movie = input ("enter current hollywood movie guide movie: ")
ratings = []
userinput = []
def average():
    print(sum (ratings) / len (ratings))
def ratingprog():
    while True:
        rating = float(input("enter a value between 0 and 4 to rate this movie: "))
        if (rating >=0 and rating <=4):
            ratings.append(rating)
            print("thank you")
        elif rating < 0:
            print ("program terminated")
            print ("the whole ratings for",movie,":")
            print (ratings)
            print ("the rating average for",movie,"is:")
            average()
            break
        elif rating >= 5:
            userinput.append(rating)
            print("try again \nremember to enter a number between 0 and 4")
            userprog()
def userprog():
    if len(userinput) == 3:
        print("you have entered incorrect input three times please move away for next customer")
        print (userinput)
        userinput.clear()
        return ratingprog()
    else:
        return ratingprog()
ratingprog()