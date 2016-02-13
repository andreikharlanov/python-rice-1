# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user41_JNlI9IshBy_0.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_radius = 20

score1, score2 = 0, 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH / 2, HEIGHT / 2]

    if direction is True:
        ball_vel = [random.randrange(120, 240) / 60, - random.randrange(60, 180) / 60]
    else:
        ball_vel = [- random.randrange(120, 240) / 60, - random.randrange(60, 180) / 60]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT / 2]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2]

    direction = random.randrange(0, 2)
    if direction == 0:
        spawn_ball(LEFT)
    if direction == 1:
        spawn_ball(RIGHT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel


    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1] <= 0 + ball_radius: # ceiling
        ball_vel[1] = - ball_vel[1]

    elif ball_pos[1] >= HEIGHT - ball_radius: # floor
        ball_vel[1] = - ball_vel[1]

    elif ball_pos[0] >= WIDTH - PAD_WIDTH - ball_radius: # right wall
        score1 += 1
        print score1, score2
        spawn_ball(LEFT)

    elif ball_pos[0] <= PAD_WIDTH + ball_radius: # left wall
        score2 += 1
        print score1, score2
        spawn_ball(RIGHT)

    else:
        pass


    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 2, "Red")

    # update paddle's vertical position, keep paddle on the screen

    # draw paddles

    # left paddle
    canvas.draw_polygon([
        [0, paddle1_pos[1] - HALF_PAD_HEIGHT],
        [PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT],
        [PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
        [0, paddle1_pos[1] + HALF_PAD_HEIGHT]],
        2,
        "Red",
        "Red")

    # right paddle
    canvas.draw_polygon([
        [WIDTH - PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT],
        [WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT],
        [WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
        [WIDTH - PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT]],
        2,
        "Red",
        "Red")

    # determine whether paddle and ball collide

    # draw scores

def keydown(key):
    global paddle1_vel, paddle2_vel

def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button("Restart", new_game)

# start frame
new_game()
frame.start()
