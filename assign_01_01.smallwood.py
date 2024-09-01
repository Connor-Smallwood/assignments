# Connor Smallwood
# CBIS 4210
# Assignment 01.01
# 09/01/2024

# This program calculates the total revenue generated from selling apples, bananas, and cherries.


# Define a function to calculate the total revenue generated from selling apples, bananas, and cherries
def calculate_revenue(apples_sold, bananas_sold, cherries_sold):
    # Define the prices for each type of fruit
    apple_price = 0.60  # Price per apple
    banana_price = 0.40  # Price per banana
    cherry_price = 0.25  # Price per cherry

    # Calculate the revenue for each type of fruit
    apple_revenue = apples_sold * apple_price  # Revenue from apples
    banana_revenue = bananas_sold * banana_price  # Revenue from bananas
    cherry_revenue = cherries_sold * cherry_price  # Revenue from cherries

    # Calculate the total revenue by summing up the revenue from all types of fruit
    total_revenue = apple_revenue + banana_revenue + cherry_revenue

    # Return the total revenue to be used elsewhere in the program
    return total_revenue

# Define the main function to prompt the user for input and display the total revenue
def main():
    # Prompt the user to enter the number of apples sold and store the input as an integer
    apples_sold = int(input("Enter the number of Apples sold: "))

    # Prompt the user to enter the number of bananas sold and store the input as an integer
    bananas_sold = int(input("Enter the number of Bananas sold: "))

    # Prompt the user to enter the number of cherries sold and store the input as an integer
    cherries_sold = int(input("Enter the number of Cherries sold: "))

    # Call the calculate_revenue function, passing the number of each fruit sold as arguments
    total_revenue = calculate_revenue(apples_sold, bananas_sold, cherries_sold)

    # Display the total revenue to the user
    print("Total Revenue: $", total_revenue)


# Main guard to ensure that the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
