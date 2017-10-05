"""
File IO Exception Handling
"""
print("This program averages numbers inside a given file.")

file = str(input("Enter a filename: "))

while file != "quit":
    
    try:
        f = open(file)
        nums = f.read().strip().split('\n')
        test = ''.join(str(e) for e in nums)
        if test.isdigit():
            total = 0
            for i in nums:
                total += int(i)
            print("The average is " + "{:.2f}".format(total/len(nums))) 
        else:
            raise ValueError('Not all numbers')
    except IOError:
        otravez = str(input("Error reading from the file. Try again? (y/n): "))
        if otravez == 'n':
            break
    except ValueError:
        otravez = str(input("The file does not have proper numbers. Try again? (y/n): "))
        if otravez == 'n':
            break
        
    file = str(input("Enter a filename: "))