#P1: Write a program that asks the user for a temperature in Fahrenheit and prints out the same temperature in Celsius.

#Firstly, ask a question for tempF (temp if fahrenheit)
tempF = int(input(" Input a number in Fahrenheit: "))
#then this below is the calculation for the tempF to tempC
tempC = (tempF - 32) * (5 / 9)
#Prints the final answer in celsius.
print(" Your temperature in celsius is " , tempC)

# P2: Write a program that converts from Fahrenheit to Celsius or from Celsius to Fahrenheit, depending on the user's choice.

#First ask the user if the want to either convert from Fahrenheit to Celcius or vise versa.
change = input("Input either 0 to convert Fahrenheit to Celcius, or input 1 to convert Celcius to Fahrenheit:  ")
#Then ask the number that they want to change
Ntemp = input("Input the temperature that you are wanting to convert: ")
#if the user decides to either convert from Celcius or Fahrenheit it goes into a conversion it uses the same equation as the previous qustion and it will always work.
if float(change)== 0:
  #This is the Fahrenheit to Celsius
  Ntemp = (float(Ntemp)- 32) * 5 / 9
  print("The temperature in celsius is: %s." %Ntemp)

elif float(change) == 1: 
  #This is the Celsius to Fahrenheit
  Ntemp = float(Ntemp) * 9 / 5 + 32
  print("The temperature in fahrenheit is: %s." %Ntemp) 
#If they dont do anything it will say the message below.
else:
  print("You have to either input 0 or 1 to convert. ")

#P3: Write a program that lets the user type words and when they press 'x', it prints how many words the user inputted then quits the program.

#The total words will always be 0 
total = 0
#After it will go through the code.
while True:
  #So the variable W will be set for words and it will easily work and count the amount of words.
    W = input("Enter words of your choice I will count it otherwise press x to quit: ")
    print (W)
    #Then it says if words = x then the count will stop and say the amount of words.
    if W== "x":
        print ("The total amount of words you typed is %s." %total)
        #if x is pressed than it will stop and give the total.
        break
    #This will add one to the count everytime a word is added
    else:
        total = total + 1

#P4: Write a program in which a password is set and the program will keep prompting the user to guess it, until they get the word right.

#This is my password and the variable password is set.
password = ("God")
#The variable guess will the users guess for the password itself, then it prints a message basically  saying to try to guess the right password.
guess = input("Try and guess the password you will never guess it right: ")
#Then this will start the loop and this means if the guess was wrong it will say I told you so.
while guess != password:
    print ("I told you so, ")
    #After this it will say to guess again
    guess = input("Guess again, good luck: ")
    #if they somehow manage to guess it will display a secret message
    if guess == password:
        print ("Good job, بارك الله فيك!")

#P5: Write a program that asks for a user to enter a number, and then print all those numbers after 10 numbers are entered.
#First create two variables in this case, numtotal and listtotal.
numtotal =0
listtotal =[]
#Then after, it shows 0-9 numbers must be entered after the tenth it will print meaning this while numtotal has to <=9.
while numtotal <=9:
  #Then the num= the message will say that it needs a message that says Enter the numbers you deseire.
    num=input("Enter the numbers you desire: ")
    #This is the numtotal and it will + 1 everytime.
    numtotal = numtotal + 1
    #Then listtotal which is the whole list must append num.
    listtotal.append(num)
  #After this then its easy because the numbers will print the message "The magic numbers you entered were:".
print ("The magic numbers you entered were: ")
#After this its the code that will list the total numbers and join everything together
print ("\n".join(listtotal))
#Finished now
print("Thank you I hope everything went well.")