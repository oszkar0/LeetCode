class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = collections.defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append([b, values[i]])
            graph[b].append([a, 1 / values[i]])

        def bfs(src, target):
            if src not in graph or target not in graph:
                return -1
        
            q = collections.deque()
            visited = set()
            q.append([src, 1])
            visited.add(src)

            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                
                for nei, nei_w in graph[n]:
                    if nei not in visited:
                        q.append([nei, w * nei_w])
                        visited.add(nei)

            return -1


        return [bfs(q[0], q[1]) for q in queries]