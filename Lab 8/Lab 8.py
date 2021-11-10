
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
    if x == 0: 
        return 1
    if x==1:
        return x
    else:
        return x * (power(x,n-1))
                
        


if __name__ == "__main__":
    print(add(5,9))
    print(log2(20))
    print(reverse("Hi How Are You"))
    print(power(2,10))
