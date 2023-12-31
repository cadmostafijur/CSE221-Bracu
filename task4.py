def findmaxvalue(arr):
    if len(arr) <= 1:
        return arr, int(arr[0])
    mid = len(arr) // 2
    left, m_value = findmaxvalue(arr[:mid])
    right, m_value = findmaxvalue(arr[mid:])
    findmaxd, m_value = findmaxm(left, right, m_value)
    return findmaxd, m_value
def findmaxm(left, right, m_value):
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        exp = left[i] + right[j]*right[j]
        m_value = max(m_value, exp)
        if left[i] <= right[j]:
            i += 1
        else:
            j += 1
    return left+right, m_value
f1 = open("input4.txt", "r")
f2 = open("output4.txt", "w")
inp = f1.read().split("\n")
f1.close()
arr = inp[1].split(" ")
arr = list(map(int, arr))
sorted, max = findmaxvalue(arr)
f2.write(str(max))
f2.close()