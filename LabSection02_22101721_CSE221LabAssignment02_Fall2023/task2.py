#task 2 (1)O(nlogn).
def task2_1():
    file1 = open("input2.txt", "r")
    file2 = open("output2.txt", "w")

    inp = file1.read().split("\n")
    file1.close()

    len1 = int(inp[0])# take length input file
    arrr1 = inp[1].split(" ")#split array and take those number and in list str
    len2 = int(inp[2])
    arrr2 = inp[3].split(" ")

    arrr1.extend(arrr2)# add the elements of arr2  to the arr1 list
    arrr1.sort()# sort the arr1
    file2.write(" ".join(arrr1))
    file2.close()

#task 2 (2)O(n)
def task2_2():
    file1 = open("input2.txt", "r")
    file2 = open("output2.txt", "w")

    inp = file1.read().split("\n")
    file1.close()
    len1 = int(inp[0])
    arrr1 = inp[1].split(" ")
    len2 = int(inp[2])
    arrr2 = inp[3].split(" ")
    tolen = len1+len2# total length is sumation len1 and len2
    arrr3 = []

    x = 0
    y = 0
    for i in range(tolen):
        if x<len1 and y<len2:
            if int(arrr1[x])<int(arrr2[y]):
                arrr3.append(arrr1[x])
                x+=1
            else:
                arrr3.append(arrr2[y])
                y+=1
    if y<len2:
        arrr3.extend(arrr2[y:])
    elif x<len1:
        arrr3.extend(arrr2[x:])

    file2.write(" ".join(arrr3))
    file2.close()

task2_1()
task2_2()

