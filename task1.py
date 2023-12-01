def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)// 2 #find the mid
    # print("mid",mid)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    merged = []
    i = 0
    j = 0
    # print("len:",len(left))
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
f1 = open("input1.txt", "r")
f2 = open("output1.txt", "w")
inp = f1.read().split("\n")
f1.close()
arr = inp[1].split(" ")
arr = list(map(int, arr))
sorted = list(map(str, mergeSort(arr)))
f2.write(" ".join(sorted))
f2.close()
