same_one = [1,2,3,4]
same_two = [1,2,3,4]

diff_one = ['one', 'two', 'three']
diff_two = ['one', 'two', 'four']

difflen_one = [0, 0, 0, 0]
difflen_two = [0, 0, 0]

def compare(list_one, list_two):
    if list_one == list_two:
        print 'identical'
    else:
        print 'not'




compare(same_one, same_two)
compare(diff_one, diff_two)
compare(difflen_one, difflen_two)
