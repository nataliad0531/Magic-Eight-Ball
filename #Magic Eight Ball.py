#Magic Eight Ball
#Natalia Diaz
import random
#Functions
Responses=["without a doubt", "It is decidely so", "No" , "Ask again later", "Outlook good","Without a doubt", "Idk ask Aminat Rosenje", "That will never happen", "My sources say no", "Signs point to yes"]
 

#prompts user to ask question and validates the user's input to ensure it ends with a "?". Creates a loop o repeat the question-answering process until the user chooses to exit.
def askQuestion():
    question= input("Ask a question")
    if question.endswith("?"):
        print("Good Question!")
        print(random.choice(Responses))
        option=input("Ask Another Question?(y) or (n))")
        if option=="y":
            askQuestion()
        if option=="n":
            print("Goodbye!")
            quit()    
    elif():
        print("please ask a question that end in question mark")
        askquestion()

#Intro to Magic Eight Ball Game 
def MagicEightBall():
    print("Welcome to the Magic Eight Ball!")  
    print("Press 1 to continue")
    print("Press 2 to quit")
    option=int(input("Continue(1) or Exit(2)?"))
    if option==1:
        askQuestion()
    if option==2:
        print("Goodbye!")
        quit()      


#Main
MagicEightBall()




