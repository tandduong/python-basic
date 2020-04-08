numbers = [5, 2, 1, 7, 4, 5]

uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


# to check if the number is in the list,
# use print((the number we want to check) in numbers)

#Create the uniques list to add the number from the numbers list
#Number that already exist does not be added to uniques
#Use append method to add the number in the tail of the list
#make the for loop to go through the numbers' items.