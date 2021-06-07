import random
#function goes here

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
            print()
def instructions():
    rules_welcome = statement_generator("how to play", "=")
    print (rules_welcome)
    print()
    print("the rules of the game go here")
    print()
    return ""

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

def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement + "1")

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return""

#main routine goes here
welcome = statement_generator("welcome to lucky unicorn", "-")
print (welcome)

#ask the user if the played before
played_before = yes_no("have you played the game before?")

if played_before =="no":
    instructions()
else:
    print("program continues")

#ask how much the user want to pay
how_much = num_check("how much would you like to pay?", 0, 10)
print("you will be spending ${}".format(how_much))

#set balance for testing purposes
balance = how_much
rounds_played = 0
play_again = input("press <enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    #print round number
    print()
    round = statement_generator("round #{}".format(rounds_played), "#")
    (" Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1,100)
    #adjust balance
    # if the random # is between 1 and 5 user gets a unicorn (add $4 to balance)
    if 1<= chosen_num <= 5:
        chosen = "unicorn"
        balance +=4
        decoration = "!"
    #  if the random # is between 6 and 36 user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <=36:
        chosen = "donkey"
        balance -= 1
        decoration = "D"
    else:
        # if the number is even(divisible by 2) set token to horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            balance -= 0.5
            decoration = "H"
        #otherwise set it to zebra
        else:
            chosen = "zebra"
            balance += 0.5
            decoration = "Z"


    #output
    outcome = "you got a {}. your balance is ${:.2f}".format(chosen,balance)

    statement_generator(outcome, decoration)


    if balance <1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("press enter to play again or xxx to quit")
print()
ending = statement_generator("RESULTS", "-")
print (ending)
print("you final balance is ${:.2f}. thank you for playing".format(balance))
