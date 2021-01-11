#!/usr/bin/env python3

# Created by Gabriel A
# Created on Jan 2021
# This program rounds decimal numbers

import math


def decimalRound(number, decimal):
    # rounds a decimal

    # process
    number[0] = number[0] * (10 ** decimal[0]) + 0.5
    number[0] = int(number[0])
    number[0] = number[0] / (10 ** decimal[0])


def main():
    # input the number and height

    # list
    number = []
    decimal = []

    while True:
        try:
            user_number = float(input("Enter a number, preferably one with"
                                      " decimals: "))
            user_place = int(input("Enter how many decimal places to"
                                   " round: "))
            print("")

            # list adding
            number.append(user_number)
            decimal.append(user_place)

            # calls function
            decimalRound(number, decimal)

            if user_place < 0:
                print("Invalid input\nTry again.\n")
            else:
                # ouput
                print("The rounded number is {}".format(number[0]))
                break

        except ValueError:
            print("\nInvalid input\nTry again.\n")


if __name__ == "__main__":
    main()
