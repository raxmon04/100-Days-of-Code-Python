from tkinter import Tk, Label, Button, Entry

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx = 100, pady= 200)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)





window.mainloop()

# # Add any amount of Numbers and Calculate the sum
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return(sum)

# print(add(3, 5, 6, 2, 1, 7, 4, 3))

# # Add any kind of argument (like add) and use them
# def calculate(n, **kwargs):
#     for key, value in kwargs.items():
#         n += kwargs["add"]
#         n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)

# # Create a Class with inifite keyword arguments
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#         self.seats = kw.get("seats")

# mycar = Car(make="Nissan", colour="black", seats="4")
# print(mycar.model, mycar.colour, mycar.seats)