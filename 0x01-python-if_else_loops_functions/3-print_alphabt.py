#!/usr/bin/python3
for value in range(97, 123):
    if value != 102 or value != 113:
        print("{}".format(chr(value)), end="")
