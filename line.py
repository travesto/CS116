"""
2D List Indexing
"""
lines = []
words = [[], []]

print('Enter a paragraph. Press enter between each line. Type q on a line by itself to quit.')
singleWords = ''

while singleWords != 'q':
    singleWords = input("").replace(',', ' ').replace('.', ' ').replace(';', ' ').replace('?', ' ').replace('!', '').replace(':', ' ').lower()
    lines.append(singleWords)
del lines[-1]

for m in range(len(lines)):
    for item in lines[m].split():
        if not item in words[0]:
            words[0].append(item)
            words[1].append('')
    for n in range(len(words[0])):
        if words[0][n] in lines[m].split():
            if words[1][n] == '':
                words[1][n] = str(m + 1)
            else:
                words[1][n] = words[1][n] + ', ' + str(m + 1)

print('')
print('The index for this paragraph is:')

sortList = list(words[0])
sortList.sort()
for word in sortList:
    print(word + ': ' + words[1][words[0].index(word)])