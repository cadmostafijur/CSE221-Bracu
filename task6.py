def partition(arr1,l,h):#(a,p,r):
    x = arr1[h]
    i = l-1
    for j in range(l, h, 1):
        if arr1[j]<x:
            i +=1
            arr1[i], arr1[j] = arr1[j], arr1[i]
    arr1[i+1], arr1[h] = arr1[h], arr1[i+1]
    return i+1
def findkthSmallest(arr1,k):
    l = 0
    h = len(arr1)-1
    while l<=h:
            p_idx = partition(arr1,l,h) 
            if p_idx==k-1:# check pivot index
                return arr1[p_idx]
            elif p_idx>k-1:
                h = p_idx-1
            else:
                l = p_idx+1
file1 = open("input6.txt", "r")
file2 = open("output6.txt", "w")
inp = file1.read().split("\n")
file1.close()
t_ele = (inp[0].split(" "))[0]# total element
nq = (inp[0].split(" "))[2]
arr = inp[1].split(" ")# all elements in list type str
arr = list(map(int, arr))# int value in list
for i in range(3, len(inp), 1):
  rslt = findkthSmallest(arr, int(inp[i]))
  #print(rslt)
  if i<len(inp)-1:
    file2.write(str(rslt)+"\n")
  else:
    file2.write(str(rslt))
file2.close()
