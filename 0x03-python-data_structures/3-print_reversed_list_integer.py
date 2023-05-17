#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_length = len(my_list)
    for i in range(list_length - 1, -1, -1):
        print("{}".format(my_list[i]))

# Test
my_list = [10, 22, 30, 44, 50]
print_reversed_list_integer(my_list)
