#
# You need to replace 'pass' with your code
#


from random import randint
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.
pile = randint(10, 100)
turn = randint(0, 1)
strategy = randint(0, 1)


def nim(pile, turn, strategy):
    """
    return True if the winner is human, False if winner is computer.
    """
    # While the game is still being played.
    while pile > 0:
        if turn == COMPUTER:
            if pile == 1:
                # Take the last marble.
                print('The computer took the last marble.')
                return True
            elif pile == 2:
                take = 1
                pile -= take
            elif strategy == DUMB:
                # Take a random, legal number of marbles from the pile.
                take = randint(1, round((pile - 1)/2))
                pile -= take
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                # The computer is smart, but can't make a smart move.
                # Take a random, legal number of marbles from the pile.
                take = randint(1, round((pile - 1)/2))
                pile -= take
            else:
                # The computer is smart and can make a smart move.
                # Take marbles so that the pile will be be a power of 2, minus
                # 1.
                take = 0
                for i in range(7):
                    if (2**i - 1) >= round(pile/2) and i >= 2:
                        take = pile - (2**(i) - 1)
                        break

                if take <= 0:
                    take = randint(1, round((pile - 1)/2))
                pile -= take
            # Update pile
            pass
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            # take is the variable you might need above
            turn = HUMAN

        elif turn == HUMAN:
            if pile == 1:
                print('There is only one marble left so you are forced to take it.')
                return False

            print("Your turn.   The pile currently has", pile, "marbles in it.")

            take = int(input("How many marbles will you take? "))
            # Force the user to take a legal number of marbles.
            if take > pile / 2:
                print('You cannot take that many marbles')
                turn = HUMAN

            # Update pile
            else:
                pile -= take
                print("Now the pile has", pile, "marbles in it.\n")
                turn = COMPUTER

    return turn == COMPUTER

if nim(pile, turn, strategy):
    print("You Won!")
else:
    print("The computer won!")
