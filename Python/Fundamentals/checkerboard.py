row1 = " " + "*"
row2 = "*" + " "

for i in range (0, 10):
    if i % 2 == 1:
        print row1 * 5
    else:
        print row2 * 5
