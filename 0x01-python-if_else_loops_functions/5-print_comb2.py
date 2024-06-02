#!/usr/bin/python3
<<<<<<< HEAD
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
=======
for i in range(0, 100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
>>>>>>> bda00abe17b898a4383bb8c45a40dea1d7eee93e
