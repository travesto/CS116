"""
Jury Summons 1 of 3
Read file and return true if line num = x
"""
print("This program divides a group of people into jury pools.")

file = str(input("Enter a file name: "))
numLines = int(input("Enter a number: "))

def verify_file(fileName, number):
    
    try:
        f = open(file)
        contents = f.read()
        fileList = contents.split('\n')
        if len(fileList) >= numLines and len(fileList) > 0:
            return True
        else:
            return False
    except IOError:
        return False

flag = verify_file(file, numLines)
if flag == True:
    print("File is OK.")
else:
    print("There was a problem with the file:", file)