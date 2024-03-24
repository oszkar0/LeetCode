class Solution(object):
    def findMinArrowShots(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: int
        """
        segments.sort(key=lambda p: p[1])
        arrows = 0
        last_arrow = 0
        for start, end in segments:
            # from the 2-nd segment, we check whether the current arrow pass through the current segment, if not add an arrow, put it at the end of the current segment
            if arrows == 0 or start > last_arrow:
                arrows += 1
                last_arrow = end
        
        return arrows

        