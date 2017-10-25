"""
Dictionary indexing :/
"""
def main():
    index = {}
    lines = []
    sortedIndex = []

    print("Enter a paragraph. Press enter between each line. Type q on a line by itself to quit.")

    singleWords = ''
    while singleWords != 'q':
        singleWords = input("").replace(',', ' ').replace('.', '').replace(';', ' ').replace('?', ' ').replace('!', '').replace(':', ' ').lower()
        lines.append(singleWords.split())
    del lines[-1]

    lineCount = []
    lineNums = 0

    #lines 
    for i in lines: 
        lineNums += 1
    
        #words 
        for j in i:
            if j in index:
                temp = index[j]
                updatedList = temp
                if lineNums not in updatedList:
                    updatedList.append(lineNums)
                #get the values from the key, add this line then update 
                index[j] = updatedList
            else:
                index[j] = [lineNums] 
    
    for key, value in index.items():
        temp = [key,value]
        sortedIndex.append(temp)
    sortedIndex.sort()
    
    print("\nThe index for this paragraph is:")
    for key in sortedIndex:
        print(key[0], ": ", str(index.get(str(key[0]))).replace(']','').replace('[',''), sep='')

main()