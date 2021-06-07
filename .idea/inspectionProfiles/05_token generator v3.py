import random

#main routine goes here

starting_balance = 100

balance = starting_balance
#testing loop to generate 20 tokens
for item in range(0,5):
    #choose number from 1 to 100
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
        #otherwise set it to zebra
        else:
            chosen = "zebra"
        balance -= 0.5

        balance -= 0.5
    print("you got a {}. your balance is ${:.2f}".format(chosen,balance))
    #output
print ()
print("starting balance:${:.2f}".format(starting_balance))
print("final balance: ${:.2f}".format(balance))
