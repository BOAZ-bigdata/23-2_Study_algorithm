import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for i in range(n+1)]
answer = []
visited = [-1] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_Node = queue.popleft()
        for i in graph[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node] + 1
                queue.append(i)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

BFS(x)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)