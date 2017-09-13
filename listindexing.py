"""
2D List Indexing
"""
words = [[], []]
lines = []

print("Enter a paragraph. Press enter between each line. Type q on a line by itself to quit.")

user = ""

while user != 'q':
    user = input("")
    lines.append(user)
# print(lines)
# for x in range(len(lines) -1):
#     curline = lines[x].split()
#     for y in range(len(curline)):
#         print(len(words[0]))
#         if curline[y] == words[0]:
#             for x in range(len(words[0])):
#                 if curline[y] == words[0][z]:
#                     words[1][z] == words[1][z] + 1
#         else:
#             words[0].append(curline[y])
#             words[1].append(y)
# print(words)  


for x in range(len(lines) - 1):
    curline = lines[x].split()
    print(curline)

    for y in range(len(curline)):

        for z in range(len(words[0])):
            if curline[y] in words[0]:
                if curline[y] in words[0][z]:
                    print("Dup")
                else:
                    words[0].append(curline[y])
                    words[1][y].append(1)
    
    # singleWords = words.split()
    
#     for index,q in enumerate(singleWords):
#         if not q.isalpha():
#             q = q[:-1]
#         if not any(q in i for i in wordList):
#             wordList.append([q,1])
#         else:
#             print("already in list")
#             print(index)
#             wordList[index][1] += 1

    # words = input("")
# print(wordList)

