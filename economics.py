from textwrap import dedent
print("hello there, made a change")
print("Will it commit?")
print("Merged success, how bout now when the branch does not exist on server?")

class ecoQuestions():
    global score
    score = 0
    def questionOne():
        qOne = str(input("True or False: One way inflation occurs when the rate of spending exceeds the rate of goods produced\n>>"))
        if qOne == "True".lower():
            print("Correct, next question...")
            score =+ 1 
        elif qOne ==  "False".lower():
            print("Incorrect; this is indeed one way it happens")
        else:
            print("Invalid choice, your answer was defaulted to 'incorrect'.")
        ecoQuestions.questionTwo()

    def questionTwo():
        qTwo = str(input(dedent("""
        In a devaluation:
        A) There is a boost in the economy
        B) Debt is larger than income
        C) Lowering interest rates will have no impact
        D) It is part of the short cycle
        E) B & C
        >>""")))

        if qTwo == "E".lower():
            print("Correct, next question...")
            score =+ 1 
        elif qTwo == "A".lower():
            print("Incorrect, there is a decline in economic activity.")
        elif qTwo ==  "B".lower():
            print("That's correct, but not the sole reason, interest rates tend to be close to if not already zero, and cannot be lowered further.")
            score =+ 0.5
        elif qTwo == "C".lower():
            print("That's correct, but not the sole reason, there is also a large amount of debt.")
            score =+ 0.5
        elif qTwo == "D".lower():
            print("Incorrect, it is part of Dalio's long term cycle; the predecessor of a depression.")
        else: 
            print("Invalid choice, your answer was defaulted to 'incorrect'.")
        ecoQuestions.questionThree()

    def questionThree():
        qThree = str(input("True or False: Credit can be generated without production?\n>>"))
        if qThree == "True".lower():
            print("Correct, next question...")
            score =+ 1 
        elif qThree ==  "False".lower():
            print("Incorrect; if anything, if you have a lot of production, you're entitled to more credit by nature of your income.")

#print("your score is: ", score) will not be shown outside of a class
