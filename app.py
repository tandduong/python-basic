weight = input("Weight: ")
choice = input("(L)bs or (K)g?: ")

if choice == "L" or choice == "l":
    weight = int(weight) * 0.454
    print(f"Your weight in kg is: {weight} kg")
elif choice == "K" or choice == "k":
    weight = int(weight) * 2.2046
    print(f"Your weight in lbs is: {weight} lbs")
else:
    print("Error.")
print("End of program")