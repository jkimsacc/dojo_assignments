#       Multiples
for x in range(0,1000):
    if x % 2 == 1: #    check if x is odd number
        print x

for y in range(0, 1000000):
    if y % 5 == 0: #    check if x is multiples of 5
        print y

#       Sum List
a = [1, 2, 5, 10, 255, 3]

# print a[0]

print sum(a)  #     add all elements from a List

print sum(a) / len(a)  # average is sum / # of elements
