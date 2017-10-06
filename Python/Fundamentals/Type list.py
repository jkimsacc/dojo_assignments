l = ['magical unicorns',19,'hello',98.98,'world']
concatenatedstr = ""
sumofint = 0


for x in l:
    if type(x) == str: # check if its string
        concatenatedstr += " " + x #add to string
    elif type(x) == int: # check if interger
        sumofint += x # check if interger
if concatenatedstr != "" and sumofint != 0:
    print "The list you entered is of mixed type"

print "String:" + concatenatedstr
print "Sum:", sumofint
