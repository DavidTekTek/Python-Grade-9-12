# Program to find multiple with 1 and N iterations

# For 1 iteration simply multiply 
def o1(n,m):
  total = n*m
  print("\n1 iteration: ",total) 

# For N iteration run a for loop
def oN(n,m):
  total = 0
  for i in range(1,n+1):
    total += m
  print("N iteration: ",total) 

m = int(input("Enter 'a' for a*b : "))
n = int(input("Enter 'b' for a*b : "))

o1(m,n)
oN(m,n)