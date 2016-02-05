import simplegui

# global state

current = 217
list_of_generated_numbers = [current]

def update():
    global current
    if current == 1:
        print "\nThe list of genereted numbers is:", list_of_generated_numbers
        print "Maximum number was: ", max(list_of_generated_numbers)
        timer.stop()
    elif current % 2 == 0:
        current = current / 2
        list_of_generated_numbers.append(current)
        print current
    else:
        current = current * 3 + 1
        list_of_generated_numbers.append(current)
        print current

timer = simplegui.create_timer(1, update)

timer.start()
