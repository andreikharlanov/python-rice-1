n = 123

# 123 % 100 = 23; 123 % 10 = 3; 23 - 3 = 20; 20 / 10 = 2
print (n % 100 - n % 10) / 10

# 123 - 3 = 120; 120 % 100 = 20; 20 / 10 = 2
print ((n - n % 10) % 100) / 10

# 123 % 10 = 3; 3 / 10 = 0.3
print (n % 10) / 10
