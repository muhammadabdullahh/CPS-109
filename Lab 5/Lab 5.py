def problem_One():
    def helloWorld():
        print("Hello World")
    def call_Ten():
        x = 0
        while x < 10:
            helloWorld()
            x+=1

    helloWorld()
    call_Ten()

def problem_Two():
    def hello(name):
        print("Hello", name)
    print("What is your name")
    hello(str(input()))
    
def problem_Three():
    def hello(first, last):
        print('Hello', first, last)
        print('Hello', last+',', first)

    print('Enter First Name')
    f = str(input())
    print('Enter Last Name')
    l = str(input())
    hello(f,l)

def problem_Four():
    def repeat_Phase(phrase, n):
        x = 0
        while x < n:
            if (x%2) == 0:
                print(phrase.upper())
                x+=1
            else:
                print(phrase.lower())
                x+=1
    print("Enter your phrase")
    p = input()
    print("Enter how many times to repeat")
    n = int(input())
    repeat_Phase(p,n)
    
def problem_Five():
    def timestable(n):
        for i in range(n):
            for j in range(n):
                print((i+1) * (j+1), end = "\t")
            print('\n')
    print("Enter a number")
    timestable(int(input()))  

def problem_Six():
    def perfectcube(n):
        ans = False
        i = 0
        while ans == False:
            if ((i+1)**3) == n and ((i+1)**3) <= n:
                return True
            elif ((i+1)**3) > n:
                return False
            else:
                i+=1
                ans = False
        return False
    print('Enter a Number')
    x = float(input())
    if perfectcube(x)== True:
        print("Yes, that number is a perfect cube")
    else:
        print("No, that number is not a perfect cube")
 
def problem_Seven():
    def biggestOdd():
        temp = 0
        while True:
            print("Enter a Number")
            x = int(input())
            if x == 0:
                return temp
            elif (x%2) != 2 and x > temp:
                temp = x
            else:
                temp = temp
    print('The Largest Odd Number is:', biggestOdd())

def problem_Eight():
    def biggestBuried(s):
        nums_recovered = []
        s += '.'
        num = ''

        for i in range(len(s)):
            if s[i].isdigit():
                num += s[i]
            else:
                if len(num) > 0:
                    nums_recovered.append(int(num))
                num = ''
        return max(nums_recovered)
    print(biggestBuried('abcd51kkk3kk19ghi'))



def problem_Nine():
    def sqaureRoot(x, epsilon):
        low = 1.0
        high = x
        y = (high+low)/2.0

        while abs(y**2 - x) > epsilon:
            if y**2 < x:
                low = y
            else:
                high = y
            y = (high + low) / 2.0
        return(y)
    print(sqaureRoot(16, 0.01))

def problem_Ten():
    def decimalToBinary(n):
        y = n 
        z = []
        if n == 0:
            return 0  
        while(n > 0):
            temp = n % 2    
            z.append(temp)  
            n = n // 2
        z.reverse() 
        s = ''  
        for i in range(len(z)):
            s = s + (str(z[i])) 
        return(s)
    def callFunc(n):
        for i in range(n):
            print((decimalToBinary(i)), ' is the binary of ', i)
    callFunc(10)


if __name__ == "__main__":
    problem_Eight()