file1=open("input4.txt","r")
file2=open("output4.txt","w")
l = file1.readlines() #list and string with ,
# print(l)
train = []
dest = []
time = []
d_time = {}
d_dest = {}

def seletionSort(arr1, arr2):
    f = []
    for i in range(len(arr1)):
        max = i
        for j in range(i+1, len(arr1)):
            if arr1[j] > arr1[max]:
                max = j
        arr1[i], arr1[max] = arr1[max], arr1[i]
        arr2[i], arr2[max] = arr2[max], arr2[i]
    f.append(arr1)
    f.append(arr2)#[[time],[destin]]
    return f

for t in range(1, len(l)):
    i = l[t].split()
    train.append(i[0])
    tm = i[len(i)-1]
    tm = tm.replace(":", ".")
    tm = float(tm)
    if i[0] not in d_time:
        d_time[i[0]] = [tm]
        d_dest[i[0]] = [i[len(i)-3]]
    else:
        d_time[i[0]] += [tm]
        d_dest[i[0]] += [i[len(i)-3]]
for k, v in d_time.items():#sort departure times for each train
    temp = seletionSort(v, d_dest[k])#d_dest[k] destination in list
    #v = timing
    d_time[k] = temp[0]
    d_dest[k] = temp[1]
train.sort()#train name sort dictionary order 
line = ""
for z in range(len(train)):
    trn = train[z]
    tim = d_time[trn][0]
    dst = d_dest[trn][0]
    d_time[trn].remove(tim)
    d_dest[trn].remove(dst)
    tim = f"{tim:.2f}"
    tim = str(tim).zfill(5)
    tim = tim.replace(".", ":")
    ll = f"{trn} will departure for {dst} at {tim}"
    if z != len(train)-1:
        line += ll + "\n"
    else:
        line += ll
file2.writelines(line)
#lexicographical order or dictionary order 
# order of their appearance in a dictionary or
# alphabet.  
# selsort that takes the number of test cases,
# student ids, and marks as input and sorts the
# students based on their marks in descending order. 
# finds the minimum element from the unsorted part of
# the array and swaps it with the first unsorted
# element. This process
# is repeated until the entire array is sorted. 