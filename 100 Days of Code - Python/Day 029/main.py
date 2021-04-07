from tkinter import *
from tkinter import messagebox
import random
NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
UPLOW = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m",
         "Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
ESPECIAL = ["!","@","#","$","%","&","*","(",")"]
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    nl = random.randint(8,10)
    nn = random.randint(2,4)
    ne = random.randint(2,4)
    new_password = []
    password = ""
    for _ in range(nl):
        new_password.append(random.choice(UPLOW))
    for _ in range(nn):
        new_password.append(random.choice(NUMBERS))
    for _ in range(ne):
        new_password.append(random.choice(ESPECIAL))

    random.shuffle(new_password)
    for i in new_password:
        password += i
    password_text.insert(0, password) 
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    site = website_text.get()
    user = username_text.get()
    password = password_text.get()
    if messagebox.askokcancel(title = "Save", message = f"{site} | {user} | {password} \n Is this data right?") == True:
        if site != "" and user != "" and password != "":
            with open("Day 029/password_manager.txt", mode = "a") as file:
                file.write(f"{site} | {user} | {password} \n")
                website_text.delete(0, END)
                username_text.delete(0, END)
                username_text.insert(0, "@gmail.com")
                password_text.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)
canvas = Canvas(height = 200, width = 200)
logo_img = PhotoImage(file = "Day 029/logo.png")
canvas.create_image(100, 100, image = logo_img)
canvas.grid(row = 0, column = 1)
#website
website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)
website_text = Entry(width = 40)
website_text.grid(row = 1, column = 1, columnspan = 2)
website_text.focus()
#username
username_label = Label(text = "Email/Username:")
username_label.grid(row = 2, column = 0)
username_text = Entry(width = 40)
username_text.insert(0, "@gmail.com")
username_text.grid(row = 2, column = 1, columnspan = 2)
#password
password_label = Label(text = "Password:")
password_label.grid(row = 3, column = 0)
password_text = Entry(width = 22)
password_text.grid(row = 3, column = 1)
password_button = Button(text= "Generate password", command = generate)
password_button.grid(row = 3, column = 2)
#add
add_button = Button(text = "Add", command = add_info)
add_button.grid(row = 4, column = 1, columnspan = 2)






window.mainloop()