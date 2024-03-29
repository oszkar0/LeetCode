class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = set()
        graph = {i: [] for i in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)

        def dfs(c):
            if c in visited:
                return False
            
            if graph[c] == []:
                return True

            visited.add(c)

            for nei in graph[c]:
                if not dfs(nei):
                    return False
                
            graph[c] = []
            visited.remove(c)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 