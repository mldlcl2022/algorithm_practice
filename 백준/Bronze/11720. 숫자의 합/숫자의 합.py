# 숫자의 개수 n 입력
n = int(input())

# n개 숫자의 합 출력
print(sum([int(i) for i in input()[:n]]))