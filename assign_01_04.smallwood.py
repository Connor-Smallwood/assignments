# Connor Smallwood
# CBIS 4210
# Assignment 01.04
# 09/01/2024

# This program calculates the total number of items in stock and checks which items need to be restocked based on the current stock quantity.


# Define a function to calculate the total number of items in stock
def calculate_total_stock(widgets_stock, gadgets_stock, doodads_stock):
    # Calculate the total number of items in stock
    total_stock = widgets_stock + gadgets_stock + doodads_stock

    # Return the total number of items in stock to be used elsewhere in the program
    return total_stock


# Define a function to check which items need to be restocked based on the current stock quantity
def check_restock_items(widgets_stock, gadgets_stock, doodads_stock):
    # Define the minimum threshold for restocking for each item
    widgets_threshold = 50  # Minimum stock level for Widgets
    gadgets_threshold = 30  # Minimum stock level for Gadgets
    doodads_threshold = 20  # Minimum stock level for Doodads

    # Create a list to hold items that need to be restocked
    restock_list = []

    # Check if the stock for Widgets is below the threshold and add to restock list if true
    if widgets_stock < widgets_threshold:
        restock_list.append("Widgets")

    # Check if the stock for Gadgets is below the threshold and add to restock list if true
    if gadgets_stock < gadgets_threshold:
        restock_list.append("Gadgets")

    # Check if the stock for Doodads is below the threshold and add to restock list if true
    if doodads_stock < doodads_threshold:
        restock_list.append("Doodads")

    # Return the list of items that need to be restocked
    return restock_list


# Define the main function to prompt the user for input and display the total number of items in stock and items that need to be restocked
def main():
    # Prompt the user to enter the current stock quantity for Widgets and store the input as an integer
    widgets_stock = int(input("Enter the current stock quantity for Widgets: "))

    # Prompt the user to enter the current stock quantity for Gadgets and store the input as an integer
    gadgets_stock = int(input("Enter the current stock quantity for Gadgets: "))

    # Prompt the user to enter the current stock quantity for Doodads and store the input as an integer
    doodads_stock = int(input("Enter the current stock quantity for Doodads: "))

    # Calculate the total number of items in stock using the calculate_total_stock function
    total_stock = calculate_total_stock(widgets_stock, gadgets_stock, doodads_stock)

    # Check which items need to be restocked using the check_restock_items function
    restock_list = check_restock_items(widgets_stock, gadgets_stock, doodads_stock)

    # Display the total number of items in stock
    print("Total Number of Items in Stock:", total_stock)

    # Display the list of items that need to be restocked
    if restock_list:
        print("Items that need to be restocked:")
        for item in restock_list:
            print(f"- {item}")
    else:
        print("All items are sufficiently stocked.")


# Main guard to ensure that the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
