import sys # 시간 초과 나서 추가
from collections import Counter
# 최빈값을 구할때 Counter함수를 사용하지않으니 시간초과

n = int(sys.stdin.readline())

numbers = []

for i in range(n):
    numbers.append(int(sys.stdin.readline()))

def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    mid = nums[len(nums)//2] # why [], // ?
    return mid

def frequency(nums):
    mode_dict = Counter(nums)
    frequencys = mode_dict.most_common()

    if len(nums) > 1 : #만약 입력값이 하나면 , 그게 최빈값이 되므로 예외처리
        if frequencys[0][1] == frequencys[1][1] :
            mod = frequencys[1][0]
        # 최빈값의 빈도수를 비교하여, 2개이상의 최빈값이 있으면 두번째로 작은것을 출력
        else:
            mod = frequencys[0][0]
    else:
        mod = frequencys[0][0]

    return mod

def scope(nums):
    return max(nums) - min(nums)


print(mean(numbers))
print(median(numbers))
print(frequency(numbers))
print(scope(numbers))