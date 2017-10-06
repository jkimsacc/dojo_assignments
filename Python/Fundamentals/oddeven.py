def oddeven():
    for i in range (0, 2001):
        if i % 2 == 1:
            print "Number is", i, ". This is an odd number."
        else:
            print "Number is", i, ". This is an even number."

oddeven()

def multiply(arr, n):
    print arr, n
    for i in range(len(arr)):
        print i
        arr[i] = n *arr[i]
    return arr


a = [2,4,10,16]
b = multiply(a, 5)
print b

def layered_multiples(arr):
    for i in range(len(arr)):
        print i
        arr[i] = [1] * arr[i]
    return arr

x = layered_multiples(multiply([2,4,5],3))
print x

#[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
# is [1]*6, [1]*12, [1]*15
