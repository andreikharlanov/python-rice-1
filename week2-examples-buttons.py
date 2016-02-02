# calculator with all buttons
import simplegui

# intialize globals
store = 12
operand = 3

# event handlers for calculator with a store and operand

def output():
    """prints contents of store and operand"""
    print "Store = ", store
    print "Operand = ", operand
    print ""

def swap():
    """ swap contents of store and operand"""
    global store, operand
    store, operand = operand, store
    output()

def add():
    """ add operand to store"""
    global store
    store = store + operand
    output()

def sub():
    """ subtract operand from store"""
    global store
    store = store - operand
    output()

def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()


# create frame
frame = simplegui.create_frame("Calculator", 300, 300)

# register event handlers
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)


# get frame rolling
frame.start()
