def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didn't provide valid inputs."
    name = f_name + " " + l_name
    name = name.title() #returns a version of the string where each word is title case
    return name
'''
def format_name2(f_name, l_name):
    format_f = f_name.title()
    format_l = l_name.title()
    print(f"{format_f} {format_l}")
'''

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Your full name is: {format_name(first_name, last_name)}")