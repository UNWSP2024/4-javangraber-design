# Programmer: Javan Graber
# Date: February 14, 2026
# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average
# rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    # Ask for the number of years
    num_years = int(input('Enter the number of years: '))

    # Create the first loop
    for year in range(num_years):
        # Establish the accumulator
        total = 0

        # Create the inner loop
        for month in range(1, 13):
            inches = float(input('Enter the number of inches for the months in order: '))
            total += inches

            # Create validation
            if inches < 0:
                print('Error! That is invalid input!')
                inches = float(input('Enter the real number of inches for the months in order: '))

    # Calculate and Display the number of months
    number_of_months = num_years * 12
    print(f'The total months is {number_of_months}')

    # Display the total rainfall
    print(f'The total rainfall is {total:.2f}')

    # Calculate and Display the average rainfall
    average_rainfall = total / number_of_months
    print(f'The average rainfall for the period is {average_rainfall:.2f}')
    ######################


if __name__ == '__main__':
    main()
