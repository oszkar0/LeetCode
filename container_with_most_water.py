# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(curr_area, max_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

    def test(self):
        height = [1,8,6,2,5,4,8,3,7]
        expected_area = 49
        actual_area = self.maxArea(height)

        if actual_area == expected_area:
            print('Test passed!')
        else:
            print('Test failed!')


        
if __name__ == '__main__':
    solution = Solution()
    solution.test()
        