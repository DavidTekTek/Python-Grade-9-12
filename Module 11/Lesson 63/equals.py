def  checkIfSame(number1,number2):
  if((number1 ^ number2)!= 0):
    print("numbers are not equal")

  else:
    print("both numbers are equal")

number1 = int(input("Enter first number to compare"))
number2 = int(input("Enter second number to compare"))
checkIfSame(number1, number2)