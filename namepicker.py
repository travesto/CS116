"""
Name Generator
"""

fList = []
mList = []
lList = []
x = 0

fname = input("Enter some first names. Enter \"quit\" to quit.\n")
while fname != 'quit':
    fList.append(fname)
    fList.sort()
    fname = input("")

mname = input("Enter some middle names. Enter \"quit\" to quit.\n")
while mname != 'quit':
    mList.append(mname)
    mList.sort()
    mname = input("")

lname = input("Enter some last names. Enter \"quit\" to quit.\n")
while lname != 'quit':
    lList.append(lname)
    lList.sort()
    lname = input("")
      
print("Full name\t\tInitials\n--------------------------------")

while len(fList) != 0 and len(mList) != 0 and len(lList) != 0:
    acro = str(fList[0][0]).upper() + str(mList[0][0]).upper() + str(lList[0][0]).upper()
    print(str(fList.pop(x)) + " " + str(mList.pop(x)) + " " + str(lList.pop(x)) + "\t" + acro)

if len(fList) != 0:
    print("\nLeftover first names:")
    while len(fList) != 0:
        print(str(fList.pop(x)))
if len(mList) != 0:
    print("\nLeftover middle names:")
    while len(mList) != 0:
        print(str(mList.pop(x)))
if len(lList) != 0:
    print("\nLeftover last names:")
    while len(lList) != 0:
        print(str(lList.pop(0)))