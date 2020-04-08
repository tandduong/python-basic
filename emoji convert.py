def emojis_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "🙂",
        ":(": "😞",
        ":D": "😀",
        ":3": "😗"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")

print(emojis_converter(message))


#split method will split each word in the input into a list
#where each word as a single item
#In the program above, we need to braek down each word from the input
#The split will go through string and break down word from the space as the set boundary
#for each seperated word in "words" list, emojis will transplate those word matches with the input
#for those does not match, return as default "word" parameter
#set the empty output, put it to the loop and print the final output