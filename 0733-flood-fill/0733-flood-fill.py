from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color: return image

        m = len(image); n = len(image[0]); target = image[sr][sc]
        def fill(h, w):
            if image[h][w] == target:
                image[h][w] = color
                if h > 0: fill(h-1, w)
                if h < m - 1: fill(h+1, w)
                if w > 0: fill(h, w-1)
                if w < n - 1: fill(h, w+1)
        
        fill(sr, sc)
        return image