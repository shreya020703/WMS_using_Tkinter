import tkinter as tk
from tkinter import messagebox, Toplevel

# Function to add a new inventory entry
def add_inventory():
    try:
        item_name = item_name_entry.get().strip()
        item_qty = int(item_qty_entry.get())
        item_price = float(item_price_entry.get())
        item_sold = int(item_sold_entry.get())
        item_left = item_qty - item_sold

        if item_name == "":
            raise ValueError("Item name cannot be empty.")

        with open('inventory.txt', 'a') as file:
            file.write(f'{item_name},{item_qty},{item_price},{item_sold},{item_left}\n')
        
        messagebox.showinfo("Success", "Inventory added successfully!")
        clear_fields()
    
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to update an existing inventory entry
def update_inventory():
    try:
        item_name = item_name_entry.get().strip()
        item_qty = int(item_qty_entry.get())
        item_price = float(item_price_entry.get())
        item_sold = int(item_sold_entry.get())
        item_left = item_qty - item_sold

        updated = False
        with open('inventory.txt', 'r') as file:
            inventory_data = file.readlines()
        
        with open('inventory.txt', 'w') as file:
            for line in inventory_data:
                name, qty, price, sold, left = line.strip().split(',')
                if name == item_name:
                    file.write(f'{name},{item_qty},{item_price},{item_sold},{item_left}\n')
                    updated = True
                else:
                    file.write(line)
        
        if updated:
            messagebox.showinfo("Success", "Inventory updated successfully!")
        else:
            messagebox.showwarning("Warning", "Item not found.")
        
        clear_fields()

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to search and display an inventory entry
def search_inventory():
    search_name = item_name_entry.get().strip()
    if search_name == "":
        messagebox.showerror("Error", "Please enter an item name.")
        return
    
    with open('inventory.txt', 'r') as file:
        for line in file:
            name, qty, price, sold, left = line.strip().split(',')
            if name == search_name:
                result_label.config(text=f'{name} - Qty: {qty}, Price: {price}, Sold: {sold}, Left: {left}')
                return
    result_label.config(text=f'{search_name} not found in inventory.')

# Function to remove an existing inventory entry
def remove_inventory():
    remove_name = item_name_entry.get().strip()
    if remove_name == "":
        messagebox.showerror("Error", "Please enter an item name.")
        return
    
    removed = False
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    
    with open('inventory.txt', 'w') as file:
        for line in inventory_data:
            name, qty, price, sold, left = line.strip().split(',')
            if name != remove_name:
                file.write(line)
            else:
                removed = True
    
    if removed:
        messagebox.showinfo("Success", "Item removed successfully!")
    else:
        messagebox.showwarning("Warning", "Item not found.")
    
    clear_fields()

# Function to generate a full list of inventory
def generate_inventory():
    with open('inventory.txt', 'r') as file:
        inventory_data = file.readlines()
    
    if not inventory_data:
        result_label.config(text="No inventory available.")
        return

    inventory_text = ''
    for line in inventory_data:
        name, qty, price, sold, left = line.strip().split(',')
        inventory_text += f'{name} - Qty: {qty}, Price: {price}, Sold: {sold}, Left: {left}\n'

    result_label.config(text=inventory_text)

# Function to clear input fields
def clear_fields():
    item_name_entry.delete(0, tk.END)
    item_qty_entry.delete(0, tk.END)
    item_price_entry.delete(0, tk.END)
    item_sold_entry.delete(0, tk.END)

# Function to display the full inventory in a new window
def display_inventory_menu():
   with open('inventory.txt', 'r') as file:
       inventory_data = file.readlines()
       inventory_text = '\n'.join(inventory_data)
       result_label.config(text=inventory_text)

# create the main window
root = tk.Tk()
root.title("Inventory Management")

# input fields
item_name_label = tk.Label(root, text="Item Name:")
item_name_label.grid(row=0, column=0, padx=5, pady=5)
item_name_entry = tk.Entry(root)
item_name_entry.grid(row=0, column=1, padx=5, pady=5)

item_qty_label = tk.Label(root, text="Item Quantity:")
item_qty_label.grid(row=1, column=0, padx=5, pady=5)
item_qty_entry = tk.Entry(root)
item_qty_entry.grid(row=1, column=1, padx=5, pady=5)

item_price_label = tk.Label(root, text="Unit Price:")
item_price_label.grid(row=2, column=0, padx=5, pady=5)
item_price_entry = tk.Entry(root)
item_price_entry.grid(row=2, column=1, padx=5, pady=5)

item_sold_label = tk.Label(root, text="Items Sold:")
item_sold_label.grid(row=3, column=0, padx=5, pady=5)
item_sold_entry = tk.Entry(root)
item_sold_entry.grid(row=3, column=1, padx=5, pady=5)

# creating the buttons
add_button = tk.Button(root, text="Add Inventory", command=add_inventory)
add_button.grid(row=4, column=0, padx=5, pady=5)

update_button = tk.Button(root, text="Update Inventory", command=update_inventory)
update_button.grid(row=4, column=1, padx=5, pady=5)

search_button = tk.Button(root, text="Search Inventory", command=search_inventory)
search_button.grid(row=5, column=0, padx=5, pady=5)

remove_button = tk.Button(root, text="Remove Inventory", command=remove_inventory)
remove_button.grid(row=5, column=1, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Inventory", command=generate_inventory)
generate_button.grid(row=6, column=0, padx=5, pady=5)

display_button = tk.Button(root, text="Display Inventory", command=display_inventory_menu)
display_button.grid(row=6, column=1, padx=5, pady=5)

result_label = tk.Label(root, text="Inventory Display Area", anchor="w", justify="left")
result_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
