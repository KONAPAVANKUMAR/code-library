INF = float("inf")

def min_cost(cost):
    n = len(cost)
    dist = [INF] * n
    dist[0] = 0  
    for i in range(n):
        for j in range(i+1,n):
            dist[j] = min(dist[j], dist[i] + cost[i][j])
    return dist[n-1]