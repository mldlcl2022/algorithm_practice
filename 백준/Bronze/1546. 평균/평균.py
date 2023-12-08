# 과목의 개수 n
n = int(input())

# 세준이의 실제 성적
score = [int(i) for i in input().split()][:n]

# 세준이의 최고 점수(최댓값)
m = max(score)

# 점수 조작 결과
print(sum([i/m*100 for i in score])/n)