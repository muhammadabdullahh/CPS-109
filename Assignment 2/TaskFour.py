from TaskOne import getPairs
def getQuestions():
    pairs = getPairs()
    text = open("Questions.txt", "w")
    for i in pairs:
        text.write(str(i[0]) + "\n")
    text.close()


    

