# Program to print the time complexity of the given function

# Given function
def myfunction(n):
  # Loop 1  
  for i in range(0,n+1):
      print("First Loop")

  # Loop 2
  j=1
  while(j<=n+1):
      print("Second Loop ",j)
      j=j*2

  # Loop 3
  for i in range(0,100):
      print("Third loop")

print("Function above will take time :")
print(" O(N) +  O(log N) + O(1)")