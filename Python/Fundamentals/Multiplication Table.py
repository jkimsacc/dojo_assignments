x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# second list = [2, 4, 6, ... x[index]*x]
global new = []

for i in range (1, len(x)):
    for n in range (1, len(x)):
        new[i] = n * x[i]
        print new
