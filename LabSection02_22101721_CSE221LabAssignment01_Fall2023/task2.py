file1=open("input2.txt","r")
file2=open("output2.txt","w")
testcase=file1.readlines()
arr=list(map(int,testcase[1].split(" ")))
def bubblesort(arr):
  for i in range( len(arr)):
     swap=0#detecting whether the array is already sorted
     for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
          arr[j],arr[j+1]=arr[j+1],arr[j]
          swap=1
     if swap== 0:
         break
  return arr

bubblesort(arr)
#file2.write(str(arr)[1:-1].split())
strg=""
for i in range(len(arr)):
  strg+=str(arr[i]) +" "
file2.write(strg)
file1.close()
file2.close()
#  detecting whether the array is already 
#  sorted. If no swaps are made during a 
#  pass, it indicates that the array is 
# sorted