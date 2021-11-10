
#problem 1
def add(a,b):

    if b > 0:
        a+= 1
        return(add(a,b-1))
    return a

#problem 2
def log2(x):
    if x <= 1:
        return 0
    else:
        return 1+log2(x//2)

#problem 3
def reverse(sentence):
    if len(sentence) == 0:
        return sentence
    else:
        return reverse(sentence[1:]) + sentence[0]

#problem 4
def power(x,n):
    if n == 0: 
        return 1
    else:
        global countCalls
        countCalls += 1
        return x * (power(x,n-1))
countCalls = 0

#problem 6
def powerHalf(x,n):
    if n%2 == 0:
        if n == 0: 
            return 1
        else:
            global countCalls
            countCalls += 1
            return x * (power(x,n/2))
    else:
        if n == 0: 
            return 1
        else:
            countCalls += 1
            return x * (power(x,n-1))
countCalls = 0

#problem 7
def problem_7():
    def gcContent(sequence): 
        # You do the rest
        count = 0
        for i in range(len(sequence)):
            if sequence[i] == ('A') or sequence[i] == ('C'):
                count+=1
        print("\nPercentage of A or C: ", count/len(sequence),'%')
    f = open('kdpF.txt') # opens a file for reading 
    line = f.readline() # reads a single line 
    print(line)
    seq = ''
    for line in f : # reading the rest of the lines
        seq = seq + line
    seq = seq.replace('\n', '') # removing the newline characters 
    seq = seq.upper()
    print(seq)
    gcContent(seq)



if __name__ == "__main__":
    #problem 1
    print("PROBLEM 1\n", add(5,9))
    #problem 2
    print("PROBLEM 2\n", log2(20))
    #problem 3
    print("PROBLEM 3\n", reverse("Hi How Are You"))
    #problem 4
    print("PROBLEM 4\n", power(3,2))
    #problem 5
    countCalls = 0
    print("PROBLEM 5\n For power(2,5)", power(2,5), " --> count calls: ", countCalls)
    countCalls = 0
    print("\n For power(5,10)", power(5,10), " --> count calls: ", countCalls)
    countCalls = 0
    print("\n For power(5,0)", power(5,0), " --> count calls: ", countCalls)
    #problem 6
    print("\nPROBLEM 6 For power(2,5)", powerHalf(2,5), " --> count calls: ", countCalls)
    #problem 7
    print("\nPROBLEM 7")
    problem_7()
    

   
