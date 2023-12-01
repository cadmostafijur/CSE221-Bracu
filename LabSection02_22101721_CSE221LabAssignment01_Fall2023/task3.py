file1=open("input3.txt","r")
file2=open("output3.txt","w")
testcase=int(file1.readline().strip())
id = list(map(int, file1.readline().split()))
mark = list(map(int, file1.readline().split()))
#print(mark)[80, 60, 80, 50]
def selsort(testcase,id,mark):
    for i in range(testcase-1):
        index=i
        for j in range(i,testcase):
            if mark[j]>mark[index] or (mark[j]==mark[index] and id[j]<id[index]):
                index=j
        mark[i],mark[index]=mark[index],mark[i]
        id[i],id[index]=id[index],id[i]
selsort(testcase,id,mark)
for i in range(testcase):
    file2.write(f'ID: {id[i]} Mark: {mark[i]}\n')

# selsort that takes the number of test cases,
# student ids, and marks as input and sorts the
# students based on their marks in descending order. 
# finds the minimum element from the unsorted part of
# the array and swaps it with the first unsorted
# element. This process
# is repeated until the entire array is sorted. 