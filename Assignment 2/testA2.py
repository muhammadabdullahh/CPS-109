import unittest
#importing all functions from each task needed to test
from TaskOne import getNumOfPairs
from TaskTwo import getOverlap
from TaskTwo import getUnique
from TaskThree import get_unique_dict
from TaskFour import getQuestions
from TaskFive import getAnswers
from TaskSix import getFrequency
from TaskSeven import getDecFrequency

class MyTests(unittest.TestCase):
    #printing number of pairs for task one
    print("Testing Task 1...\n")
    print("\tnumber of pairs: ", getNumOfPairs(), "\n")

    #creating an overlap and unique text file for task two
    print("Testing Task 2...\n")
    getUnique()
    print("\tunique_QA_Pairs.txt Created\n")
    getOverlap()
    print("\tOverlapping.txt Created\n")

    #Storing the pairs from unique_QA_Pairs.txt as a dictionary for task three
    print("Testing Task 3...\n")
    myDict = get_unique_dict()
    print("\tdictionary of unique pairs created and returned: \n")
    print("Would you like to print the entire dictionary? Enter 'y' or 'n': ")
    ans = input(str())
    if ans == 'y':
        print("Printing the entire Unique Dictionary: \n", myDict)
    else:   print("\n")

    #creating a Questions.txt for all questions for part four
    print("Testing Task 4...\n")
    getQuestions()
    print("\tQuestions.txt Created\n")

    #creating a Answers.txt for all answers for part five
    print("Testing Task 5...\n")
    getAnswers()
    print("\tAnswers.txt Created\n")

    #creating a Frequency.txt for part six
    print("Testing Task 6...\n")
    getFrequency()
    print("\tFrequency.txt Created\n")

    #creating a Decreasing_Frequency.txt for part seven
    print("Testing Task 7...\n")
    getDecFrequency()
    print("\tDecreasing_Frequency.txt Created\n")


if __name__ == '__main__':
    unittest.main(exit=True)
    
    