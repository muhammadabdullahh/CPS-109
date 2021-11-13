
from TaskOne import getNumOfPairs
def getUnique():
    result = getNumOfPairs()[1]
    pairs = result[1]
    unique = open('unique_QA_Pairs.txt', 'w')
    overlap = open('Overlapping.txt', 'w')


    for i in range(len(pairs)):
        for j in range(i, len(pairs)):
            if ((pairs[i] == pairs[j]) or (pairs[i][0] == pairs[j][0]) or (pairs[i][1] == pairs[j][1])):
                overlap.write(pairs[i][0] + "\n")
                overlap.write(pairs[i][1] + "\n")
            else:
                unique.write(pairs[i][0] + "\n")
                unique.write(pairs[i][1] + "\n")
    unique.close()
    overlap.close()
    
def getOverlap():
    pass

if __name__ == '__main__':
    getUnique()
    