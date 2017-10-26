"""
Provides stats on exam results
"""
def main():
    correctAnswers = {1:'B',2:'D',3:'A',4:'A',5:'C',6:'A',7:'B',8:'A',9:'C',10:'D',11:'B',12:'C',13:'D',14:'A',15:'D',16:'C',17:'C',18:'B',19:'D',20:'A'}
    testAnswers = {}
    counter = 1
    listCorrect = []
    numCorrect = 0
    listWrong = []
    numWrong = 0

    file = input("Enter a filename: ")
    try:
        with open(file) as f:
            answers = f.readlines()
            answers = [x.strip("\n") for x in answers]
            testAnswers = {i+1: answers[i] for i in range(0, len(answers))}
        print("\nContents of",file)
        for key in testAnswers:
                print(key, ": ", testAnswers[key], sep='')
                if testAnswers[key] == correctAnswers[key]:
                    listCorrect.append(key)
                    numCorrect += 1
                else:
                    listWrong.append(key)
                    numWrong += 1
        
        
        print("Total correctly answered questions:", numCorrect)
        print("Questions that were answered correctly:", str(listCorrect).replace("[","").replace("]","").replace(" ", ""))
        print("Total incorrectly answered questions:", numWrong)
        print("Questions that were answered incorrectly:", str(listWrong).replace("[","").replace("]","").replace(" ", ""))
        
        if numCorrect >= 15:
            print("This exam receives a passing score.")
        else:
            print("This exam receives a failing score.")
    except FileNotFoundError:
        print("Bad file.")
    
main()