def cpair(arr): # count the pair
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, c_left = cpair(arr[:mid])
    right, c_right = cpair(arr[mid:])
    s_arr, cnt = cpairm(left, right)

    t_count = c_left + c_right + cnt # count the total leftcount and right count and count
    return s_arr, t_count # return sorted array

def cpairm(left, right):
    mergedlist = []
    c = 0
    i = 0
    j = 0
    while i < len(left) and j < len(right): #check
        if left[i] > right[j]:
            mergedlist.append(left[i])
            c += len(right) - j
            i += 1
        else:
            mergedlist.append(right[j])
            j += 1

    mergedlist.extend(left[i:])
    mergedlist.extend(right[j:])

    return mergedlist, c

f1 = open("input3.txt", "r")
f2 = open("output3.txt", "w")
inp = f1.read().split("\n")
f1.close()
arr = inp[1].split(" ")
arr = list(map(int, arr))
sorted_array, count = cpair(arr)
f2.write(str(count))
f2.close()