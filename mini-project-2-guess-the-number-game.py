# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# http://www.codeskulptor.org/#user41_7nhiRwmDpFKWLzZ_0.py

import simplegui
import random

# helper function to start and restart the game

range = 100
remaining_guesses = 7

def new_game():
    global remaining_guesses
    global secret_number
    global range

    print "\nNew game started."
    print "Range is [0, %d)" % range
    print "You have %d remaining guesses." % remaining_guesses

    secret_number = random.randrange(0, int(range))
    # print secret number for testing
    # print "Secret number is:", secret_number

# define event handlers for control panel
def range100():
    global range
    global remaining_guesses

    range = 100
    remaining_guesses = 7

    new_game()

def range1000():
    global range
    global remaining_guesses

    range = 1000
    remaining_guesses = 10

    new_game()

def input_guess(guess):
    global remaining_guesses

    remaining_guesses -= 1

    print "\nGuess was", int(guess)

    if secret_number < int(guess):
        print "Lower"
        print "\nYou have %d remaining guesses." % remaining_guesses
    elif secret_number > int(guess):
        print "Higher"
        print "\nYou have %d remaining guesses." % remaining_guesses
    else:
        print "Correct"
        if range == 100:
            remaining_guesses = 7
        elif range == 1000:
            remaining_guesses = 10
        new_game()

    if remaining_guesses == 0:
        if range == 100:
            remaining_guesses = 7
        elif range == 1000:
            remaining_guesses = 10
        new_game()

def restart_button():
    global range
    global remaining_guesses

    if range == 100:
        remaining_guesses = 7
    elif range == 1000:
        remaining_guesses = 10
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
