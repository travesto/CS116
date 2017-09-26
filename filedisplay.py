"""
File I/O: File Display
Returns numbers from a file
"""
file_name = 'numbers.txt'
print('This program displays numbers read from a file.')
with open('numbers.txt') as file:
    for i in file:
        print("Number:", int(i))
file.close()