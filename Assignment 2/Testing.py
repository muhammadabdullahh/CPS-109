#importing all functions from each task needed to test
from TaskOne import getNumOfPairs
from TaskTwo import getOverlap
from TaskTwo import getUnique
from TaskThree import get_unique_dict
from TaskFour import getQuestions
from TaskFive import getAnswers
#from TaskSix import getUnique
#from TaskSeven import getUnique

if __name__ == '__main__':
    #printing number of pairs for task one
    print("Task 1, number of pairs: ", getNumOfPairs(), "\n")

    #creating an overlap and unique text file for task two
    getUnique()
    print("Task 2, unique_QA_Pairs.txt Created\n")
    getOverlap()
    print("Task 2, Overlapping.txt Created\n")

    #Storing the pairs from unique_QA_Pairs.txt as a dictionary for task three
    myDict = get_unique_dict()
    print("Task 3: dictionary of unique pairs created and returned: \n")
    print("Would you like to print the entire dictionary? Enter 'y' or 'n': ")
    ans = input(str())
    if ans == 'y':
        print("Printing the entire Uniqie Dictionary: \n", myDict)

    #creating a Questions.txt for all questions for part four
    getQuestions()
    print("Task 4, Questions.txt Created\n")

    #creating a Answers.txt for all answers for part five
    getAnswers()
    print("Task 5, Answers.txt Created\n")

    #


    