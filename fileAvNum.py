"""
File IO Average Numbers
"""
print("This program averages numbers inside a given file.")
file = str(input("Enter a filename: "))
while file != 'quit':
    f = open(file)
    nums = f.read().strip().split('\n')
    total = 0
    for i in nums:
        total += int(i)
    print("The average is " + "{:.2f}".format(total/len(nums)))
    file = str(input("Enter a filename: ")) 
