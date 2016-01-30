# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game

    # remove this when you add your code
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game

    pass

def input_guess(guess):
    # main game logic goes here

    # remove this when you add your code
    pass



# create frame

frame = simplegui.create_frame("Guess the number", 300, 200)

# register event handlers for control elements and start frame

inp_guess = frame.add_input("Guess", input_guess, 50)

frame.start()

# call new_game
new_game()


# always remember to check your completed program against the grading rubric
