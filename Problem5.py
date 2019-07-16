# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Brute Force Search - Takes 2 minutes ish
def main():
    found = False
    num = 1
    while found == False:
        divisible = True
        for x in range(1,20):
            if num % x != 0:
                divisible = False
                break

        if divisible == True:
            found = True
            print("Your number is %d!" %(num))
        else:
            num +=1

if __name__ == "__main__":
    main()
