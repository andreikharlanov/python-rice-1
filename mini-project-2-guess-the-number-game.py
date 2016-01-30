# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# http://www.codeskulptor.org/#user41_P8vFTOWn4gbjoIo.py

import simplegui
import random

# helper function to start and restart the game

range = 100

def new_game():
    global secret_number
    global range

    print "New game started."
    print "Range is [0, %d)" % range

    secret_number = random.randrange(0, int(range))
    # print secret number for testing
    print "Secret number is:", secret_number

# define event handlers for control panel
def range100():
    global range
    range = 100
    new_game()

def range1000():
    global range
    range = 1000
    new_game()

def input_guess(guess):
    print "Guess was", int(guess)
    if int(guess) < secret_number:
        print "Lower"
    elif int(guess) > secret_number:
        print "Higher"
    else:
        print "Correct"

def restart_button():
    new_game()

# create frame

frame = simplegui.create_frame("Guess the number", 300, 200)

# register event handlers for control elements and start frame

inp_guess = frame.add_input("Guess", input_guess, 50)

frame.add_button("Restart game", restart_button)
frame.add_button("Range is [0,100)", range100)
frame.add_button("Range is [0,1000)", range1000)

frame.start()

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
