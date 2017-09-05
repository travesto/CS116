"""
Date converter 
"""
months = ['January', 'February', '"March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print('This program converts dates.')
date = input('Please enter a date in the form mm/dd/yyyy: ')

if (date[0] == '0'):
    if (date[3] == '0'):
        converted = str(months[(int(date[1:2]))-1] + " " + date[4:5] + ", " + date[6:])
    else:
        converted = str(months[(int(date[1:2]))-1] + " " + date[3:5] + ", " + date[6:])
else:
    if (date[3] == '0'):
        converted = str(months[int(date[1])-3] + " " + date[4:5] + ", " + date[6:]) 
    else:
        converted = str(months[int(date[1])-3] + " " + date[3:5] + ", " + date[6:])

print('The converted date is ' + converted + '.')
