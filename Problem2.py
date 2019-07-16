# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.


def main():
    total = 2
    sum1 = 1
    sum2 = 2
    temp = 0
    while sum2 < 4000000:
        temp = sum2
        sum2 = sum1 + sum2
        sum1 = temp
        if sum2 % 2 == 0:
            total += sum2
    print(total)


if __name__ == "__main__":
    main()
