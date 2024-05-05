# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color.
# You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
# Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.
image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
color = 2


class Solution(object):
    def floodFill(self, image, sr, sc, color):

        selected_color = image[sr][sc]
        self.dfs(image, sr, sc, color, selected_color)
        return image

    def dfs(self, image, sr, sc, color, selected_color):

        if sr < 0 or sr > len(image)-1 or sc < 0 or sc > len(image[0]) - 1 or image[sr][sc] != selected_color or image[sr][sc] == color:
            return

        image[sr][sc] = color

        self.dfs(image, sr-1, sc, color, selected_color)
        self.dfs(image, sr+1, sc, color, selected_color)
        self.dfs(image, sr, sc-1, color, selected_color)
        self.dfs(image, sr, sc+1, color, selected_color)
