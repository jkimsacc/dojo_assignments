# example = [1, 200, 3, 400, "some", "random long ass string longer than 50 characters just for testing", ["small","list"], ["big", "list", 1, 2, 3, 4, 5, 6, 7, 8]]
# print example
for x in example:
    if type(x) == int:
        if x >= 100:
            print "Thant's a big number!"
        else:
            print "That's a small number"
    if type(x) == str:
        if len(x) >= 50:
            print "Long sentence"
        else:
            print "Short sentence"
    if type(x) == list:
        if len(x) >= 10:
            print "Big list!"
        else:
            print "Short list."
