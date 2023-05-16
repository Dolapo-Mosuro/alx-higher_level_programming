0x03. Python - Data Structures: Lists, Tuples

Requirements

Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc

Tasks
0. Print a list of integers

Write a function that prints all integers of a list.

1. Secure access to an element in a list

Write a function that retrieves an element from a list like in C

2. Replace element

Write a function that replaces an element of a list at a specific position (like in C).

3. Print a list of integers... in reverse!

Write a function that prints all integers of a list, in reverse order.

4. Replace in a copy

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

5. Can you C me now?

Write a function that removes all characters c and C from a string.

6. Lists of lists = Matrix

Write a function that prints a matrix of integers.

7. Tuples addition
mandatory
Write a function that adds 2 tuples.

8. More returns!
mandatory
Write a function that returns a tuple with the length of a string and its first character

9. Find the max**
  * [9-max_integer.py](./9-max_integer.py): Python function that finds the biggest integer
  of a list.
  * If the list is empty, the function returns `None`.
  * Without importing modules or using the builtin `max()`.

10. Only by 2**
  * [10-divisible_by_2.py](./10-divisible_by_2.py): Python function that finds all multiples
  of 2 in a list.  * Returns a new list of the same size. Each element of the new
  list contains either `True` or `False` corresponding to whether the integer at
  the same position in the original list is a multiple of 2.
  * Without importing modules.

11. Delete at**
  * [11-delete_at.py](./11-delete_at.py): Python function that deletes an item at
  a specific position in a list.
  * If `idx` is negative or out of range (greater than the number of elements in
  `my_list`), the function returns the original list.
  * Without imporitng modules or using `pop()`.

12. Switch**
  * [12-switch.py](./12-switch.py): Python program that switches the values of
  variable `a` and `b`.
  * Completion of [this source code](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py).

13. Linked list palindrome**
  * [13-is_palindrome.c](./13-is_palindrome.c): C function that checks if a
  singly-linked list is a palindrome.
  * If the function is not a palindrome - returns `0`.
  * If the function is a palindrome - returns `1`.
  * An empty list is considered a palindrome.
  * Helper files:
    * [linked_lists.c](./linked_lists.c): C functions handling linked lists for
    testing [13-is_palindrome.c](./13-is_palindrome.c) (provided by Holberton School).
 [lists.h](./lists.h): Header file containing definitions and prototypes for all types
    and functions used in [linked_lists.c](./linked_lists.c) and
    [13-insert_number.c](./13-insert_number.c).

14. CPython #0: Python lists**

[100-print_python_list_info.c](./100-print_python_list_info.c): C function that
  prints basic information about Python lists.
