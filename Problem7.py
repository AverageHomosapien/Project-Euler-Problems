# What is the 10 001st prime number?

def main():
    counter = 4
    primes = 2
    found = False
    prime_check = True
    while found == False:
        for x in range(2,counter):
            if counter % x == 0:
                prime_check = False
                break

        if prime_check == True:
            primes += 1

        if primes >= 10001:
            found = True
        else:
            counter +=1
            prime_check = True

    print("%d is the answer for number 7!" %(counter))







if __name__ == "__main__":
    main()
