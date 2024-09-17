# Inventory Management System

A simple inventory management system built using Python's `tkinter` module for the graphical user interface (GUI). The program allows users to manage inventory items by adding, updating, searching, removing, and displaying all items in a neat interface. All data is stored in a text file (`inventory.txt`) for persistence.

## Features

- **Add Inventory**: Add new items with details such as name, quantity, unit price, and items sold.
- **Update Inventory**: Update the details of an existing item (quantity, price, items sold).
- **Search Inventory**: Search for an item by name and view its details.
- **Remove Inventory**: Remove an item from the inventory.
- **Generate Inventory**: Display the entire inventory list in the main window.
- **Display Inventory**: Opens a new window with a table-like format showing all inventory items.

## How It Works

1. **Inventory Storage**: 
   - Inventory data is stored in a text file (`inventory.txt`), with each item saved as a line in the format:
     ```
     ItemName,Quantity,UnitPrice,ItemsSold,ItemsLeft
     ```
   - When you add or update items, the text file is modified accordingly.

2. **Graphical Interface**: 
   - The interface is built using `tkinter`, providing buttons for each operation (Add, Update, Search, Remove, Generate, Display).
   - Items can be viewed and managed directly from the GUI.

3. **Error Handling**: 
   - Input validation and exception handling are included to ensure that valid data is entered (e.g., preventing the entry of non-numeric values for quantity and price).

## Getting Started

### Prerequisites

- **Python 3.x** must be installed on your machine.
- No external libraries are required other than `tkinter`, which is included with most Python installations.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/inventory-management-system.git
    ```

2. Navigate to the project directory:

    ```bash
    cd inventory-management-system
    ```

3. Run the Python script:

    ```bash
    python inventory_management.py
    ```

## How to Use

1. **Add Inventory**:
   - Fill in the fields for Item Name, Quantity, Unit Price, and Items Sold.
   - Click the **Add Inventory** button to save the item to the inventory.

2. **Update Inventory**:
   - Enter the name of the item you want to update along with the new quantity, price, and sold items.
   - Click the **Update Inventory** button to update the item's details.

3. **Search Inventory**:
   - Enter the item name in the `Item Name` field and click **Search Inventory** to search for the item. The details will be displayed below.

4. **Remove Inventory**:
   - Enter the item name in the `Item Name` field and click **Remove Inventory** to delete it from the inventory.

5. **Generate Inventory**:
   - Click **Generate Inventory** to display a list of all items in the main window.

6. **Display Inventory**:
   - Click **Display Inventory** to open a new window with a table format of the entire inventory.

## File Structure

