"""
Average words
"""

line = []
total = 0
count = 0

print('Please enter some sentences. Type \'quit\' on a line by itself to quit.')
words = input('')

while words != 'quit':
    w = words.split()

    total += len(w)
    count += 1

    words = input('')

av = "{:.2f}".format(total/count)
print('These sentences have an average of ' + str(av) + " words.")