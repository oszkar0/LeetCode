class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        visited = {}

        for gene in bank:
            visited[gene] = False

        queue = [(start, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr == end:
                return level

            for i in range(len(curr)):
                for char in 'ACGT':
                    if char == curr[i]:
                        continue
                    
                    next = curr [:i] + char + curr[i + 1:]

                    if next in visited and not visited[next]:
                        queue.append((next, level + 1))
                        visited[next] = True
                    
        return -1