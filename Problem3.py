# What is the largest prime factor of the number 600851475143 ?
# Date Last Modified: 07/07/2019
# Author: Calum Hamilton


def main():
    prime = False
    num = 600851475143
    while prime == False:
        if num % 2 == 0:
            num = num / 2
        elif num % 3 == 0:
            num = num / 3
        else:
            prime_test = True
            for x in range(4,num):
                if num % x == 0:
                    num = num / x
                    prime_test == False
                    break
            if prime_test == True:
                prime = True
                print(num)



if __name__ == "__main__":
    main()
