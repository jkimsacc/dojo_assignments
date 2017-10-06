# for loop arr index
# convert number to '*'* numbers
# profit

# check if i is interger

def draw_stars(arr):
    for i in arr:
        if type(i) == int:
            print "*" * i
        elif type(i) == str:
            print i[0].lower() * len(i)






x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
