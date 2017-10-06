def printrow(n):
    x = [1 * n, 2 * n, 3 * n, 4* n, 5 * n, 6* n, 7*n, 8*n, 9*n, 10*n, 11*n, 12*n]
    return x

def list2table(arr):
    print arr[0], arr[1], arr[2], arr[3], arr[4], arr[5], arr[6], arr[7], arr[8], arr[9], arr[10], arr[11]

for n in range(1, 13):
    list2table(printrow(n))
