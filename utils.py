def find_max(list):
    maximum = list[0]
    for i in list:
        if i > maximum:
            maximum = i
    return maximum

#First set the maximum number is the first number in the list
#For all index i in the list, if any number greatewr than max
#Then reset it as the maximum number
#Print the final result as the largest number in the list