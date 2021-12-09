input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0] # 어차피 배열에 초기값을 비교해야하니 0을 넣어준것
    for num in array:
        if num > max_num:
            max_num = num

        return max_num

result = find_max_num(input)
print(result)