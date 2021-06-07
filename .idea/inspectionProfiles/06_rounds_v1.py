import random

#set balance for testing purposes
balance = 5
rounds_played = 0
play_again = input("press <enter> to play...").lower()
while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    #print round number
    print()
    print("*** Round #{} ***".format(rounds_played))
    chosen_num = random.randint(1,100)
    #adjust balance
    # if the random # is between 1 and 5 user gets a unicorn (add $4 to balance)
    if 1<= chosen_num <= 5:
        chosen = "unicorn"
        balance +=4
    #  if the random # is between 6 and 36 user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <=36:
        chosen = "donkey"
        balance -=1
    else:
        # if the number is even(divisible by 2) set token to horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            balance -= 0.5
        #otherwise set it to zebra
        else:
            chosen = "zebra"
            balance -= 0.5



        #output
    print("you got a {}. your balance is ${:.2f}".format(chosen,balance))


    if balance <1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("press enter to play again or xxx to quit")
