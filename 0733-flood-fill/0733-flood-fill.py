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
        target = image[sr][sc]
        if target == color: return image

        m = len(image); n = len(image[0])
        stack = deque(); stack.append((sr, sc)); image[sr][sc] = color
        while stack:
            h, w = stack.pop()
            if h > 0 and image[h-1][w] == target:
                image[h-1][w] = color
                stack.append((h-1, w))
            if h < m - 1 and image[h+1][w] == target:
                image[h+1][w] = color
                stack.append((h+1, w))
            if w > 0 and image[h][w-1] == target:
                image[h][w-1] = color
                stack.append((h, w-1))
            if w < n - 1 and image[h][w+1] == target:
                image[h][w+1] = color
                stack.append((h, w+1))

        return image
            