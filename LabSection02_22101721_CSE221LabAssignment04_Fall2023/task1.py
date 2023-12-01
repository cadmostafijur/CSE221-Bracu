##################(  1A )##################

file1 = open("input1a.txt", "r")
file2 = open("output1a.txt", "w")
inp = file1.read().split("\n")
file1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])
matrix = [[0 for i in range(nodes+1)] for i in range(nodes+1)]
for i in range(1, len(inp), 1):
  info = inp[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  cost = int(info[2])
  matrix[node1][node2] = cost
for i in range(len(matrix)):
  line = map(str, matrix[i])
  line = " ".join(list(map(str, line)))
  file2.write(line)
  if i<len(matrix)-1:
    file2.write('\n')
file2.close()

##################(  1B )##################

file1 = open("input1b.txt", "r")
file2 = open("output1b.txt", "w")

inp = file1.read().split("\n")
file1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])
dic = {i:[] for i in range(nodes+1)}
for i in range(1, len(inp), 1):
  info = inp[i].split(" ")
  node1 = int(info[0])
  node2 = int(info[1])
  cost = int(info[2])
  arr = dic[node1]
  arr.append((node2, cost))
vals = list(dic.values())
for i in range(len(vals)):
  file2.write(str(i)+' : '+" ".join(list(map(str, vals[i]))))
  if i<len(vals)-1:
    file2.write('\n')
file2.close()
#========== Task 1A ==========#
# Here, we get the number of nodes and vertices from the input file
# and build an empty matrix based on them. Then we iterate through 
# the rest of the input file to get first node, second node and the 
# cost between them. Then this cost is set in the matrix for the two
# nodes in this way matrix [node ][node2] = cost
#========== Task 1B ==========#
# Based on the number of nodes and points in the input file, we build 
# an empty dictionary with empty lists, just like in task1A. In the 
# dictionary, the array of node 1 is updated with the value of node 2 
# and the cost from node 1 for each setup in the input file. 

