# 계수 정렬 :
'''
특정 조건이 부합때만 사용
데이터의 차이가 1000000이 넘지 않을때 효과적으로 사용

모든 범위를 담을 수 있는 크기의 리스트를 선언
'''


def count_sort(array):
    result = []
    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            result.appned(i)

    return result