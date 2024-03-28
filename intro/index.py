# msg ='Welcome to Python 101: Split and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(csv.split(','), type(csv.split(',')))

# print(str(friends_list))

# print('-'.join(friends_list), type('-'.join(friends_list)))

# print(''.join(msg.split()))

# print(msg.replace(' ', ''))


# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# friends_list = ['Exercise: fill me with names']
# print(friends_list)

# csv = csv.replace(':', ',')
# csv = csv.replace(';', ',')
# print(csv.split(','), type (csv.split(',')))

# #can also chain the functions like this:

# print(csv.replace(';', ',').replace(':', ',').split(','))

########

#Tuples - faster Lists you can't change
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends[2])
print(friends_tuple[2:3])
