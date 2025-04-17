# Program to convert Binary to decimal 
 
def binaryToDecimal(binary):
    
    # Variable set as 0
    decimal, i = 0, 0

    # while there is a digit multiply with 2 power i 
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10

        # increment i
        i += 1
    print("Decimal : ",decimal)   
     

# Take binary input from the user 
binary = int(input("Enter your Binary: "))

# Call function
binaryToDecimal(binary)