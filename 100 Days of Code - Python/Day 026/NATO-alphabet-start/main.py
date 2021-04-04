import pandas as pd
with open("Day 026/NATO-alphabet-start/nato_phonetic_alphabet.csv") as file:
    file = file.readlines()
file.pop(0)

new_file = {}
for obj in file:
    list_obj = obj.strip("\n").split(",")
    new_file[list_obj[0]] = list_obj[-1]

name = input("name that you want to put in NATO: ").upper()
NATO = ""
for word in name:
    if word in new_file:
        NATO += new_file[word] + " "

print(NATO)




