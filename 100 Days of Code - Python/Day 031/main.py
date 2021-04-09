from tkinter import Tk, PhotoImage, Canvas, Button
import pandas 
import random 

BACKGROUND_COLOR = "#B1DDC6"

#reading data 
data = pandas.read_csv("Day 031/data/french_words.csv")
data_dict = {row.French: row.English for (index, row) in data.iterrows()}
data_list = [row.French for index, row in data.iterrows()]

word = random.choice(data_list)
timer = None
counter = 5

# if you know the translation it removes from the list of words so you dont repet that word 
def add_front_card_right():
    global word
    if data_list != []: 
        data_list.remove(word)
    add_front_card()

def add_front_card_wrong():
    add_front_card()
    
# update data on the screen and stats the variables for the timer
def add_front_card():
    if data_list != []:
        global word
        global counter
        word = random.choice(data_list)
        show.create_image(400, 262, image = front_img)
        show.grid(row = 0, column = 0, columnspan = 2)
        show.create_text(400, 150, text = "French", font = ("Arial", 40, "italic"))
        show.create_text(400, 263, text = word, font = ("Arial", 60, "bold"))
        reset()
        run_timer(counter)
    else:
        reset()
        show.create_image(400, 262, image = front_img)
        show.grid(row = 0, column = 0, columnspan = 2)
        show.create_text(400, 150, text = "END", font = ("Arial", 40, "italic"))
        show.create_text(400, 263, text = "CONGRATULATIONS", font = ("Arial", 55, "bold"))

#resets the timer and the counter 
def reset():
    global timer
    window.after_cancel(timer)

# count the time
def run_timer(counter): 
    global timer
    if counter > 0:
        timer = window.after(1000, run_timer, counter - 1)
    else:
        add_back_card()

#update the back of the card displaying into the window
def add_back_card():
    show.create_image(400, 262, image = back_img)
    show.grid(row = 0, column = 0, columnspan = 2)
    show.create_text(400, 150, text = "English", font = ("Arial", 40, "italic"))
    show.create_text(400, 263, text = data_dict[word], font = ("Arial", 60, "bold"))
    

#creating window
window = Tk()
window.title("Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

#loading images
right_img = PhotoImage(file = "Day 031/images/right.png")
wrong_img = PhotoImage(file = "Day 031/images/wrong.png")
front_img = PhotoImage(file = "Day 031/images/card_front.png")
back_img = PhotoImage(file = "Day 031/images/card_back.png")

#setting the card images
show = Canvas(width = 800, height = 525, bg = BACKGROUND_COLOR, highlightthickness = 0)
show.create_image(400, 262, image = front_img)
show.grid(row = 0, column = 0, columnspan = 2)
show.create_text(400, 150, text = "French", font = ("Arial", 40, "italic"))
show.create_text(400, 263, text = word, font = ("Arial", 60, "bold"))
run_timer(counter)#if you dont star the timer you can't reset to restart the time counting


#adding buttons
wrong_button = Button(image = wrong_img, highlightthickness = 0)
wrong_button.config(command = add_front_card_wrong)
wrong_button.grid(row = 1, column = 0)

right_button = Button(image = right_img, highlightthickness = 0)
right_button.config(command = add_front_card_right)
right_button.grid(row = 1, column = 1)



window.mainloop()
