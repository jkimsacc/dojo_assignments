# create function that counts # of denominators except 1 and itself
# : for loop from 2 to n-1 : range(2,n)
# : if # of denominators are 0 its prime
# : if # of denominators are odd number its squre



def foobar(n):
    denominator = 0
    for num in range(2, n):
        if n % num == 0:
            denominator += 1
    if denominator == 0:
        print n, "foo"
    elif denominator % 2 == 1:
        print n, "bar"
    else:
        print n, "foobar"

for i in range(100, 100001):
    foobar(i)





# n = 7
# for num in range(2, n):
#     print num, n
