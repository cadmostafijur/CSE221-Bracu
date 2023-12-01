f1 = open("input3.txt", "r")
f2 = open("output3.txt", "w")
inp = f1.read().split("\n")
tasks=[]
for i in range(int(inp[0])):
    arr = inp[i+1].split(" ")
    arr = list(map(int, arr))
    tasks.append(arr)
tasks.sort(key=lambda x: (x[1],x[0]))#sort task by end time
# print(tasks)
done_task=[]
curr_edtime=-1
for j in tasks: # iterate j to find the non overlaping time
    start,end=j
    if start>=curr_edtime:
        done_task.append((start,end))
        curr_edtime=end
# print(len(done_task))# len of task done
f2.write(f"{len(done_task)}\n")
for k in done_task:
    f2.write(f"{k[0]} {k[1]}\n")
    