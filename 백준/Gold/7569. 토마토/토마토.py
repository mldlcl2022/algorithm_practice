import sys;input = sys.stdin.readline
from collections import deque
n,m,h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]

queue = deque()
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
visited = [[[0]*n for _ in range(m)] for _ in range(h)]
count = 0

for z in range(h) :
    for y in range(m) :
        for x in range(n) :
            if matrix[z][y][x] == 1 :
                queue.append((x,y,z))
                visited[z][y][x] = 1
            if matrix[z][y][x] == 0 :
                count += 1

while queue :
    x,y,z = queue.popleft()
    for i in range(6) :
        nx,ny,nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and visited[nz][ny][nx] == 0 and matrix[nz][ny][nx] == 0 :
            queue.append((nx,ny,nz))
            visited[nz][ny][nx] = visited[z][y][x]+1
            count -= 1

if not count : print(visited[z][y][x]-1)
else : print(-1)