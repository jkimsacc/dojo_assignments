#   1. declare number of results
#   2. for loop 5000 times
#   3. generate random numbers
#   4. count the results
#   5. print results

import random

def cointoss():
    head = 0
    tail = 0
    for i in range(1, 5001):
        result = round(random.random())
        if result == 1:
            head += 1
            print "Attempt #", i, "Throwing a coin... It's a head! ... Got", head, "head(s) so far and", tail, "tail(s) so far"
        else:
            tail += 1
            print "Attempt #", i, "Throwing a coin... It's a tail! ... Got", head, "head(s) so far and", tail, "tail(s) so far"

cointoss()
