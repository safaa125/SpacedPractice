import time
import economics

#Introduction
class intro():
    def mainIntro():
        print("Welcome to the quiz!\nThere are three topics choose from.")
        global choice
        choice = input("\nCrypto, Economics or St John?\n>>")
        intro.selection()
#Choice of Topics
    def selection():
        if choice == "Crypto".lower():
            print("Chosen Crypto\n")
        elif choice == "Economics".lower():
            print("Chosen Economics\n")
            economics.ecoQuestions.questionOne()
        elif choice == "St John".lower():
            print("Chosen Medic\n")
        else:
            print("That is not a valid choice, try again\n\n")
            intro.mainIntro()

#Timer

#Right/Wrong total

#Questions from Topic 1

#Questions from Topic 2

#Questions from Topic 3
intro.mainIntro()