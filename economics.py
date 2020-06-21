import random
class questions():
    def questionList():
        score = 0
        qOne = str(input("True or False: One way inflation occurs when the rate of spending exceeds the rate of goods produced\n>"))
        if qOne == "True".lower():
            print("Correct, next question...")
            score =+ 1 
        elif qOne ==  "False".lower():
            print("Incorrect; this is indeed one way it happens")
        else:
            print("Invalid choice, your answer was defaulted to 'incorrect'.")
questions.questionList()