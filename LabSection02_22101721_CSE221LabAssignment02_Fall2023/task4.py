f1 = open("input4.txt", "r")
f2 = open("output4.txt", "w")

inp= f1.read().split("\n")
f1.close()

numlst = inp[0].split(" ")
# print(testcase)
start = int(numlst[0])
# print(n)
end = int(numlst[1])
tasks = []
total = [[]]*end
poss = []
cnt = 0 #counting

for i in range(1, len(inp), 1):
  data = inp[i].split(" ")
  starti = int(data[0])
  endi = int(data[1])
  tasks.append((starti, endi))
#sort tasks by end times
tasks = sorted(tasks, key=lambda x: x[1])
#allocate tasks to time slots see comnts
for i in range(len(tasks)):
  curnt = tasks[i]
  if i==0:
    total[0]=[curnt]
    cnt+=1
  else:
    for j in range(len(total)):
      if len(total[j])>0:
        diff = int(curnt[0]) - int(total[j][-1][1])
      else:
        diff = -9999
      if diff>=0:
        poss.append([j,diff])
    if len(poss)>0:
      poss = sorted(poss, key=lambda x: x[1])
      idx = poss[0][0]
      total[idx].append(curnt)
      cnt+=1
    else:
      if [] in total:
          idx = total.index([])
          total[idx]=[curnt]
          cnt+=1
  poss = []
f2.write(str(cnt))



#iterates through the sorted tasks and allocates each
# task to a suitable time slot. It considers the time
# difference between the current task's start time and
# the end time of the last task in each time slot.
#{#for extra line space error
#ValueError: invalid literal for int() with base 10: ''}