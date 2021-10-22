#PROBLEM Set for Lab 3
#Author @Muhammad Abdullah
#Date: September 28th, 2021

#PROBLEM 1
def problem_One(num):
    print("\n\nPROBLEM #1")
    if num > 0 :
        print("This number is positive")
    elif num == 0:
        print("This number is zero")
    else:
        print("This number is negative")

#PROBLEM 2
def problem_Two(num):
    print("\n\nPROBLEM #2")
    if num > 0: 
        if num < 1:
             print("This is a small positve number")
        elif num > 1000:
            print("This is a large positive number")
        else:
            print("This number is positive")
    elif num == 0:
        print("This number is zero")
    else:
        if num > -1:
            print("This is a small negative number")
        elif num < -1000:
            print("This is a large negative number")
        else:
            print("This number is negative number")
    
#PROBLEM 3
def problem_Three(num):
    print("\n\nPROBLEM #3")
    if num >= 1000000:
        print("lots of digits")
    else:
        if num >= 10 and num < 100:
            print("Two digits")    
        elif num >= 100 and num < 1000:
            print("Three digits")
        elif num >= 1000 and num < 10000:
            print("Four digits")
        elif num >= 10000 and num < 100000:
            print("Five digits")
        elif num >= 100000 and num < 1000000:
            print("Six digits")
        else:
            print("One digit")
    
#PROBLEM 4
def problem_Four(num_One, num_Two, num_Three):
    print("\n\nPROBLEM #4")
    if num_One == num_Two and num_One == num_Three:
        print("all the same")
    elif num_One != num_Two and num_One != num_Three and num_Two != num_Three:
        print("all different")
    else:
        print("neither")

#PROBLEM 5
def problem_Five(num_One, num_Two, num_Three):
    print("\n\nPROBLEM #5")
    if num_One < num_Two and num_Two < num_Three:
        print("increasing")
    elif num_One > num_Two and num_Two > num_Three:
        print("decreasing") 
    else:
        print("neither")           

#PROBLEM 6
def problem_Six(num_One, num_Two, num_Three):
    print("\n\nPROBLEM #6")
    answer = input(print("increasing/decreasing, type 'strict' or 'lenient: "))
    if answer == 'strict':
        print("\n\nPROBLEM #6")
        if num_One < num_Two and num_Two < num_Three:
            print("increasing")
        elif num_One > num_Two and num_Two > num_Three:
            print("decreasing") 
        else:
            print("neither")     
    elif answer == 'lenient':
        print("\n\nPROBLEM #6")
        if num_Three == num_Two and num_Three == num_One:
            print("increasing and decreasing")
        elif num_One <= num_Two and num_Two <= num_Three:
            print("increasing")
        elif num_One >= num_Two and num_Two >= num_Three:
            print("decreasing") 
        else:
            print("neither")    

#PROBLEM #7
def problem_Seven(num_One, num_Two, num_Three):
    print("\n\nPROBLEM #7")
    if (num_One < num_Two and num_Two < num_Three) or (num_One > num_Two and num_Two > num_Three):
        print("In Order")
    else:
        print("Not in Order")

#PROBLEM #8
def problem_Eight(num_One, num_Two, num_Three, num_Four):
    digits = [num_One, num_Two, num_Three, num_Four]
    digit_Pairs = 0
    for i in range(len(digits)):
        for j in range(i+1, len(digits)):
            if digits[i] == digits[j]:
                digit_Pairs += 1

    if digit_Pairs >= 2:
        print("Two Pairs")
    else:
        print("not two pairs")
#PROPBLEM #9
def problem_Nine(temp, letter):
    print("\n\nPROBLEM #9")
    if letter == 'C':
        if temp <= 0:
            print("water is solid")
        elif temp > 100:
            print("water is gaseous")
        else:
            print("water is liquid")

    else:
        if temp < 32:
            print("water is solid")
        elif temp > 212:
            print("water is gaseous") 
        else:
            print("water is liquid")

