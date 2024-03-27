# first_name = input('What\'s your first name?')
# dist_in_kilometers = input('How far away are you?')

# converted = float(dist_in_kilometers) / 1.609

# greeting = 'Nice to see you ' + first_name.capitalize() + ', you are ' + str(round(converted, 1)) + ' miles from me.'
# print(greeting)

murray_family = ['Thad', 'Linda', 'Justice', 'TJ']
print(murray_family)

print(murray_family[1])
print(murray_family[:2])

print(len(murray_family))
print(murray_family.count('Linda'))

murray_family.sort() #Descending Order

print(murray_family)

murray_family.sort(reverse=True) #Ascending Order

print(murray_family)

murray_family.reverse() # this function reverses the list as it was originally ordered -- not ascending or descending

print(murray_family)

#NOTE: .sort() functions change the list in-place, mutating it; it does not create a new list


cars = [911,130,328,535,740,308]

print(min(cars)) # min() returned the lowest value in the list of numbers

print(max(cars)) # max() gets the highest value

print(sum(cars)) # sum() will add up all the values, like .reduce() in JS

murray_family.append('Neighbor John') # .append adds a new value to the end of the list

murray_family.insert(0, 'Neighbor John')

murray_family[2] = 'Jorge' ## inserting will change a list at the specific postion

# print(murray_family)

# murray_family.extend(cars) # .extend() will append the list passed as an arugment onto the list being appended to

# print(murray_family)

# murray_family.remove('TJ') # .remove lets you completly remove a specified element/s

# murray_family.pop() # .pop() by default removes the last name in the array and also commits that name to memory

# test_var = murray_family.pop(2) #shows how you can assign the popped value to a variable; can also use the value to pop, not just the index

# murray_family.clear() #clears the whole list, leaves behind an empty list

# del friends # this will completely delete/destroy the list
# del frinds[2] # can also specifiy which parts of the list to delete

# print(murray_family) 

# print(test_var)

new_murry_family = murray_family[:] # this will copy the the list into a new list

print(new_murry_family)


