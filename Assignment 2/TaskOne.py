#Task One
#How many QA pairs in QA_Pairs.txt? Here (q1, a1) is a pair, where q stands for question, and a for answer.
def getNumOfPairs():

    #accessing file
    text = open('QA_Pairs.txt', 'r')
    lines = text.read()
    content_list = lines.split('\n')

    text.close()
    return int((len(content_list)-1)/2)

def getPairs():
    text = open('QA_Pairs.txt', 'r')
    lines = text.read()
    content_list = lines.split('\n')

    answers = []
    questions = []
    pairs = [[]]
    for i in range(len(content_list)-1):
        temp = str(content_list[i])
        if temp[0] == 'q':
            questions.append(temp)
        else:
            answers.append(temp)
    for i in range(getNumOfPairs()):
        pairs.append([questions[i],answers[i]])

    pairs.pop(0)
    text.close()
    return pairs
