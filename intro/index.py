first_name = input('What\'s your first name?')
dist_in_kilometers = input('How far away are you?')

converted = float(dist_in_kilometers) / 1.609

greeting = 'Nice to see you ' + first_name.capitalize() + ', you are ' + str(round(converted, 1)) + ' miles from me.'
print(greeting)
