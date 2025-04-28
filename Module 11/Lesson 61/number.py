def numberOfBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count

n = int(input("Enter a number: "))
print("Number of bits: ", numberOfBits(n))