import sys;input = sys.stdin.readline
from collections import deque

m,n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
for i in range(n) :
    for j in range(m) :
        if matrix[i][j] == 1 :
            queue.append([i,j])

x,y = [-1,1,0,0],[0,0,-1,1]
while queue :
    pop_x,pop_y = queue.popleft()
    for i in range(4) :
        nx,ny = x[i]+pop_x, y[i]+pop_y
        if 0 <= nx < n and 0 <= ny < m :
            if matrix[nx][ny] == -1 : continue
            elif matrix[nx][ny] == 0 :
                queue.append([nx, ny])
                matrix[nx][ny] = matrix[pop_x][pop_y]+1

result = 0
for row in range(n) :
    for col in range(m) :
        if matrix[row][col] == 0 :
            result = -1
            break
if result == -1 : print(result)
else : print(max(map(max, matrix))-1)