
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("please answer yes or no")

def instructions():
    print("***how to play***")
    print()
    print("the rules of the game go here")
    print()
    return ""
#looping
#show_instruction=""
played_before = yes_no("have you played the game before")

if played_before == "yes":
    print("programm continuous")
else:
    instructions()
