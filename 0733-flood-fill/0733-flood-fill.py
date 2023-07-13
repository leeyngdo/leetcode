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
        m = len(image); n = len(image[0]); target = image[sr][sc]
        if target == color: return image

        queue = deque(); queue.append((sr, sc)); image[sr][sc] = color
        while queue:
            h, w = queue.popleft()
            if h > 0 and image[h-1][w] == target:
                image[h-1][w] = color
                queue.append((h-1, w))
            if h < m - 1 and image[h+1][w] == target:
                image[h+1][w] = color
                queue.append((h+1, w))
            if w > 0 and image[h][w-1] == target:
                image[h][w-1] = color
                queue.append((h, w-1))
            if w < n - 1 and image[h][w+1] == target:
                image[h][w+1] = color
                queue.append((h, w+1))

        return image
            