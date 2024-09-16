import sys;input = sys.stdin.readline
line_list = []
for _ in range(int(input())) :
    line_list.append(list(map(int, input().split())))

line_list.sort()
min_x, max_y = line_list[0][0], line_list[0][1]
line_length = 0
for i in range(1,len(line_list)) :
    if max_y >= line_list[i][1] : continue
    elif max_y >= line_list[i][0] : max_y = line_list[i][1]
    else :
        line_length += (max_y - min_x)
        min_x, max_y = line_list[i][0], line_list[i][1]
print(line_length + (max_y - min_x))