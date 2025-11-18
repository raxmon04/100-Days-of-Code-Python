from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ============================ CONSTANTS ============================ #
WHITE = "#ffffff"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(letters) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("/mnt/d/Git/python/029_PasswordManager/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_image = PhotoImage(file="/mnt/d/Git/python/029_PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:", bg=WHITE)
username_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=WHITE)
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=48)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=48)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ramon.peter@css.ch")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
generate_password_button = Button(text="Generate Password", bg=WHITE, command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", bg=WHITE, width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

