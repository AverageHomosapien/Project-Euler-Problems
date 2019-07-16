import math

def main():
    temp = 0.0
    answer = 0
    calc = 0
    for x in range(0,400):
        for y in range(0,400):
            temp = math.sqrt((x ** 2) + (y ** 2))
            calc = (x + y + temp)
            if calc == 1000:
                answer = x * y * temp
                break

    print("Answer is %d." %(answer))


# Call Main function
if __name__ == "__main__":
    main()
