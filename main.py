# Import the Tkinter module for GUI
from tkinter import *

# Create the main window
root = Tk()
root.title("Python Pizza Order")

# Define pizza prices
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25
pepperoni_price2 = 2
pepperoni_price3 = 3
extra_cheese_price = 1

# Initialize total bill variable
total_bill = 0

# Function to calculate and update the total bill
def calculate_total():
    global total_bill
    total_bill = 0

    # Calculate based on pizza size
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

    # Add extra cheese if selected
    if extra_cheese_var.get() == 1:
        total_bill += extra_cheese_price

    # Update the total label
    total_label.config(text=f"Total: ${total_bill}")

# Labels for pizza size
size_label = Label(root, text="Size:")
size_label.pack()

# Dropdown menu for pizza size
size_var = StringVar()
size_var.set("Small")
size_options = ["Small", "Medium", "Large"]
size_menu = OptionMenu(root, size_var, *size_options)
size_menu.pack()

# Checkbox for Pepperoni
pepperoni_var = IntVar()
pepperoni_checkbox = Checkbutton(root, text="Pepperoni", variable=pepperoni_var)
pepperoni_checkbox.pack()

# Checkbox for Extra Cheese
extra_cheese_var = IntVar()
extra_cheese_checkbox = Checkbutton(root, text="Extra Cheese", variable=extra_cheese_var)
extra_cheese_checkbox.pack()

# Button to calculate total
calculate_button = Button(root, text="Calculate Total", command=calculate_total)
calculate_button.pack()

# Label to display the total amount
total_label = Label(root, text="Total: $0")
total_label.pack()

# Start the GUI application
root.mainloop()



