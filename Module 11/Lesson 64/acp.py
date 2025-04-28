# Program to check if a number is power of 8

def powerOf8(number):
	
	# Variable i will denote the bit
	# that we are currently at
	bitPosition = 0
	mask = 1
	
	while (bitPosition <= 63):
		mask <<= bitPosition

		# If only set bit in n
		# is at position i
		if (mask == number):
			return True

		# Get to next valid bit position
		bitPosition += 3
		mask = 1

	return False

number = int(input("Enter your number : "))
if (powerOf8(number)):
	print("Yes ",number,"is power of 8")
else:
	print("No ",number,"is not power of 8")