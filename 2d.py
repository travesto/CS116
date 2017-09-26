"""
2D list (n x n)
"""
print("This program uses a two dimensional list.\nPlease enter the numbers in your list. To quit type \"quit\".")

firsts = []
num = input("")

while num != 'quit':
    firsts.append([int(num)])
    num = input("")

inc = input("Please enter the value by which you wish to increment: ")

for p in range(len(firsts)):
    for q in range(len(firsts) - 1):
        firsts[p].append(firsts[p][q] + int(inc))

print("")
for z in range(len(firsts)):
    print(*firsts[z], sep=' ')