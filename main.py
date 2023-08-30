from tkinter import *

root = Tk()
root.title("Python Pizza Order")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_price2 = 2
pepperoni_price3 = 3
extra_cheese_price = 1

total_bill = 0


def calculate_total():
    global total_bill
    total_bill = 0

    if size_var.get() == "Small":
        total_bill += small_pizza_price
        if pepperoni_var.get() == 1:
            total_bill += pepperoni_price2

    elif size_var.get() == "Medium":
        total_bill += medium_pizza_price
        if pepperoni_var.get() == 1:
            total_bill += pepperoni_price3

    elif size_var.get() == "Large":
        total_bill += large_pizza_price
        if pepperoni_var.get() == 1:
            total_bill += pepperoni_price3

    if extra_cheese_var.get() == 1:
        total_bill += extra_cheese_price

    total_label.config(text=f"Total: ${total_bill}")


size_label = Label(root, text="Size:")
size_label.pack()

size_var = StringVar()
size_var.set("Small")
size_options = ["Small", "Medium", "Large"]
size_menu = OptionMenu(root, size_var, *size_options)
size_menu.pack()

pepperoni_var = IntVar()
pepperoni_checkbox = Checkbutton(root, text="Pepperoni", variable=pepperoni_var)
pepperoni_checkbox.pack()

extra_cheese_var = IntVar()
extra_cheese_checkbox = Checkbutton(root, text="Extra Cheese", variable=extra_cheese_var)
extra_cheese_checkbox.pack()

calculate_button = Button(root, text="Calculate Total", command=calculate_total)
calculate_button.pack()

total_label = Label(root, text="Total: $0")
total_label.pack()

root.mainloop()

