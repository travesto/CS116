"""
2D List Indexing
"""
wordList = []
print("Enter a paragraph. Press enter between each line. Type q on a line by itself to quit.")

words = input("")
while words != 'q':
    singleWords = words.split()
    
    for q in singleWords:
        c = 0 #subindex
        if not q.isalpha():
            q = q[:-1]
        if not (q in i for i in wordList):
            wordList[c][0] = q
            wordList[c][1] = 1
        else:
            print("2nd")
            wordList[c][1] = 1

    words = input("")
print(wordList)