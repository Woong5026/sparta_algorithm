import collections
a  = [1,1,1,2,3,2,3,245,9]

print(collections.Counter(a).most_common(5))

# a에서 요소들의 개수를 세어, 딕셔너리 형태로 반환합니다.  {문자 : 개수} 형태

# b = [1,3,4,2,3,5,2,3,9]
# a = [1,2,3,4,1,5,3,1,3,4,2,3]
# print(collections.Counter(a) , collections.Counter(b))