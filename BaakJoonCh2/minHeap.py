import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap: # 빈배열이 아니라면 최소값을 출력 후 삭제(heappop)
            print(heapq.heappop(heap))
        else: # 배열이 빈배열이면 0을 출력
            print('0')
    else:
        heapq.heappush(heap, x)