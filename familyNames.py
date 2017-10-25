"""
Prints a bunch of names from a dict
"""
def main():
    with open('names.txt') as f:
        nameList = f.readlines()
    nameList = [x.strip("\n") for x in nameList]
    names = {nameList[i]: [nameList[i+1]] for i in range(0, len(nameList), 2)}
    
    print("This program determines which family is the largest, the smallest, and greets each of them.")
    
    lNames = list(names.keys())
    lNames.sort()
    lengths = [len(v) for v in names.values()]
    lengths.sort()
    print(nameList)
    # for i in names:
    #     print(names.get(i))

main()
