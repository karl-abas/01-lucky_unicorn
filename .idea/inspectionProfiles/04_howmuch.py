#functions go here

#main route goes here
error = "please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask the question
        response = int(input("how much would you like to pay? "))
        # if the ammount is too low/ too high give
        if 0 < response <= 10:
            print("you have asked to play with ${}".format(response))

        else:
            print (error)
    except ValueError:
        print(error)