#PROBLEM #10
def problem_Ten():
    print("\n\nPROBLEM #10")
    grade = input(print("Enter a grade: "))
    if grade == 'A+':
        print("The numeric value of A+ is : 3.7")
    elif grade == 'A':
        print("The numeric value of A is : 4")
    elif grade == 'A-':
        print("The numeric value of A- is : 3.7")
    elif grade == 'B+':
        print("The numeric value of B+ is : 3.3")
    elif grade == 'B':
        print("The numeric value of B is : 3")
    elif grade == 'B-':
        print("The numeric value of B- is : 2.7")
    elif grade == 'C+':
        print("The numeric value of C+ is : 2.3")
    elif grade == 'C':
        print("The numeric value of C is : 2")
    elif grade == 'C-':
        print("The numeric value of C- is : 1.7")
    elif grade == 'D+':
        print("The numeric value of D+ is : 1.3")
    elif grade == 'D':
        print("The numeric value of D is : 1")
    elif grade == 'D-':
        print("The numeric value of D- is : 0.7")
    else:
        print("The numeric value of F is : 0")
    
#PROBLEM #11
def problem_Eleven():
    print("\n\nPROBLEM #11")
    sum = 0
    for i in range(99):
        if (i % 2) == 0:
            sum = sum + (i+2)
    print(sum)

#PROBLEM #12            
def problem_Twelve():
    print("\n\nPROBLEM #12")
    sum = 0
    for i in range (101):
        sum = sum + (i**2)
    print(sum)

#PROBLEM 13
def problem_Thirteen():
    print("\n\nPROBLEM #13")
    sum = 0
    for i in range(21):
        sum = sum + (2**i)
    print(sum)

#PROBLEM 14
def problem_Fourteen(a,b):
    sum = 0
    i = a
    while i <= b:
        if (i%2) == 1:
            sum = sum + i
        i+=1
    print(sum)


#PROBLEM 15
def problem_Fifteen(num):
    sum = 0
    string = str(num)
    for i in range(len(string)):
        if ((int(string[i]))%2) == 1:
            sum = sum + (int(string[i]))
    print(sum)



if __name__ == "__main__":
    #TEST

    #PROBLEM ONE TEST
    #problem_One(-3)
    #problem_One(2)
    #problem_One(0)

    #PROBLEM TWO TEST
    #problem_Two(-0.5)
    #problem_Two(-10)
    #problem_Two(-1100)
    #problem_Two(0.5)
    #problem_Two(10)
    #problem_Two(1100)
    
    #PROBLEM THREE TEST
    #problem_Three(1)
    #problem_Three(10)
    #problem_Three(100)
    #problem_Three(1000)
    #problem_Three(10000)
    #problem_Three(100000)
    #problem_Three(1000000)

    #PROBLEM FOUR TEST
    #problem_Four(1,2,3)
    #problem_Four(1,1,1)
    #problem_Four(2,3,3)

    #PROBLEM FIVE TEST
    #problem_Five(1,2,3)
    #problem_Five(3,2,1)
    #problem_Five(3,2,7)

    #PROBLEM SIX TEST
    #problem_Six(1,2,3)
    #problem_Six(3,2,1)
    #problem_Six(1,1,1)
    #problem_Six(2,3,1)

    #PROBLEM SEVEN TEST
    #problem_Seven(1,2,3)
    #problem_Seven(3,2,1)
    #problem_Seven(4,7,1)

    #PROBLEM EIGHT TEST
    #problem_Eight(1,1,2,2)
    #problem_Eight(1,3,2,2)

    #PROBLEM NINE TEST
    #problem_Nine(-15, 'C')
    #problem_Nine(-15, 'F')

    #PROBLEM TEN TEST
    #problem_Ten()
    #problem_Ten()
    #problem_Ten()

    #PROBLEM ELEVEN TEST
    #problem_Eleven()

    #PROBLEM TWELVE TEST
    #problem_Twelve()

    #PROBLEM THIRTEEN TEST
    #problem_Thirteen()

    #PROBLEM FOURTEEN TEST
    #problem_Fourteen(3,5)

    #PROBLEM FIFTEEN TEST
    problem_Fifteen(135)

