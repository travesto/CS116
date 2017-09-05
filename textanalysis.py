"""
Text Analysis
Find #upper, lower, digit, and whitespace
"""
print('This program analyzes text. Enter text or enter "quit" to quit.')

wordlist = []
upper = 0
lower = 0
digit = 0
white = 0

words = input('Please enter some text: ')

while words != 'quit':
    wordlist.append(words)

    words = input('Please enter some text: ')
  
print(wordlist)