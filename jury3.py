"""
Jury Summons 3 of 3
Read file and do stuff
"""
def verify_mwj(message,maximum):
    blerg = input(message)
    while True:
        try:
            float(blerg)
            while float(blerg) not in range(1, maximum+1):
                print("You must enter a number in the range [1, " + str(maximum) + "].")
                blerg = input(message)
            break
        except ValueError:
            print("You must enter an integer value.")
            blerg = input(message)
    return int(blerg)

def verify_file(filename,number):
    try:
        f = open(filename)
        contents = f.read()
        fileList = contents.split('\n')
        if len(fileList) >= number and len(fileList) > 0:
            return True
        else:
            return False
    except FileNotFoundError:
        return False

def main():
    months = ['','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    numPos = ['','1st', '2nd', '3rd', '4th']
    jurypools = []
    number_of_months = 12
    number_of_weeks = 4
    number_of_jurors = 480
    continueInput = ''

    print("This program divides a group of people into jury pools.")
    file = str(input("Enter a file name: "))

    #check months
    monthInput = verify_mwj("Enter the number of months: ", number_of_months)
    number_of_months = monthInput

    #check weeks
    weekInput = verify_mwj("Enter the number of weeks: ", number_of_weeks)
    number_of_weeks = weekInput

    #set juror numb
    number_of_jurors = 480/(int(number_of_months)*int(number_of_weeks))

    #check jurors
    jurorInput = verify_mwj("Enter the number of people in each jury pool: ", int(number_of_jurors))
    number_of_jurors = jurorInput

    #test file and print info
    flag = verify_file(file, number_of_jurors)
    if flag == False:
        print("There was a problem with the file:", file)
        quit()
    else:
        f = open(file)
        #put names in list
        for i in range(0,number_of_months):
            jurypools.append([])
            for j in range(0,number_of_weeks):
                jurypools[i].append([])
                for k in range(0,number_of_jurors):
                    jurypools[i][j].append(f.readline().rstrip('\n'))

        print('\nEnter a month, week, and juror number to select a juror.')
        
        while continueInput.upper() != 'N':
            monthInput = verify_mwj("Select a month: ", number_of_months)
            weekInput = verify_mwj("Select a week: ", number_of_weeks)
            jurado = verify_mwj("Select a juror number: ", int(number_of_jurors))
            print("Juror #" + str(jurado) + " for the " + str(numPos[weekInput]) + " week of " + str(months[monthInput]) + " is " + str(jurypools[monthInput-1][weekInput-1][jurado-1]) + "." )
            continueInput = input("\nWould you like to find another juror? (y/n) ")
            while continueInput.upper() != 'Y':
                if continueInput.upper() != 'N':
                    print("Invalid input.")
                    continueInput = input("\nWould you like to find another juror? (y/n) ")
                else:
                    break;

main()