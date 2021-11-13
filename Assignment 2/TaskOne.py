

#Task One
#How many QA pairs in QA_Pairs.txt? Here (q1, a1) is a pair, where q stands for question, and a for answer.
def getNumOfPairs():

    #accessing file
    text = open('QA_Pairs.txt', 'r')
    lines = text.readlines()

    pairs, numOfPairs, count, allLines,  = [], 0, 0, []

    for line in lines:  #assigning each line to a element in a list
        count += 1
        allLines.append((line.strip()))
    #print(len(allLines))
    for i in range(len(allLines)):  #going through line by line in the list
        if i < (len(allLines)-1):   #makes sure the index isnt out of range
            temp_One, temp_Two = allLines[i], allLines[i+1]
            if (temp_One[0]) == ('a' or 'A') and (temp_Two[0] == ('q' or 'Q')):
                pairs.append([temp_One, temp_Two])
                numOfPairs +=1
        else:
            numOfPairs+=1
            break
    #print(pairs[0][0])
    text.close()
    return (numOfPairs, pairs)





if __name__ == "__main__":
    answer = (getNumOfPairs())
    print(answer[0])
   