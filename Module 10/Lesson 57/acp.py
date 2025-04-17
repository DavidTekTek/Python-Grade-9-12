# Program to print he Recurrence relation of the below 2 recursive functions 

# Funciton 1
def myfunction1(n):
  if(n>0):
      return
  for i in range (0,n+1):
      print("Codingal")
  myfunction1(n/2)
  myfunction1(n/3)

# Funciton 2
def myfunction2(n):
  if(n<=1):
      return
  print("Codingal")
  myfunction2(n-1)

# Printing the recurrence relations
print("For first funciton : ")
print("T(n) = T(n/2) + T(n/3) + N")

print("\nFor second funciton : ")
print("T(n) = T(n-1) + 1")