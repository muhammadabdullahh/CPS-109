#This program is used as a conversion calculator, these conversion include, Decimal to Binary,
#Decimal to Octal, and Decimal to Hexadecimal.
#The user is prompted to pick a conversion, followed by a decimal they would like to convert
#@Author Muhammad Abdullah
#Student ID: 501112499
#Date: September 12, 2021
#CPS109 Assignment 1

#Conversion Selecter
def main_Frame():   #this function is used to determind which conversion the user wants
    play_Back = True    #Variable to determine if the loop should stop or continue
    while play_Back == True:
        print("\n\nWhat conversion would you like: \n1: Decimal to Binary\n2: Decimal to Octal\n3: Decimal to Hexadecimal\n4: Exit")
        x = int(input())    #users input on what conversion they would like
        if x <= 4 and x >=1:    #error checking
            if x == 1:
                dec_To_Binary()
                play_Back = False   #stopping the loop
            elif x == 2:
                dec_To_Octal()
                play_Back = False
            elif x == 3:
                dec_To_Hex()
                play_Back = False
            else:
                print("BYE BYE")
                play_Back = False
        else:
            print("Invalid Input, enter 1, 2, 3, or 4\n")  #error check

#Decimal to Binary
def dec_To_Binary():
    print("\n\nDecimal to Binary\nEnter a decimal number: ")
    x = int(input())
    y = x   #copying the user input for later use
    z = []  #creating a list
    while(x > 0):
        temp = x % 2    #finding the remainders to determine the elements
        z.append(temp)  #adding an element to the list
        x = x // 2
    z.reverse() #reversing the list because LSD and MSD
    print(y,"'s Binary Equivalent is: ")
    s = ''  
    for i in range(len(z)):
        s = s + (str(z[i])) #creating a string and adding the list to it, so it will print cleaner
    print('= ', s)
    main_Frame()       #returning back to the mainframe

#Decimal to Octal
def dec_To_Octal():
    print("\n\nDecimal to Octal\nEnter a decimal number: ")
    x = int(input())
    temp = x
    z = []
    while temp > 0: #this entire loop is basicallt using the binary to octal method, just in code
        r = temp % 8    #find the remainder to find the octal elements
        z.append(r) #adds a element to the list
        temp = int(temp / 8)
    z.reverse() 
    print(x, 's Octal Equivalent is: \n')
    s = ''
    for i in range(len(z)):
        s = s + (str(z[i]))
    print('= ', s)
    main_Frame()

#Decimal to Hexadecimal
def dec_To_Hex():
    print("\n\nDecimal to Hexadecimal\nEnter a decimal number: ")
    x = int(input())
    temp = x
    z = []  #creating a list
    while temp > 0:
        r = temp % 16   #using the hexademal conversion method, and turning it into code
        z.append(r) #adding an element to the list
        temp = int(temp / 8)
    z.reverse() #reversing hr elist
    s =''
    for i in range(len(z)): #replacing int above 9 with proper letters (hexadecimal numbering)
        if z[i] == 10:      #all of the if statements are used to replace the appropriate elements
            s = s + 'A'     #adding all th elements into a string so that it prints neater
        elif z[i] == 11:
            s = s + 'B'
        elif z[i] == 12:
            s = s + 'C'
        elif z[i] == 13:
            s = s + 'D'
        elif z[i] == 14:
            s = s + 'E'
        elif z[i] == 15:
            s = s + 'F'
        else:
            s = s + (str(z[i-1]))
        
    print(x, 's Octal Equivalent is: \n')
    print('= ', s)
    main_Frame()    #returning back to the main frame

#Main method
if __name__ == '__main__':
    main_Frame()    #calling the main function
