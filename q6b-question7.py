n = 1000
numbers = []

i = 2
while i < n:
    numbers.append(i)
    i += 1

result = []

while len(numbers) != 0:
    result.append(numbers[0])
    new_numbers = []
    print "NUMBERS = " + str(numbers) + "\n" + "-" * 10 + "\n"

    for n in numbers:
        print "n = " + str(n) + ", numbers = " + str (numbers) + ", result = " + str(result)
        if n % numbers[0] != 0:
            new_numbers.append(n)
        else:
            pass
    numbers = new_numbers

print len(result)
