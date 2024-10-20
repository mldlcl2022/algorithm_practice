from collections import deque
def BFS(x,y) :
    queue = deque()
    queue.append((x,y))
    while queue :
        cx,cy = queue.popleft()
        for i in range(4) :
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m : continue
            if maze[nx][ny] == 0 : continue
            if maze[nx][ny] == 1 :
                maze[nx][ny] = maze[cx][cy] + 1
                queue.append((nx,ny))
    return maze[n-1][m-1]

import sys;input = sys.stdin.readline
n,m = map(int, input().split())
maze = [list(map(int, list(str(input().rstrip()))))[:m] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(BFS(0,0))