# 선택 정렬 : 가장 원시적인 방법으로 매번 가장 작은 것을 선택

def select_sort(array):

    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array
