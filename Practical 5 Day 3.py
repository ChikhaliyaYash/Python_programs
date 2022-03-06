year = int(input("Which year do you want to check? "))

# https://www.youtube.com/watch?v=xX96xng7sAE (this video explain leap year)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year")