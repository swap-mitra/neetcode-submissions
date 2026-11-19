import heapq
from collections import defaultdict
from typing import List, Dict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {}
        heap = [(0, src)]
        while heap:
            d, node = heapq.heappop(heap)
            if node in dist:
                continue
            dist[node] = d
            for nei, w in adj[node]:
                if nei not in dist:
                    heapq.heappush(heap, (d+w, nei))

        for i in range(n):
            if i not in dist:
                dist[i] = -1
        return dist
