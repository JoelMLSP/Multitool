from tkinter import *

def convert():
    value = float(user_input.get()) * 1.60934
    con_value.config(text=f"{value:.2f}")

def show_converter():
    menu_frame.pack_forget()
    converter_frame.pack()

def show_menu():
    converter_frame.pack_forget()
    menu_frame.pack()

# Main window
window = Tk()
window.title("multitool")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Menu Frame
menu_frame = Frame(window)
menu_frame.pack()

menu_label = Label(menu_frame, text="Multitool", font=("Arial", 16))
menu_label.pack(pady=20)

convert_button = Button(menu_frame, text="miles to km converter", command=show_converter)
convert_button.pack(pady=10)

# Converter Frame
converter_frame = Frame(window)

is_equal = Label(converter_frame, text="is equal to")
is_equal.grid(column=0, row=1)

km = Label(converter_frame, text="Km")
km.grid(column=2, row=1)

miles = Label(converter_frame, text="Miles")
miles.grid(column=2, row=0)

con_value = Label(converter_frame, text="0")
con_value.grid(column=1, row=1)

calculate_button = Button(converter_frame, text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

user_input = Entry(converter_frame)
user_input.grid(column=1, row=0)
user_input.config(width=10)

back_button = Button(converter_frame, text="Back to Menu", command=show_menu)
back_button.grid(column=0, row=3, columnspan=3, pady=10)

# Start with the menu
show_menu()

mainloop()