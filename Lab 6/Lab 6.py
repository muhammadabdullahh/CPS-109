import math
import random

def problem_One():
    list = []
    for i in range(10):
        print("Enter String ")
        list.append(str(input()))
    for i in range(9,-1,-1) :
        print("String ", i , "/10: ", list[i])
def problem_Two():
    def max(L):
        hasFloat = False
        temp = 0.0
        for i in range(len(L)):
            if type(L[i]) == float:
                hasFloat = True
                if temp < L[i]:
                    temp = L[i]
        if hasFloat == False:
            return None
        else:
            return temp
    print(max([100, 'blue', 3.5, 'sugar on the rocks', 7.0]))
    print(max([7, 2, 9, 1]))

def problem_Three():
    def longest(L):
        largestyet = L[0]
        for i in range(1, len(L)):
            if len(L[i]) > len(largestyet):
                largestyet = L[i]
        return largestyet
    print(longest(['blue', 'red', 'the old barn', 'the white house', 'green']))

def problem_Four():
    L = []
    for i in range(1, 101):
        L.append(i)
    T = ()
    for i in range(1, 101):
        T += (i,)
    print(L,"\n", T, "\n")

    L = []
    for i in range(1, 102, 2):
        L.append(i)
    T = ()
    for i in range(1, 102, 2):
        T += (i,)
    print(L,"\n", T, "\n")

    L = []
    for i in range(0, 50):
        L.append(i**2)
    T = ()
    for i in range(0, 50):
        T += (i**2,)
    print(L,"\n", T, "\n")

    L = []
    for i in range(60):
        L.append(random.randrange(0, 50))
    T = ()
    for i in range(60):
        T += (random.randrange(0, 50),)
    print(L,"\n", T, "\n")

    L = []
    for i in range(50):
        L.append(0)
    T = ()
    for i in range(50):
        T += (0,)
    print(L,"\n", T, "\n")
    

def problem_Six():
    def perimiter(poly):
        perimiter = 0.0
        for i in range(len(poly)-1):
            x1, y1, x2, y2, = poly[i][0], poly[1][1], poly[i+1][0], poly[i+1][1]
            d = math.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
            print("the distance between ", poly[i], " and ", poly[i+1], ": ", d)
            perimiter += d
        print("The perimiter of the polygon is: ", perimiter)

def problem_Seven():
    def permutation(L):
        P = []
        C = list(L)
        for i in range(len(C)):
            i = random.randrange(0, len(C))
            P.append(C[i])
            C.pop(i)
        return P
    print(permutation([19, 4, 3, 17]))
    print(permutation([19, 4, 3, 17]))

    poly = [(0, 0), (20, 0), (20, 10), (0, 10)]
    print(permutation(poly))
    print(permutation(poly))


if __name__ == "__main__":
    problem_Four()
