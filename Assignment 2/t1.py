#Task One
#How many QA pairs in QA_Pairs.txt? Here (q1, a1) is a pair, where q stands for question, and a for answer.
def getNumOfPairs():
    '''returns the number of pairs in the text file'''
    #accessing file
    text = open('Smaller_Pairs.txt', 'r')
    #text = open('QA_Pairs.txt', 'r')
    lines = text.read()
    content_list = lines.split('\n')

    text.close()
    return int((len(content_list)-1)/2)

def getPairs():
    '''returns all of the questions and answers in pairs'''
    text = open('Smaller_Pairs.txt', 'r')
    #text = open('QA_Pairs.txt', 'r')
    lines = text.read()
    content_list = lines.split('\n')    #splitting each line

    #creating an answers and questions array which will store
    #all questions, and answers along with the 2d pairs list which will store both questions and answers
    #and will later be returned which will help in future tasks
    answers = []
    questions = []
    pairs = [[]]
    #this loop identifies all questions and answers
    for i in range(len(content_list)-1):   
        temp = str(content_list[i])
        if (temp[0] == 'q') or (temp[0] == 'Q'):
            questions.append(temp)
        else:
            answers.append(temp)
    for i in range(getNumOfPairs()):
        pairs.append([questions[i],answers[i]]) #adds questions and answers to pairs 2d list

    pairs.pop(0)
    text.close()
    return pairs
