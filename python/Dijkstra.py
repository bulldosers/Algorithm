import heapq

def dijkstra(G, n, start, end):
    dis = [999999999999999]* n
    dis[start] = 0
    vis = [False] * n
    pq = []
    heapq.heappush(pq, [dis[start], start])
    while len(pq)>0:
        v_dis, v = heapq.heappop(pq)
        print
        if vis[v] == True:
            continue
        vis[v] = True
        for node, edge_dis in G[v]:
            new_dis = dis[v] + edge_dis
            if new_dis < dis[node] and (not vis[node]):
                dis[node] = new_dis
                heapq.heappush(pq, [dis[node],node])
    return dis[end]

def judge(input_list, n, m, k, s, t, mid):
    G = [[] for i in range(n)]
    for x in input_list:
        if x[-1] <= mid:
            G[x[0]].append((x[1], x[2]))
    return dijkstra(G, n, s, t) <= k

n, m, k, s, t = map(int, input().split())
input_list = [0] * m
s-=1
t-=1
min_t = 0
max_t = 0
for i in range(m):
    input_list[i] = list(map(int, input().split()))
    input_list[i][0] -= 1
    input_list[i][1] -= 1
    if input_list[i][-1] > max_t:
        max_t = input_list[i][-1]

# if s == t:
#     print (0)
# elif not judge(input_list, n, m, k, s, t, max_t):
#     print (-1)
# else:
#     for i in range(23333):
#         if max_t == min_t:
#             break
#         mid = int((min_t+max_t)/2)
#         if judge(input_list, n, m, k, s, t, mid):
#             max_t = mid
#         else:
#             min_t = mid+1
#     print (max_t)