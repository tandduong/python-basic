f = [5, 2, 5, 2, 2]

for item in f:
    output = ''
    for count in range(item):
        output += 'x'
    print(output)

#The program first take the item in f, set this to empty string
#Then, for the count in each item, set the string to x
#Make a loop for the x by adding it to output
#Print the x and finish the first item
#For the second item, reset the output to empty string
#Do the same step for the rest of items in f