# Connor Smallwood
# CBIS 4210
# Assignment 01.02
# 09/01/2024

# This program calculates the average grade and performance of a student based on their scores in Math, Science, and English.


# Define a function to calculate the average grade based on the scores in Math, Science, and English
def calculate_average(math_score, science_score, english_score):
    # Calculate the average grade by summing up the scores and dividing by the number of subjects
    average_grade = (math_score + science_score + english_score) / 3

    # Return the calculated average grade to be used elsewhere in the program
    return average_grade

# Define a function to determine the student's performance based on their average grade
def determine_performance(average_grade):
    # Determine the student's performance based on their average grade
    if average_grade >= 90:
        return "Excellent"
    elif average_grade >= 75:
        return "Good"
    elif average_grade >= 50:
        return "Average"
    else:
        return "Poor"

# Define the main function to prompt the user for input and display the average grade and performance
def main():
    # Prompt the user to enter the Math score and store the input as a float
    math_score = float(input("Enter the Math score: "))

    # Prompt the user to enter the Science score and store the input as a float
    science_score = float(input("Enter the Science score: "))

    # Prompt the user to enter the English score and store the input as a float
    english_score = float(input("Enter the English score: "))

    # Call the calculate_average function, passing the scores as arguments
    average_grade = calculate_average(math_score, science_score, english_score)

    # Determine the performance based on the average grade
    performance = determine_performance(average_grade)

    # Display the average grade and the performance message to the user
    print("Average Grade:", average_grade)
    print("Performance:", performance)


# Main guard to ensure that the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
