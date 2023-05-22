#Accepting Sentence to be analysed 
sentence = input("Enter the sentence: ")

# Initializing variables to count letters and digits
letter = 0
digit = 0

# For loop to count through the sentence
for char in sentence:
    if char.isalpha():
        letter += 1
    elif char.isdigit():
        digit += 1

# Print Output
print("LETTERS: ", letter)
print("DIGITS: ", digit) 
