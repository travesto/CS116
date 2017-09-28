"""
File I/O: Line Numbers
Returns file with line numbers
"""
file_name = str(input("Enter a filename: "))
print('\nContents of', file_name)
with open(file_name) as file:
    x = 1
    for i in file:
        print(str(x) + ":\t" + str(i), end='')
        x += 1
file.close()