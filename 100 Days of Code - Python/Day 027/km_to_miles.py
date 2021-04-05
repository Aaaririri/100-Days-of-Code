import tkinter as tk
#create a window 
window = tk.Tk()
window.title("Kilometers do Miles")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)
#functions
def conversion():
    km = float(input.get())
    miles = km / 1.61
    my_label_miles.config(text=f"The value is equal to {miles:.2f} miles")
def conversion2():
    miles = float(input2.get())
    km = miles * 1.61
    my_label_km.config(text=f"The value is equal to {km:.2f} km")
#label 
my_label = tk.Label(text="Calculator", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=0)
#label km 
my_label2 = tk.Label(text="KM: ", font=("Arial", 12, "bold"))
my_label2.grid(column=0, row=2)
#convert button
button = tk.Button(text="Convert to miles", command=conversion)
button.grid(column=2, row=2)
#Entry
input = tk.Entry(width=10)
input.grid(column=1, row=2)
#label miles 
my_label_miles = tk.Label(text="The value is equal to 0 miles ", font=("Arial", 12, "bold"))
my_label_miles.grid(column=0, row=3)
#label miles 
my_label3 = tk.Label(text= "Miles: ", font=("Arial", 12, "bold"))
my_label3.grid(column=0, row=4)
#convert button2
button2 = tk.Button(text="Convert to kilometers", command=conversion2)
button2.grid(column=2, row=4)
#Entry
input2 = tk.Entry(width=10)
input2.grid(column=1, row=4)
#km
my_label_km = tk.Label(text="The value is equal to 0 km", font=("Arial", 12, "bold"))
my_label_km.grid(column=0, row=5)
window.mainloop()