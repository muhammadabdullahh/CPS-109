from TaskOne import getPairs
def getAnswers():
    pairs = getPairs()
    text = open("Answers.txt", "w")
    for i in pairs:
        text.write(str(i[1]) + "\n")
    text.close()
