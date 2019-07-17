#Find the sum of all the primes below two million.
import numpy as np

# Program has an array of integers and mirror array of booleans
# Finds the prime numbers and marks in boolean array
def main():
    prime_total = 0.0
    temp = 0
    num_list = np.arange(2000000)
    bool_list = np.ones((2000000), dtype=bool)

    for numbers in range(2,(num_list.size//2)):
        multiplier = 2
        temp = numbers*multiplier
        while temp<2000000:
            bool_list[temp] = False
            multiplier+=1
            temp = numbers*multiplier

    bool_list[1] = False
    bool_list[2] = True

    for x in range(bool_list.size):
        if bool_list[x] == True:
            prime_total += num_list[x]
    print("The prime total is %d." %(prime_total))


if __name__ == "__main__":
    main()
