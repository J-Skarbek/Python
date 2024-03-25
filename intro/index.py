msg='welcome to Python 101: Strings'
print(msg, msg)
print(msg.upper())
print(msg.lower())

print(msg.capitalize())
      
print(msg.title())

print(len(msg)) #measure lenght of string

print(msg.count('Python')) #this command is case sensitive

string_to_slice = 'We\'re going to be splicing this string up!'

print(string_to_slice[-1])

welcome_statement = msg[18] + ' ' + msg[0:7] + ' Ring to Tyler'
print(welcome_statement.title())

reverse_statement = welcome_statement[::-1]
print(reverse_statement)

multiline = """Hello,
this is a mulitline string
and it requires the triple-quotes!"""

print(multiline)

print(msg)

replaced_msg = msg.replace('Python', 'DingDongs')

print(replaced_msg)

print('Python' in msg) #will check for the string within the msg string

print('Python' not in msg) #will check for the string to not exist within the msg string


name='TERRY'
color = 'RED'
example1 = '[' + name + '] loves the color ' + color + '!'
example2 = f'[{name}] loves the color {color.lower()}!'
print(example1)
print(example2)