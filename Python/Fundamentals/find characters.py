word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newlist = []
randomword = 'hahaha'
#
# print randomword.count('a')
# print randomword.count('o')

def findcharacters(list, character):
    for index in range(0, len(list)):
        if list[index].count(character) != 0:
            newlist.append(list[index])
    print newlist



findcharacters(word_list, char)
