#looping
show_instruction=""
while show_instruction != "finnished":
    # ask the user if they played before
    show_instruction = input("have you played before").lower()

    # if they say yes, outpurt 'program continues'
    if show_instruction == "yes" or show_instruction == "b":

        print("program continues")
    elif show_instruction =="no" or show_instruction == "n":

        print("display instructions")

    # if they say no, outpiut 'display instruction'
    else:
        print("please answer yes or no")
