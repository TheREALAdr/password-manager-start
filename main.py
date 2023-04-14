from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_list = []
    password_entry.delete(0, END)
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    email_and_user = email_and_user_entry.get()
    password = password_entry.get()
    saved_password_info = {
        website: {"email_and_user":
                      email_and_user,
                  "password": password,
                  }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="HEY!",
                               message="At least one of your columns is empty or hasn't been filled with sufficient "
                                       "data. "
                                       "Please fill all "
                                       "boxes before proceeding.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", mode="w") as data_file:
                json.dump(saved_password_info, data_file, indent=4)
        else:
            data.update(saved_password_info)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

# ---------------------- SEARCH FOR PASSWORD -------------------------- #

def find_password():
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = open("data.json", mode="w"):
            data.close()
            # Add error message here!!!
        else:
            list_of_json_items = data.values()
            # Code used for testing how to loop through data.values()
#             for item in list_of_json_items:
#                 print(item['name'], item['password'])          
            for item in list_of_json_items:
            # Testing try catch (MIGHT NOT WORK, NEED TO TEST IN AN ENVIRONMENT!!!)
#                 try:
#                     if website_entry.get() == list_of_json_items[website_entry.get()]:
#                         old_website_name == website_entry.get()
#   
                if website_entry.get() == str(v[item]):  
                    messagebox.showinfo(title="Website already in database", message=f"Website: {str(item)}\n" 
                                             f" Password: {str(item["password"]}")
#     

#
           





# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200, highlightthickness=0, )
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# Text

website_text = Label(text="Website:")
website_text.grid(column=0, row=1, sticky=EW)
email_and_user_text = Label(text="Email/Username:")
email_and_user_text.grid(column=0, row=2, sticky=EW)
password_text = Label(text="Password:")
password_text.grid(column=0, row=3, sticky=EW)

# Entries

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, sticky=EW)
website_entry.focus()
email_and_user_entry = Entry(width=52)
email_and_user_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
email_and_user_entry.insert(0, "example@domain.com")
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3, sticky=EW)

# Buttons

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky=EW)
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3, sticky=EW)
add_button = Button(width=52, text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky=EW)

window.mainloop()
