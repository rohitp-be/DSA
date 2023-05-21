class Graph:
    def __init__(self, row, col, g):
        self.graph = g
        self.row = row
        self.col = col

    def isSafe(self, i, j, visited):
        return (i >= 0 and i< self.row and j >= 0 and j < self.col and not visited[i][j] and self.graph[i][j])

    def dfs(self, i, j, visited):
        newrow = [-1,-1,-1,0,0,1,1,1]
        newcol = [-1,0,1,-1,1,-1,0,1]
        visited[i][j] = True
        for k in range(8):
            if self.isSafe(i+newrow[k], j+newcol[k], visited):
                self.dfs(i+newrow[k], j+newcol[k], visited)
    
    def numsofIslands(self):
        visited = [[False for i in range(self.col)] for j in range(self.row)]
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    self.dfs(i,j, visited)
                    count += 1
        return count
# grid = [[0,1],[1,0],[1,1],[1,0]]
grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

graph = Graph(len(grid), len(grid[0]),grid)
print(graph.numsofIslands())