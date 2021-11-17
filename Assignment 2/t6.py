import re
def getFrequency():
    text = open("unique_QA_Pairs.txt", "r")
    freq = open("Frequency.txt", "w")
    lines = text.read()

    #uses import re
    temp_All_Words = re.split(' |\n', lines) #seperating each word into a sperate elment in a list
    temp_All_Words.sort() #sorting the list to make the searching more efficient
    all_Words = []

    #This loop removes all of the questions marks and elements with nothing in them
    #and creates a new list with only valid words
    for i in range(len(temp_All_Words)):
        temp =  (str(temp_All_Words[i])).lower()
        newTemp = ''.join(filter(str.isalnum, temp))    #this line removes all special chars froma str
        all_Words.append(newTemp)
     
    words_Used = [] #creating an array to add words that we have already counted
    list_Of_Words = []
    list_Of_Counts = []

    #first loop will be used to go through each word
    #the if statement looks if that word has already been used
    #the second loop searched through all of the words to see how many times it appears
    for i in range(len(all_Words)):
        count = 0
        if all_Words[i] not in words_Used:
            count = all_Words.count(all_Words[i])
            words_Used.append(all_Words[i]) 
            list_Of_Counts.append(count)  #adding the word and its count into a list
            list_Of_Words.append(all_Words[i]) #adding current elem to words used
    #writing all words and their counts into Frequency.txt
    for i in range(len(list_Of_Counts)):
        freq.write(list_Of_Words[i] + ', ')
        freq.write(str(list_Of_Counts[i]) + '\n')
    text.close()
    freq.close()
    return(list_Of_Words, list_Of_Counts)
