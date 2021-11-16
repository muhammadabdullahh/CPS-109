from TaskSix import getFrequency
def getDecFrequency():

    text = open("Decreasing_Frequency.txt", "w")
    #calling un sorted frequencies
    #count and word are alligned with eachother per index
    result = getFrequency()
    all_Counts  = result[1]
    all_Words = result[0]

    #creating new arrays for count and words which will
    #be filled up with sorted counts and words
    new_Counts = []
    new_Words = []
    #loop to sort counts and words in dec order
    while all_Counts:
        minimum_Count = all_Counts[0]  # arbitrary number in list 
        minimum_Word = all_Words[0]
        for x in range(len(all_Counts)): 
            if all_Counts[x] > minimum_Count:
                minimum_Count = all_Counts[x]
                minimum_Word = all_Words[x]
        new_Counts.append(minimum_Count)
        new_Words.append(minimum_Word)
        all_Counts.remove(minimum_Count) 
        all_Words.remove(minimum_Word)
    #loop which prints the words ancd counts into the Decreasing_Frequency.txt
    for i in range(len(new_Counts)):
        text.write(new_Words[i] + ', ')
        text.write(str(new_Counts[i]) + '\n')
    text.close()

    
