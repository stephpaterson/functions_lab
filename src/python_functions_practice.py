import calendar

# Test return 10
def return_10():
    return 10

# Test add
def add(num_1, num_2):
    return num_1 + num_2

# Test subract
def subtract(num_1, num_2):
    return num_1 - num_2

# Test multiply
def multiply(num_1, num_2):
    return num_1 * num_2

# Test divide
def divide(num_1, num_2):
    return num_1 / num_2

# Length of string
def length_of_string(string):
    return len(string)

# Join string
def join_string(string_1, string_2):
    return string_1 + string_2

# Add string as a number
def add_string_as_number(str_num_1, str_num_2):
    num_1 = int(str_num_1)
    num_2 = int(str_num_2)
    return num_1 + num_2

# Month names
def number_to_full_month_name(number):
    my_month = calendar.month_name[number]
    return my_month

# Month short names
def number_to_short_month_name(number):
    my_month = calendar.month_abbr[number]
    return my_month

# Volume cubed
def cube_volume(side_length):
    volume_cube = side_length ** 3
    return volume_cube

# Reverse String
def reverse_string(a_string):
    return a_string[::-1]

# Convert farenheit to celcius - this passes the test but 
# I would want to consider improving this to account for decimal places
def farenheit_to_celsius(farenheit_value):
    celsius_value = (farenheit_value - 32)/1.8
    return celsius_value