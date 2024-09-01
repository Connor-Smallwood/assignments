# Connor Smallwood
# CBIS 4210
# Assignment 01.03
# 09/01/2024

# This program calculates the total cost of purchasing laptops, smartphones, and tablets, and applies a discount based on the total cost.


# Define a function to calculate the total cost of purchasing laptops, smartphones, and tablets
def calculate_total_cost(laptops, smartphones, tablets):
    # Define the prices for each product type
    laptop_price = 1000  # Price per Laptop
    smartphone_price = 600  # Price per Smartphone
    tablet_price = 300  # Price per Tablet

    # Calculate the cost for each product type
    laptop_cost = laptops * laptop_price
    smartphone_cost = smartphones * smartphone_price
    tablet_cost = tablets * tablet_price

    # Calculate the total cost by summing up the costs of all product types
    total_cost = laptop_cost + smartphone_cost + tablet_cost

    # Return the total cost to be used elsewhere in the program
    return total_cost


# Define a function to apply a discount based on the total cost
def apply_discount(total_cost):
    # Apply discount based on the total cost
    if total_cost >= 5000:
        discount = 0.10  # 10% discount
    elif total_cost >= 2000:
        discount = 0.05  # 5% discount
    else:
        discount = 0.00  # No discount

    # Calculate the final amount after applying the discount
    final_amount = total_cost - (total_cost * discount)

    # Return the final amount to be paid
    return final_amount


# Define the main function to prompt the user for input and display the final amount to be paid
def main():
    # Prompt the user to enter the number of Laptops they want to purchase
    laptops = int(input("Enter the number of Laptops: "))

    # Prompt the user to enter the number of Smartphones they want to purchase
    smartphones = int(input("Enter the number of Smartphones: "))

    # Prompt the user to enter the number of Tablets they want to purchase
    tablets = int(input("Enter the number of Tablets: "))

    # Calculate the total cost using the calculate_total_cost function
    total_cost = calculate_total_cost(laptops, smartphones, tablets)

    # Apply the discount using the apply_discount function
    final_amount = apply_discount(total_cost)

    # Display the final amount to the user
    print("Final Amount to be Paid: $", final_amount)


# Main guard to ensure that the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
