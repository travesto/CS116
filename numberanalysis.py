"""
Number Analysis
Find lo, hi, count, and mean
"""
print('Please enter some numbers. Type \'q\' to quit.')

numlist = []
count = 0
total = 0

numbers = input('Enter a number: ')
hi = int(numbers)
lo = int(numbers)

while numbers != 'q':
    numlist.append(numbers) 
    count += 1

    if int(numbers) >= hi:
        hi = int(numbers)
    if int(numbers) <= lo:
        lo = int(numbers)
    total += int(numbers)
    numbers = input('Enter a number: ')
  
print('The lowest number is ' + str(lo))
print('The highest number is ' + str(hi))
print('The total of the numbers is ' + str(total))
av = "{:.2f}".format(total/count)
print('The average of the numbers is ' + str(av))