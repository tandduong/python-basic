phone = input("Phone: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!") + " "
print(output)

#each key must be unique. Duplicate keys are prohibited
#value can be anything: string, int, bool, list,...

#For the program above, the loop get the key in dictionaries
#The "!" is default output key if the input number does not match in the dictionary