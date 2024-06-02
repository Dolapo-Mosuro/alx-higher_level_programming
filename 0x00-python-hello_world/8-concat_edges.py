#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
<<<<<<< HEAD
        language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
=======
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[-23:-17] + str[:6]
>>>>>>> bda00abe17b898a4383bb8c45a40dea1d7eee93e
print(str)
