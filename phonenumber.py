"""
Telephone converter
"""
letters = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

phone = str(input("Please enter an alphabetic telephone number:"))

converted = ''

for i in range(len(phone)):
    if phone[i].isalpha():
        for j in range(len(letters)):
            if phone[i] in letters[j]:
                converted += str(j + 2)
    else:
        converted += str(phone[i])    
print('The converted telephone number is ' + converted + '.')