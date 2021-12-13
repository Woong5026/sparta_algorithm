def solution(board, moves):
    answer = 0
    bucket = []

    # moves를 통해서 어떤 컬럼을 조회할 건지 반복문을 통해 조회
    for move in moves:
        index = move - 1  # move는 번째 이니 컬럼 -1을 해준다
        # board 역시 비었는지 아닌지를 확인
        for row_info in board:
            if row_info[index] != 0:
                bucket.append(row_info[index])
                row_info[index] = 0  # 0으로 뽑은 인덱스 초기화

                if len(bucket) >= 2 and bucket[-1] == bucket[-2]:
                    answer += 2
                    bucket = bucket[0:-2]
                break  # 꼭대기만 뽑아오면 되는 것이기에 뒤에것을 찾지 않고 break
    return answer