# 입력받을 초기 리스트 생성
num_list = []

# 나머지를 구할 값 입력
for _ in range(10) :
    num_list.append(int(input()))

# 42로 나눈 나머지로 다시 저장
for i, num in enumerate(num_list) :
    num_list[i] = num%42

# 입력받은 값을 42로 나눈 나머지들의 서로 다른 값 개수
print(len(set(num_list)))