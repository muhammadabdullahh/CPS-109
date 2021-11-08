import random

def problem_One():
    l = []  
    for i in range(20):
        num = random.randint(1,6)
        l.append(num)
    inRun = False
    for i in range(len(l)):
        if inRun:
            if l[i] != l[i-1]:
                print(')', end= '')
                inRun = False
        if inRun == False:
             if i != len(l)-1:
                 if l[i] == l[i+1]:
                    print('(', end= '')
                    inRun = True
        print(l[i], end= '')
    if inRun:
        print(')', end= '')

def problem_Two():
    L = []  
    for i in range(20):
        num = random.randint(1,6)
        L.append(num)
    print(L)

    biggestStart = 0
    biggestEnd = 0
    for e in range(len(L)):
        start = 0
        end = 0
        for i in range(len(L)):
            if L[i] == L[e]:
                tempStart = i
                j = i
                if j >= len(L):
                    tempEnd = i
                    break
                else:
                    while (L[j] == L[e]) and ((j+1) < len(L)):
                        tempEnd = j
                        j+=1
            if (tempEnd - tempStart) > (end-start):
                start = tempStart
                end = tempEnd 
            #print('Start', start, "Biggest", end)
        if (end-start) > (biggestEnd - biggestStart):
                print('hi')
                biggestStart = start
                biggestEnd = end 
    if biggestEnd == biggestStart:
        biggestStart, biggestEnd = -1, -1
    for p in range(len(L)):
        if p == biggestStart:
            print('(', end= '')
            print(L[p], end = ' ')
        elif p == biggestEnd:
            print(L[p], end=' ')
            print(')', end= '')
        else:
            print(L[p], end= ' ')  

def problem_Three():
    def longestFalse(L):
        start = -1
        end = -1
        for i in range(len(L)):
            if L[i] == False:
                tempStart = i
                j = i
                if j >= len(L):
                    tempEnd = i
                    break
                else:
                    while (L[j] == False) and ((j+1) < len(L)):
                        tempEnd = j
                        j+=1
            if (tempEnd - tempStart) > (end-start):
                start = tempStart
                end = tempEnd 
        tup = (start,end)
        return(tup)
    l = [False, False, True,False, False, False, False, True, True, False, False]
    print(longestFalse(l))

def problem_Four():
    def occupy(n):
        L = []
        for i in range(n):
            L.append('_')
        for i in range(n):
            start = -1
            end = -1
            for i in range(len(L)):
                if L[i] == '_':
                    tempStart = i
                    j = i
                    if j >= len(L):
                        tempEnd = i
                        break
                    else:
                        while (L[j] == '_') and ((j+1) < len(L)):
                            tempEnd = j
                            j+=1
                if (tempEnd - tempStart) >= (end-start):
                    start = tempStart
                    end = tempEnd 
            L[round((start + end)/2)] = 'X'
            s = ""
            for e in L:
                s = s + e
            print(s)
    occupy(20)
        
def problem_Five():
    def isPal(L):
        rev = L.copy()
        rev.reverse()
        if L == rev:
            return True
        return False
            
    l = [2,2,2,2,2,2]
    print(isPal(l))

print("problem 1")
problem_One()
print("\n\nproblem 2")
problem_Two()
print("\n\nproblem 3")
problem_Three()
print("\n\nproblem 4")
problem_Four()
    



