# my implementation of card game - Memory
# http://www.codeskulptor.org/#user41_bVztEavPj4_7.py

import simplegui
import random

# helper function to initialize globals
def new_game():
    global numbers_list, state, exposed, turns

    exposed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]

    click1_index = None
    click2_index = None

    turns = 0
    label_text = "Turns = " + str(turns)
    label.set_text(label_text)

    state = 0

    simple_list = [i for i in range(8)]
    print simple_list

    numbers_list = []

    numbers_list.extend(simple_list)
    numbers_list.extend(simple_list)

    random.shuffle(numbers_list)

# define event handlers
def mouseclick(pos):
    global state, click1_index, click2_index, turns

    clicked_index = pos[0] // 50

    if state == 0:
        if exposed[clicked_index] == False:
            exposed[clicked_index] = True
            click1_index = clicked_index
            state = 1

    elif state == 1:
        if exposed[clicked_index] == False:
            exposed[clicked_index] = True
            click2_index = clicked_index

            turns += 1
            label_text = "Turns = " + str(turns)
            label.set_text(label_text)

            state = 2

    else: # state == 2
        if exposed[clicked_index] == False:

            # what to do with the cards: flip or not
            # if the cards have the same value, leave them opened
            if numbers_list[click1_index] == numbers_list[click2_index]:
                exposed[click1_index] = True
                exposed[click2_index] = True

                click1_index = clicked_index
                exposed[clicked_index] = True

                state = 1
            # if the cards don't have the same value, flip them
            else:
                exposed[click1_index] = False
                exposed[click2_index] = False

                click1_index = clicked_index
                exposed[clicked_index] = True

                state = 1

# cards are logically 50x100 pixels in size
def draw(canvas):

    number_lower_left_coordinate = 13
    rectangle_x_coordinate = 0

    for index, number in enumerate(numbers_list):
        if exposed[index] == False:
            canvas.draw_polygon([[rectangle_x_coordinate, 0], [rectangle_x_coordinate + 50, 0], [rectangle_x_coordinate + 50, 100], [rectangle_x_coordinate, 100]], 1, "Black", "Green")
        else:
            canvas.draw_text(str(number), (number_lower_left_coordinate, 70), 50, "White")
        number_lower_left_coordinate += 50
        rectangle_x_coordinate += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
