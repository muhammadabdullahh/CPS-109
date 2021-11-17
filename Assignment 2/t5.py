from t1 import getPairs
def getAnswers():
    '''creates a text file with all answers'''
    pairs = getPairs()
    text = open("Answers.txt", "w")
    for i in pairs:
        text.write(str(i[1]) + "\n")
    text.close()
