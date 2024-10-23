import sys;input = sys.stdin.readline
from collections import deque
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0]
dy = [0,1]
visited = [[False]*n for _ in range(n)]
def BFS(x,y) : # start x,y
    queue = deque()
    queue.append((x,y))
    while queue :
        x,y = queue.popleft()
        if matrix[x][y] == -1 : # 승리 지점 = -1
            return True
        for move in range(2) :
            nx = x + dx[move]*matrix[x][y]
            ny = y + dy[move]*matrix[x][y]
            if nx < 0 or nx >= n or ny < 0 or ny >= n : continue # 범위 벗어나면 무시
            if not visited[nx][ny] : # 방문하지 않았다면
                visited[nx][ny] = True # 방문 처리
                queue.append((nx,ny)) # 다음 스텝을 위해 저장
if BFS(0,0) : print('HaruHaru')
else : print('Hing')