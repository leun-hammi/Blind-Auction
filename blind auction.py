print("!welcome to blind auction!...\n here it is what it is kid! u cant fight with money anymore!\n lets see how generous u are")

bidders = {}


def bidding():
    while True:
        name = input("what is your name?")
        bid_amount = int(input("how much would you like to bid today?"))
        bidders[name] = bid_amount
        again = input("is there anyone else to bid?yes or no?").lower()
        if again != "yes":
            break
        print("\n"*100)

bidding()

highest_bid = 0
winner = ""

for bidder in bidders:
    if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
        winner = bidder
print(f"the final winner of this bid is {winner} with a bid of {highest_bid}")

