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