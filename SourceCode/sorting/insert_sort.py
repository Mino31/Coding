# 삽입 정렬 : 특정한 데이터를 적절한 위치에 삽입
def select_sort(array):

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j-1], array[j]
            else:
                break

    return array