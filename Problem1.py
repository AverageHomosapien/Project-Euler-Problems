# Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    total = 0
    for x in range(0,1000):
        if x % 5 == 0 or x % 3 == 0:
            total += x
    print(total)


if __name__ == "__main__":
    main()
