from t1 import getPairs
def getQuestions():
    '''creates a text file with all questions'''
    pairs = getPairs()
    text = open("Questions.txt", "w")
    for i in pairs:
        text.write(str(i[0]) + "\n")
    text.close()


    

