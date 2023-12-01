def quicksort(arr,l,h):
    if l<h:
        pv = partition(arr,l,h)
        quicksort(arr,l,pv-1)# left of pivot
        quicksort(arr,pv+1,h)# recursive on right of pivot
def partition(arr,l,h):
    pvot = arr[h]
    i = l-1
    for j in range(l, h, 1):
        if arr[j]<pvot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i+1
file1 = open("input5.txt", "r")
file2 = open("output5.txt", "w")
inp = file1.read().split("\n")
file1.close()
n = int(inp[0])
arr = inp[1].split(" ")
arr = list(map(int, arr))
quicksort(arr,0,n-1)
arr = list(map(str, arr))
file2.write(" ".join(arr))
file2.close()