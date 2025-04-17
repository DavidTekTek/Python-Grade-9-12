# write in file using with()function
with open('Sample_File', 'w') as file:
  file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

# split file into words
with open('Sample_File.txt', 'r') as file:
  data = file.readlines()
  print("Words in this file are....")
  for line in data:
    word = line.split()
    print (word)
file.close()

#check if a file exists 
import os
print("Checking if my_file exists or not....")
if os.path.exists("My_file.txt"):
  print("File exists")
else:
  print("The file does not exist")

#create a new if it doesn't
my_file = open("My_file.txt", "w")
my_file.write("Hi! I am Penguin. I am in class 8 studying in Pune.")
my_file.close()

#delete file named codingal
os.remove('Sample_doc.txt')