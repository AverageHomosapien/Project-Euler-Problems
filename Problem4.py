# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    num1 = 999
    num2 = 999
    temp = 0
    temp_str = ""
    highest = 0

    for x in range(2,num1):
        for y in range(2,num2):
            temp = x * y
            temp_str = str(temp)
            if temp_str == temp_str[::-1]:
                if temp > highest:
                    highest = temp

    print("Your number is %s." %(highest))


if __name__ == "__main__":
    main()
