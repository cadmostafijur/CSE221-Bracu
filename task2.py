def mergeSort(arr):
    if len(arr) <= 1:
        return arr, int(arr[0])
    mid = len(arr) // 2
    left, maxValue = mergeSort(arr[:mid])
    right, maxValue = mergeSort(arr[mid:])

    merged, max_value = merge(left, right, maxValue)
    #print(merged)
    #print(maxValue)
    return merged, max_value
def merge(left, right, maxValue):
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            maxValue = max(maxValue, right[j])
            i += 1
        else:
            maxValue = max(maxValue, left[i])
            j += 1
    #print(left+right)
    #print(maxValue)
    return left+right, maxValue
file1 = open("input2.txt", "r")
file2 = open("output2.txt", "w")
inp = file1.read().split("\n")
file1.close()
arr = inp[1].split(" ")
arr = list(map(int, arr))
sorted, max = mergeSort(arr)
file2.write(str(max))
file2.close()
#here thus code time complexity O(nlogn)
# comparison based sorting algorithm that divide the input array into smaller subarray, sort them and merege them.
