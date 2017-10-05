"""
File, File, File
Read file of files
"""
print("This program prints the contents of files listed in a file.")

file = str(input("Enter the file: "))

while file != "quit":
    
    try:
        f = open(file)
        contents = f.read()
        fileList = contents.split("\n")
        if len(fileList) < 2:
            print(len(fileList), "file found:")
        else:
            print(len(fileList), "files found:")
        for i in fileList:
            print("\t" + i)
        for p in fileList:
            try:
                innerFile = open(p)
                innerContents = innerFile.read()
                print("\nContents of " + p + ":\n")
                print(innerContents + "\n\n------------------------------")
            except IOError:
                print("\n" + p + " does not exist or is an invalid file.\n\n------------------------------")
        break;
    except IOError:
        print("No files found.")
        break;