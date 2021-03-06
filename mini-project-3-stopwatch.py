# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user41_Y4u2I0qspz_4.py

# template for "Stopwatch: The Game"

import simplegui

# define global variables

time = 0
wins = 0
stops = 0
is_stoped = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    #A:BC.D
    A = t // 600
    B = t // 10 % 60 // 10
    C = t // 10 % 60 % 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global is_stoped
    is_stoped = False
    timer.start()

def stop_handler():
    global print_win
    global stops, wins
    global is_stoped

    if not is_stoped:
        stops += 1
        if time % 10 == 0:
            wins += 1

    timer.stop()

    is_stoped = True


def reset_handler():
    global time
    timer.stop()
    time = 0


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1


# define draw handler
def draw_time(canvas):
    canvas.draw_text(format(time), (100, 100), 25, "White")
    canvas.draw_text(str(wins) + "/" + str(stops), (200, 20), 20, "Green")


# create frame
frame = simplegui.create_frame("Timer game", 300, 200)

frame.set_draw_handler(draw_time)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)

start_button = frame.add_button("Start", start_handler)
stop_button = frame.add_button("Stop", stop_handler)
reset_button = frame.add_button("Reset", reset_handler)


# start frame
frame.start()

# Please remember to review the grading rubric
