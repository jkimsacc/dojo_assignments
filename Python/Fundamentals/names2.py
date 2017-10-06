students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Part 1

def display(dic):
    for i in range (0, 4):
        print students[i]['first_name'], students[i]['last_name']

display(students)

# Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def display2(dic):
    for i in range(0, len(dic.keys())):
        print dic.keys()[i]
        for j in range(0, len(dic[dic.keys()[i]])):
            print j+1, "-", dic[dic.keys()[i]][j]['first_name'], dic[dic.keys()[i]][j]['last_name'], "-", len(dic[dic.keys()[i]][j]['first_name']) + len(dic[dic.keys()[i]][j]['last_name'])

display2(users)
