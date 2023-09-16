# 대표적인 최소 신장 트리 알고리즘
"""
1. 간선 데이터를 비용에 따라 오름 차순으로 정렬
2. 간선들을 하나씩 확인하며 현재 간선이 사이클을 발생시키는지 확인
    - 사이클이 발생하지 않는 경우 최소 신장 트리에 포함
    - 사이클이 발생하는 경우 최소 신장 트리에 포함 시키지 않음
3. 모든 간선에 대하여 2번 과정 반복
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
