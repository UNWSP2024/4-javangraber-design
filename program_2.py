# Programmer: Javan Graber
# Date: February 14, 2026
# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many
# tickets are desired for each movie.
# At the end of the program it prints out the total number of tickets desired by the user.
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    # Establish accumulator
    total = 0

    # Establish the Boolean expression
    another_movie = True

    while another_movie == True:
        # Get the movie
        film = input('Enter a movie title: ')
        # Get the tickets
        tickets = int(input(f'Enter the number of tickets for {film}: '))
        # Add the tickets to the total
        total += tickets

        # Make a validation loop
        if tickets < 0:
            print('Error! That is invalid.')
            tickets = int(input(f'Enter the real number of tickets for {film}: '))

        # Ask for another movie
        question = input('Is there another movie (type y or n)? ')
        if question == 'y':
            another_movie = True
        else:
            another_movie = False

    # Display the total
    print(f'You need to purchase {total} tickets.')

    ######################


if __name__ == '__main__':
    main()
