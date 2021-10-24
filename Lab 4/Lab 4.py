#Lab 4 -- CPS109
#Author @Muhammad Abdullah
#Date: October 7, 2021

import re
import math

def problem_One(x):
    cube = x
    epsilon = 0.01
    guess = 0.0
    increment = 0.0001
    num_guesses = 0
    while abs(guess**4 - cube) >= epsilon and guess <= cube:
        guess += increment
        num_guesses += 1
    print('num guesses +', num_guesses)
    if abs(guess**4 - cube) >= epsilon:
        print('Failed on fourth root of', cube)
    else:
        print(guess, 'is close to the fourth root of', cube)

def problem_Two():
    print("Enter a number: ")
    x = int(input())
    i = 2
    num = -1
    ans = True
    while i < 6:
        num = x **(1/i)
        if(round(num) ** i) == x:
            print(round(num), " ** ", i, " is ", x)
            ans = True
            break
        else:
            ans = False
        i = i + 1    
    if ans == False:
        print("There is no solution")
    else:
        print(" ")

def problem_Three():
    print("Enter a number: ")
    x = int(input())
    i = 5
    num = -1
    ans = True
    while i > 1:
        num = x **(1/i)
        if(round(num) ** i) == x:
            print(round(num), " ** ", i, " is ", x)
            ans = True
            break
        else:
            ans = False
        i = i - 1    
    if ans == False:
        print("There is no solution")
    else:
        print(" ")

def problem_Four():
    print("Enter a phrase")
    p = input()
    print("Enter the amount of times to print")
    n = int(input())
    i = 0
    while i < n:
        print(p,"\n")
        i= i + 1

def problem_Five():
    num = 0
    for i in range(10):
        print('Enter Number ', (i+1), ": ")
        x = int(input())
        if (x%2) != 0:
            if x > num:
                num = x
            else:
                num = num
        else:
            num = num
    if (num%2) == 0:
        print("There are no odd numbers")
    else:
        print("The largest odd number is ", num)

def problem_Six(str):
    sum = 0
    for i in range(len(str)):
        if(str[i].isdigit() == True):
            sum = sum + (int(str[i]))
        else:
            sum = sum
    print(sum)

def problem_Seven(str):
    sum = 0.0
    temp = 0
    str = str + ','
    for i in range(len(str)):
        if(str[i] == ','):
            #print(i)
            print(sum)
            sum = sum + (float(str[temp:i]))
            temp = i+1
        else:
            sum = sum
    print(sum)

def problem_Eight():
    x = -1
    while x <= -1:
        print("Enter a Positive Value")
        x = int(input())
    epsilon = 0.01
    numGuesses = 0
    low = 1.0
    high = x
    ans = (high+low)/2.0

    while abs(ans**2 - x) >= epsilon:
        print('low= '+ str(low) + ' high = '+ str(high) + ' ans= ' + str(ans))
        numGuesses+= 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print('numGuesses= ' + str(numGuesses))
    print(str(ans) + ' is close to square root of ' + str(x))

def problem_Nine():
    print("Enter a Value")
    x = int(input())
    if x < 0:
        x = (x*-1)
    else:
        epsilon = 0.01
        numGuesses = 0
        low = 1.0
        high = x
        ans = (high+low)/2.0

        while abs(ans**2 - x) >= epsilon:
            print('low= '+ str(low) + ' high = '+ str(high) + ' ans= ' + str(ans))
            numGuesses+= 1
            if ans**2 < x:
                low = ans
            else:
                high = ans
            ans = (high + low) / 2.0
        print('numGuesses= ' + str(numGuesses))
        print(str(ans) + ' is close to square root of ' + str(x))

def problem_Ten(x):
    bin = ''
    temp = x
    loop = True
    while loop == True:
        r = temp%2
        temp = int(temp / 2)
        if temp > 0:
            bin = str(r) + bin
        else:
            bin = str(r) + bin
            loop = False
    print(bin)
        
        
if __name__ == "__main__":
    