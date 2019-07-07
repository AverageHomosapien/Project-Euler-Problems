# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Date Last Modified: 07/07/2019
# Author: Calum Hamilton


def main():
    sum_of_nat = 0
    sum_of_squares = 0

    for x in range(1,101):
        sum_of_nat += x

    sum_of_nat = sum_of_nat ** 2

    for x in range(1,101):
        sum_of_squares += x ** 2

    total = sum_of_nat - sum_of_squares

    print("%d is the answer!" % (total))





if __name__ == "__main__":
    main()
