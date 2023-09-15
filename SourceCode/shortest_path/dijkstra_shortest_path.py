# 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘
"""
1. 출발 노드 설정
2. 최단 거리 테이블을 초기화
3. 방문하지 않은 노드 중에서 최단 거리가 짧은 노드를 선택
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리를 갱신
5. 3번과 4번을 반복
"""
import heapq

def dijkstra_shortest_path(start):
    q = []
    heapq.heappush(q, (0, start))
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(cost, i[0])

# input
n, m = map(int, input().split)
distance = [int(1e9)] * (n + 1)
graph = [[] for i in range(n+1)]