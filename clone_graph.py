
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        copy_mapping = {}

        def dfs_aka_clone(node):
            if node in copy_mapping:
                return copy_mapping[node]
            
            copy = Node(node.val)
            copy_mapping[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs_aka_clone(nei))
            
            return copy

        return dfs_aka_clone(node)


            
        