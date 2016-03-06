slow_wumpuses = 1000
fast_wumpuses = 1
year = 1

while slow_wumpuses > fast_wumpuses:
    year += 1
    slow_wumpuses *= (2 * 0.6)
    fast_wumpuses *= (2 * 0.7)
    print "Year: %s. %s slow wumpuses, %s fast wumpuses." % (
        str(year), str(slow_wumpuses), str(fast_wumpuses))
