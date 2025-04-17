# Prime seive

def primeSeive(n):

    # Make list to store if number is prime or not     
    prime = [True for i in range(n + 1)]

    # Start from 2 as 1 and 0 are non prime
    currentNumber = 2
    while (currentNumber * currentNumber <= n):
        # If number is prime 
        if (prime[currentNumber] == True):
            # Mark all multiples of that number as non primes
            for i in range(currentNumber ** 2, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1

    # Mark 0,1 as non primes
    prime[0]= False
    prime[1]= False

    # Print all primes till n
    for p in range(n + 1):
        if prime[p]:
            print(p)


n = 99
print("All 2 digit prime numbers: ")
primeSeive(n)