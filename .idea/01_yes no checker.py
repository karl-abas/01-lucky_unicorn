
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

#looping
#show_instruction=""
show_instruction = yes_no("have you played the game before")
print("you chose {}".format(show_instruction))
print()
having_fun = yes_no("are you having fun?")
print("you said {} to having fun".format(having_fun))
