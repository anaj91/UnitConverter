#UnitConerter

print("Welcome to my converter. It is used to convert kilometers into miles. Let\'s start.")

Start_again = 0

while True:
    Kilometers = int(input("Please, enter number of kilometers you would like to convert:"))
    Miles = Kilometers/1.609
    print(str(Kilometers) + " km is", str(round(Miles,2)), "miles.")
    Start_again = input("Would you like to start again? (y/n)")
    if Start_again != "y" and Start_again != "yes":
        break