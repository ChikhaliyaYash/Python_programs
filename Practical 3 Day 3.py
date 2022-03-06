print("Welcome to rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0

# height > 130:(in this condition in another condition are set) like this <,>,<=,>=,==,!=
if height > 130:
    print("you can ride the rollercoaster!")
    age=int(input("What is your age?"))
    if age < 12:
        bill=5
        print("Please pay $5")
    elif age <= 18:
        bill=7
        print("Please pay $7")
    else:
        bill=12
        print("Please pay $12")

    want_photo = input(" Do you want a photo taken ? yes or no.")
    if want_photo =="yes":
        bill = bill + 3
#       bill +=3
    print(f"your final bill {bill}")

else:
    print("sorry, you can't ride the rollercoater.")