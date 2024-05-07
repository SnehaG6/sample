 # a list of three elements
ages = [19, 26, 29]
print(ages)

#slicing in list
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

#Remove a item from a list
numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers)


#Add Elements to a List From Other Iterables

colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# changing the third item to 'Blue'
colors[2] = 'Blue'

print('Updated List:', colors)