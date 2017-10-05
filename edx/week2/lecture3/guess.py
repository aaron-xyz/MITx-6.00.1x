def main():
    """
    Exercise: guess my number

    ESTIMATED TIME TO COMPLETE: 15 minutes

    In this problem, you'll create a program that guesses a secret number!

    The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

    Here is a transcript of an example session:

    Please think of a number between 0 and 100!
    Is your secret number 50?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
    Is your secret number 75?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
    Is your secret number 87?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
    Is your secret number 81?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
    Is your secret number 84?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
    Is your secret number 82?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
    Is your secret number 83?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
    Game over. Your secret number was: 83
    """
    # limits
    low = 0
    hi = 100

    # start guessing in the middle
    secret_number = int((hi + low) / 2)
    print("Please think of a number between 0 and 100!")

    # Iterate until guess the number
    while True:
        print("Is your secret number " + str(secret_number) + "?")
        # Three choices
        print("Enter 'h' to indicate the guess is too high.", end=' ')
        print("Enter 'l' to indicate the guess is too low.", end=' ')
        print("Enter 'c' to indicate I guessed correctly.", end='')
        # store the chice user in the choice variable
        choice = input(" ")
        # Search in the lowest half
        if choice == 'h':
            hi = secret_number
            secret_number = int((hi + low) / 2)
        # Search in the highest half
        elif choice == 'l':
            low = secret_number
            secret_number = int((hi + low) / 2)
        # The number was guessed
        elif choice == 'c':
            print("Game over. Your secret number was: " + str(secret_number))
            break
        # If the input is wrong
        else:
            print("Sorry, I did not understand your input.")


# Call the function main
if __name__ == "__main__":
    main()