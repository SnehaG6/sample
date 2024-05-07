My_string = input("Enter the string: ")

mid_value = int(len(My_string) / 2)

if len(My_string) % 2 == 0:  # even
    first_string = My_string[:mid_value]
    second_string = My_string[mid_value:]
else:  # odd
    first_string = My_string[:mid_value]
    second_string = My_string[mid_value + 1:]

# condition to symmetric
if first_string == second_string:
    print(My_string, 'Entered string is symmertical')
else:
    print(My_string, 'Entered string is not symmertical')

# condition to check palindrome
if first_string == second_string[::-1]:  # you can also use ''.join(reversed(second_str)) [slower]
    print(My_string, 'Entered string is palindrome')
else:
    print(My_string, 'Entered string is not palindrome')