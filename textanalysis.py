"""
Text Analysis
Find #upper, lower, digit, and whitespace
"""
print('This program analyzes text. Enter text or enter "quit" to quit.')

upper = 0
lower = 0
digit = 0
white = 0

words = input('Please enter some text: ')

while words != 'quit':
    for u in words:
        if u.isupper():
            upper += 1
        elif u.islower():
            lower += 1
        elif u.isdigit():
            digit += 1
        elif u.isspace():
            white += 1
    
    words = input('Please enter some text: ')
  
print("There are " + str(upper) + " uppercase letters in this text.")
print("There are " + str(lower) + " lowercase letters in this text.")
print("There are " + str(digit) + " digits in this text.")
print("There are " + str(white) + " whitespace characters in this text.")
