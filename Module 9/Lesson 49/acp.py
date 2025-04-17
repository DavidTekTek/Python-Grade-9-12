# open the file in read mode
file_read = open('Sample_File.txt','r')
print("File in Read Mode -")
print(file_read.read())
file_read.close()

# open the file in write mode
file_write = open('Sample_File.txt', 'w')
# write in the file 
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am a class 8 student from Pune")
file_write.close()

# open the file in append mode
file_append = open('Sample_File.txt', 'a')
# append in the file 
file_append.write("\n File in append mode ....")
file_append.write("Hi! My favourite subject is Mathematics")
file_append.close()