"""
Prints a bunch of names from a dict
"""
def main():
    names = {}
    fNames = []
    temp = []
    biggest = 0
    bigFam = ""
    smallest = 25000
    lilFam = ""
    salutation = ", "

    try:
        with open('names.txt') as f:
            nameList = f.readlines()
        nameList = [x.strip("\n") for x in nameList]
        for line in nameList:
            line = line.replace(",,", " GARBAGE ")
            if line[0] == ",":
                line = line.replace(",", " GARBAGE ", 1)
            
            line = line.replace(",", " ")
            line = line.split()
            temp.append(line)
        names = {nameList[i]: temp[i+1] for i in range(0, len(nameList), 2)}
        
        print("This program determines which family is the largest, the smallest, and greets each of them.\n")
        
        for key in names:
            if len(names[key]) > biggest:
                bigFam = key
                biggest = len(names[key])
            if len(names[key]) < smallest:
                lilFam = key
                smallest = len(names[key])
        
        print("The", bigFam, "family is the largest.")
        print("The", lilFam, "family is the smallest.\n")

        lNames = list(names.keys())
        lNames.sort()

        for key in sorted(names):
            fNames.append(names[key])
        
        for i in range(len(fNames)):
            print("Hello, ", end="")
            if fNames[i][0] == "GARBAGE":
                print("Mrs. ", end="")
            elif fNames[i][1] == "GARBAGE":
                print("Mr. ", end="")
            else:
                print("Mr. and Mrs. ", end="")
            
            del fNames[i][0]
            del fNames[i][0]

            print(lNames[i], end="")
            for j in range(len(fNames[i])):
                if j+1 == len(fNames[i]):
                    salutation += "and "
                salutation += str(fNames[i][j]) + ", "
            print(salutation[:-2] + ".") 
            salutation = ", " 

    except FileNotFoundError:
        print("Bad file.")
 
main()
