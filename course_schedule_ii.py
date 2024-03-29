class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: [] for i in range(numCourses)}
        output = [] 
        cycle = set()
        visited = set()

        for c, p in prerequisites:
            graph[c].append(p)


        def dfs(c):
            if c in cycle:
                return False

            if c in visited:
                return True

            cycle.add(c)
            for nei in graph[c]:
                if not dfs(nei):
                    return False
            output.append(c)
            visited.add(c)
            cycle.remove(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return output

        
        