"""
#file = open("Day 030/file.txt") --> FileNotFoundError

try:
    file = open("Day 030/file.txt") #FileNotFoundError
    a_dict = {"key":"value"}
    #print(a_dict["aaaaaaaaaaa"]) #KeyError
    print(a_dict["key"])

#is not recomended to have a generic except, is better to especify the exception
except FileNotFoundError:
    file = open("Day 030/file.txt", mode = "w")
    file.write("Something")

except KeyError as error_message:
    print(f"{error_message}:does not exist")
else:
    content = file.read()
    print(content)
finally:
    #file.close()
    #print("file was closed.")
    raise TypeError("i made up an error")
"""
"""
import random
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    fruit = fruits[index]
    print(fruit + "pie")

try:
    make_pie(4)
except IndexError as e:
    print(f"{e}: This pie does not exist")
    index = random.randint(0,2)
    make_pie(index)
finally:
    print("Here's your pie")

"""
"""
fruits = ["Apple", "Pear", "Orange"]
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + "pie")

make_pie(4)
"""