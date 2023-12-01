file1=open("input1.txt","r")
file2=open("output1.txt","w")
arr=file1.readlines()
n=list(map(int,arr[0].split(" ")))
s=list(map(int,arr[1].split(" ")))
flag=False
flag1=False
for i in range(len(s)):
    # difference between the target sum (n[1]) and 
    # the current element in the array (s[i]). 
    check=n[1]-s[i]#10-1=9 , 9dorkar
    if check in s and flag==False:#check match val
            value=check#value=9
            index=i+1
            flag=True
    elif flag==True and value==s[i]:
        indexs=f"{index} {i+1}"
        file2.writelines(indexs)
        flag1=True
        break
if flag1==False:
    file2.writelines("Impossible") 
file1.close()
file2.close()     
#track whether the main condition 
# (finding a matching pair)