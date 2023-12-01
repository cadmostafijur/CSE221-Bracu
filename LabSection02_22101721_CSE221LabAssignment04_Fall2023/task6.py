def dfs_floodfill(r, c, rows, cols, G): 
    if r < 0 or r >= rows or c < 0 or c >= cols or G[r][c] == '#':
        return 0
    cnt = 0
    if G[r][c] == 'D':
        cnt += 1
    G[r][c] = '#'
    cnt += dfs_floodfill(r + 1, c, rows, cols, G)
    cnt += dfs_floodfill(r - 1, c, rows, cols, G)
    cnt += dfs_floodfill(r, c + 1, rows, cols, G)
    cnt += dfs_floodfill(r, c - 1, rows, cols, G)
    return cnt
#count  diamonds function
def cntdiamonds(rows, cols, G):
    maxdiamond = 0
    for r in range(rows):
        for c in range(cols):
            if G[r][c] == '.':
                diamond = dfs_floodfill(r, c, rows, cols, G)
                maxdiamond = max(maxdiamond, diamond)
    return maxdiamond
file1 = open("input6.txt", "r")
file2 = open("output6.txt", "w")
lines = file1.read().split("\n")
x,y = map(int, lines[0].split())#the number of rows and columns
z = [list(line) for line in lines[1:]]
result = cntdiamonds(x,y, z)
file2.write(str(result))
file2.close()
# 12 12
# ............
# .####.......
# .#D.#.......
# .####.......
# ........###.
# ...D....#D#.
# ........#D#.
# .########D#.
# .#D....##.#.
# .#.D..D##D#.
# .##########.
# ............


#========== Task 6 ==========#
# We use recursive DFS to explore the jungle.
# It starts from a cell and traverses the neighbour
# cells in all directions. The encountered diamonds
# are added to diamond count(cnt) variable. The visited 
# cells are marked to prenent backtracking.
# are obstacles and are avoided. 
# The count Diamonds function iterates through all cells, 
# calling DFS FloodFill for all empty (1) cells to find the
# maximum diamonds. The maximum of this result is stored.