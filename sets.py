""""
Sets -- reads course enrollment from file
"""
def main():
    courses = {}
    students = []
    mORe = []
    hANDm = []
    NOTp = []
    p = []

    file = input("Enter name of input file: ")
    try:
        f = open(file)
        for line in f:
            splitLine = line.split(',')
            splitLine = [x.strip("\n") for x in splitLine]
            
            if str(splitLine[0]) == 'Mathematics':
                courses["Mathematics"] = splitLine[1:]
            elif str(splitLine[0]) == 'English':
                courses["English"] = splitLine[1:]
            elif str(splitLine[0]) == 'Programming':
                courses["Programming"] = splitLine[1:]
            else:
                courses["History"] = splitLine[1:]
    
    except FileNotFoundError:
        print("Bad file.")
    
    # all students
    for key in courses:
        stud = courses[key]
        for i in stud:
            if int(i) not in students:
                students.append(i)
                students = list(map(int, students))
                students.sort()
    if str(students) == "[]":
        print("\nStudents at the University:")
    else:
        print("\nStudents at the University:", str(students).replace("[","").replace("]","").replace("'",""))

    # Math or English
    try:
        for i in courses["Mathematics"]:
            mORe.append(i)
            mORe = list(map(int, mORe))
            mORe.sort()
        for i in courses["English"]:
            if int(i) not in mORe:
                mORe.append(i)
                mORe = list(map(int, mORe))
                mORe.sort()
    except KeyError:
        pass
    if str(mORe) == '[]':
        print("Students taking Mathematics or English:")
    else:
        print("Students taking Mathematics or English:", str(mORe).replace("[","").replace("]","").replace("'",""))

    # History and Maths
    try:
        for i in courses["History"]:
            for j in courses["Mathematics"]:
                if i == j:
                    hANDm.append(i)
                    hANDm = list(map(int, hANDm))
                    hANDm.sort()
    except KeyError:
        pass
    if str(hANDm) == "[]":
        print("Students taking History and Mathematics:") 
    else:
        print("Students taking History and Mathematics:", str(hANDm).replace("[","").replace("]","").replace("'",""))

    # Not Programming
    try:
        for i in courses["Programming"]:
            p.append(i)
            p = list(map(int, p))
            p.sort()
        NOTp = list(set(students) - set(p))
        NOTp.sort()
    except KeyError:
        pass
    print("Students not taking Programming: " + str(NOTp).replace("[","").replace("]","").replace("'",""))

main()
    