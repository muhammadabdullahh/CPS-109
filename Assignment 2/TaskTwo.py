
from TaskOne import getPairs
def getOverlap():
    pairs = getPairs()
    text = open("Overlapping.txt", "w")
    
    questions = []
    answers = []
    overLapQuestions = []
    overLapAnswers = []
    newList = []
    for i in range(len(pairs)):
        if (pairs[i][0] not in questions) and (pairs[i][1] not in answers):
            questions.append(pairs[i][0])
            answers.append(pairs[i][1])
    
        else:
            overLapQuestions.append(pairs[i][0])
            overLapAnswers.append(pairs[i][1])
            newList.append(pairs[i])
    for i in range(len(overLapAnswers)):
        text.write(overLapAnswers[i] + "\n")
        text.write(overLapQuestions[i] + "\n")

    text.close()
    return newList
        
def getUnique():
    pairs = getPairs()
    text = open("unique_QA_Pairs.txt", "w")
    
    questions = []
    answers = []
    newList = []
    for i in range(len(pairs)):
        if (pairs[i][0] not in questions) and (pairs[i][1] not in answers):
            questions.append(pairs[i][0])
            answers.append(pairs[i][1])
            newList.append(pairs[i])
    for i in range(len(answers)):
        text.write(answers[i]+"\n")
        text.write(questions[i]+"\n")

    text.close()
    return newList

    