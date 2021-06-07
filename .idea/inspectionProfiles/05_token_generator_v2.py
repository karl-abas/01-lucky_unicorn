import random

#main routine goes here
tokens = ["unicorn", "horse",  "zebra", "donkey"]
starting_balance = 100

balance = starting_balance
#testing loop to generate 20 tokens
for item in range(0,20):
    chosen = random.choice(tokens)
    #adjust balance
    if chosen == "unicorn":
        balance +=4
    elif chosen == "donkey":
        balance -=1
    else:
        balance -= 0.5

    #output
print ()
print("starting balance:${:.2f}".format(starting_balance))
print("final balance: ${:.2f}".format(balance))
