# Programmer: Javan Graber
# Date: February 14, 2026
# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the
# month and keep a running total. (Enter 0 to exit the loop)
# When the loop finishes, the program should display the amount that the
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    # Establish the Boolean expression
    another_expense = True

    # Ask for the budget
    budget = float(input('Enter your budget for the month: '))

    while another_expense == True:

        # Ask for the expense
        expense = float(input('Enter the expense (or type 0 to stop): '))

        # Add the expense to the total
        total += expense

        # Make a validation
        if expense < 0:
            print('Error! That is invalid.')
            expense = float(input(f'Enter the real expense: '))

        if expense != 0:
            another_expense = True
        else:
            another_expense = False

    # Determine if they are over the budget or under it
    if total > budget:

        # Calculate how much they are over
        over_budget = total - budget

        # Display how much they are over
        print(f'Unfortunately, you are over the budget by ${over_budget:,.2f}')

    # Display if they exactly reach the budget
    elif total == budget:
        print('You are exactly on your budget')

    # Display if they are within the budget
    elif total < budget:

        # Calculate how much they are within the budget
        within_budget = budget - total

        # Display how much they are within the budget
        print(f'You are within the budget by ${within_budget:,.2f}')

    ######################


if __name__ == '__main__':
    main()
