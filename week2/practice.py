arr = input() #처음 문자열
search = input() #찾을 문자열
n = len(arr)
m = len(search)

def BruteForce(search,arr):
    i =0 #arr의 인덱스
    j =0 #search 의 인덱스
    while j < m and i<n: #각 인덱스가 길이보다 짧은동안
        if arr[i]!=search[j]: #만약에 다른경우
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == m :
        return i-m
    else:
        return -1

print(BruteForce(search,arr))

