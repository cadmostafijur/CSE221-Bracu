file1=open("input1b.txt","r")
file2=open("output1b.txt","w")
testcase=file1.readline()
for i in range(int(testcase)):
  newline='\n'
  current=file1.readline()
  current=current.split()
  #print(current) like list ['calculate', '8', '*', '84']
  if i==int(testcase)-1:
    newline=''
  if current[2]=='+':
    result=int(current[1]) +int(current[3])
  elif current[2]=='-':
    result=int(current[1]) -int(current[3])
  elif current[2]=='*':
    result=int(current[1]) *int(current[3])
  elif current[2]=='/':
    result=int(current[1]) /int(current[3])
  file2.write(f" The result of {current[1]} {current[2]} {current[3]} is {result} {newline}")
file1.close()
file2.close()
#check last iteration
#It checks if the current iteration
# is the last one. If it is, it sets
# newline to an empty string (''), 
# suggesting no newline character
# after the output.