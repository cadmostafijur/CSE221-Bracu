file1=open("input1a.txt","r")
file2=open("output1a.txt","w")
testcase=file1.readline()#range 
#print(testcase)
for i in range(int(testcase)):
  newline='\n'
  current=file1.readline()#input num
  #print(current)
  if i==int(testcase):#check last iteration
    newline=''
  if int(current)%2==0:
    #print(current)
    file2.write(f"{int(current)} is an Even Number\n")
  else:
    file2.write(f"{int(current)} is an Odd Number\n")
file1.close()
file2.close()
#check last iteration
#It checks if the current iteration
# is the last one. If it is, it sets
# newline to an empty string (''), 
# suggesting no newline character
# after the output.