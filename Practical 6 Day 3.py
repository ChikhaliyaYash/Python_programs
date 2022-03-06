print("Welcome to rollercoaster!")
height=int(input("What is your height in cm? "))
bill=0

if height > 130:
    print("you can ride the rollercoaster!")
    age=int(input("What is your age?"))
    if age < 12:
        bill=5
        print("Child tickets : $5")
    elif age <= 18:
        bill=7
        print("Youth tickets :$7")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill=12
        print("Adult tickets:$12")

    # multiple if condition
    want_photo = input(" Do you want a photo taken ? yes or no.")
    if want_photo =="yes":
        bill = bill + 3
    #   bill +=3
    print(f"your final bill {bill}")

else:
    print("sorry, you can't ride the rollercoater.")