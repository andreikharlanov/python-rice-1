# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# http://www.codeskulptor.org/#user41_P8vFTOWn4gbjoIo.py

import simplegui
import random

# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(0, 100)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game


    # remove this when you add your code
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game

    pass

def input_guess(guess):
    print "Guess was", int(guess)
    if int(guess) < secret_number:
        print "Lower"
    elif int(guess) > secret_number:
        print "Higher"
    else:
        print "Correct"



# create frame

frame = simplegui.create_frame("Guess the number", 300, 200)

# register event handlers for control elements and start frame

inp_guess = frame.add_input("Guess", input_guess, 50)

frame.start()

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
