import time
print("looks like once a branch is merged on server, it remains locally")
print("Is it best practice to delete branches locally after they're merged on server?")
#Introduction
class intro():
    def mainIntro():
        print("Welcome to the quiz!\nThere are three topics choose from.")
        global choice
        choice = input("\nCrypto, Economics or St John?\n>")
        intro.selection()
#Choice of Topics
    def selection():
        if choice == "Crypto":
            print("Chosen Crypto")
        elif choice == "Economics":
            print("Chosen Economics")
        elif choice == "St John":
            print("Chosen Medic")
        else:
            print("That is not a valid choice, try again\n\n")
            intro.mainIntro()

#Timer

#Right/Wrong total

#Questions from Topic 1

#Questions from Topic 2

#Questions from Topic 3
intro.mainIntro()