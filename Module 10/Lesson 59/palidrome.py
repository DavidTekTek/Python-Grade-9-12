# Program to check if the given number is a palindrome 


# Take input from the user
number = int(input("Enter your Number : "))


# Store the number for comparision later 
store  = number
reverse=int(0)


# while number is not 0 all last digit to reverse number
while(number>0):
  rem = (number%10)
  reverse = reverse*10 + rem
  number//=10


# Print reversed number
print("\nReversed number : ",reverse)


# Check if palindrome or not
if(store==reverse):
  print("\nPalindrome")
else:
  print("\nNot palindrome")