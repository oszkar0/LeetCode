class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []

        def backtrack(start, curr_comb):
            if len(curr_comb) == k:
                output.append(curr_comb[:])
                return

            for num in range(start, n + 1):
                curr_comb.append(num)
                backtrack(num + 1, curr_comb)
                curr_comb.pop()

        backtrack(1, [])
        return output