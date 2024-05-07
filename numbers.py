num_1 = 10  # int
num_2 = 5.0  # float
num_3 = 10j  # complex

print("Initial type of", num_1, "is", type(num_1))
print("Initial type of", num_2, "is", type(num_2))
print("Initial type of", num_3, "is", type(num_3))

# convert from int to float:
updated_num_1 = float(num_1)

# convert from float to int:
updated_num_2 = int(num_2)

# convert from complex to int:
updated_num_3 = complex(num_3)

print("Updated type of num_1 is", type(updated_num_1))
print("Updated type of num_2 is", type(updated_num_2))
print("Updated type of num_3 is", type(updated_num_3))
print("Updated Numbers: ", updated_num_1, updated_num_2, updated_num_3)