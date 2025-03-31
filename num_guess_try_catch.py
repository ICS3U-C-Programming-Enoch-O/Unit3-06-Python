#!/usr/bin/env python3
# Created by: Enoch O
# Created on: March 28, 2025


def main():
    # This function uses a try statement.

    # Get users input
    integer_as_string = input("Enter an integer:")
    print("")

    # process users input
    try:
        integer_as_number = int("integer_as_string")
        print("you entered an integer correctly")
    except ValueError:
        print("That was not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
