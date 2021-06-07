#functions go here
def num_check(question, low, high):
    error = "please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input( question))
            # if the ammount is too low/ too high give
            if low < response <= high:
                return response

            else:
                print (error)
        except ValueError:
            print(error)
#main route goes here
how_much = num_check("how much would you like to pay?", 0, 10)

