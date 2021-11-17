
from t1 import getPairs
def getOverlap():
    '''creates and returns an overlap text file containing all overlapping
    questions and answers'''
    pairs = getPairs()
    text = open("Overlapping.txt", "w")
    
    #using the old questions and answers and creating newer ones 
    #which will store all overlapping answers questions
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
    #wrtites into the text file "Overlapping.txt"
    for i in range(len(overLapAnswers)):
        text.write(overLapAnswers[i] + "\n")
        text.write(overLapQuestions[i] + "\n")

    text.close()
    return newList
        
def getUnique():
    '''creates and returns a uniqie text file containing all unique
    questions and answers'''
    pairs = getPairs()
    text = open("unique_QA_Pairs.txt", "w")
    
    questions = []
    answers = []
    newList = []
    #this loop checks if question or answer is already in newList, if not then it adds it to newList
    #keeps doing for all pairs of questions and answers
    for i in range(len(pairs)):
        if (pairs[i][0] not in questions) and (pairs[i][1] not in answers):
            questions.append(pairs[i][0])
            answers.append(pairs[i][1])
            newList.append(pairs[i])
    for i in range(len(answers)):   #finally writes the questions and answers into te text file
        text.write(answers[i]+"\n")
        text.write(questions[i]+"\n")

    text.close()
    return newList

    