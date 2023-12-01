file1=open("input1.txt","r")
file2=open("output1.txt","w")
arr=file1.readlines()
n=list(map(int,arr[0].split(" ")))
s=list(map(int,arr[1].split(" ")))
flag=False
for i in range(len(s)):
  for j in range(len(s)):
    sum=0
    if j!=i:
      sum=s[i]+s[j]
    if sum==n[1]:
      index=f"{i+1} {j+1}"
      file2.write(index)#writelines
      flag=True
      break
  if flag==True:
    break
if flag==False:
  file2.write("Impossible")