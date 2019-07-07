# What is the largest prime factor of the number 600851475143 ?
# Date Last Modified: 07/07/2019
# Author: Calum Hamilton


def main():
    prime = False
    num = 600851475143
    while prime == False:
        prime_test = True

        for x in range(2,int(num)):
            if num % x == 0:
                num = num / x
                prime_test = False
                break

        if prime_test == True:
            prime = True
            print("The prime is %d." %(num))




if __name__ == "__main__":
    main()
