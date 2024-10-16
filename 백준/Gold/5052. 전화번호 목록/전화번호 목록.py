import sys;input = sys.stdin.readline
for _ in range(int(input())) :
    nums = []
    for _ in range(int(input())) :
        nums.append(input().rstrip())
    nums.sort()
    result = 'YES'
    for i in range(len(nums)-1) :
        if nums[i+1].startswith(nums[i]) :
            result = 'NO'
            break
    print(result)