
from itertools import product


maxArea = 0
rows = 0
cols = 0
# def maxAreaOfIsland(grid):
#     global maxArea
#     for i in range(rows):
#         for j in range(cols):
#             if visited[i][j] == 1 or grid[i][j] == 0:
#                 visited[i][j] = 1
#             else:
#                 x = getmax(i, j)
#                 if x > maxArea:
#                     maxArea = x
#     return maxArea
# def isSafe(i, j):
#     if i < 0 or j < 0 or i > rows or j > cols:
#         return False
#     else:
#         return True

# def getmax(row, col):
#     vals = [[row-1, col],[row+1, col],[row, col-1],[row, col+1]]
#     sum = 0
#     if grid[row][col] == 0 or visited[row][col] == 1:
#         return 0
#     else:
#         for k in vals:
#             if isSafe(k[0],k[1]) and grid[k[0]][k[1]] == 1:
#                 visited[k[0]][k[1]]=1
#                 sum +=  getmax(k[0],k[1])
#             visited[k[0]][k[1]]=1
#         return sum
#     return 1


def maxAreaOfIsland(grid) -> int:
    ans, n, m = 0, len(grid), len(grid[0])
    def trav(i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == 0: return 0
        grid[i][j] = 0
        return 1 + trav(i-1, j) + trav(i, j-1) + trav(i+1, j) + trav(i, j+1)
    for i, j in product(range(n), range(m)):
        if grid[i][j]: ans = max(ans, trav(i, j))
    return ans
            




grid = [[0,0,1,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
rows = len(grid)
    
if rows > 0:
    cols = len(grid[0])
visited = [[0 for j in range(cols)] for i in range(rows)]
print(maxAreaOfIsland(grid))