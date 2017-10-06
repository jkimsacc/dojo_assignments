import random

def grade():
    for i in range (0, 11):
        num = random.randrange(60, 101)
        if num <= 100 and num > 89:
            print "Score:", num, ";", "Your grade is A"
        elif num <= 89 and num > 79:
            print "Score:", num, ";", "Your grade is B"
        elif num <= 79 and num > 69:
            print "Score:", num, ";", "Your grade is C"
        elif num <= 69 and num > 59:
            print "Score:", num, ";", "Your grade is D"
    print "End of the program, Bye!"

grade()
