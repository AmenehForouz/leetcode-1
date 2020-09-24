"""
Problem 1266 - Minimum Time Visiting All Points

On a plane there are n points with integer coordinates points[i] = [xi, yi]. 
Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

- In one second always you can either move vertically, horizontally by one 
  unit or diagonally (it means to move one unit vertically and one unit 
  horizontally in one second).

- You have to visit the points in the same order as they appear in the array.
"""

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0

        for i in range(1, len(points)):
            x_dist = abs(points[i][0] - points[i - 1][0])
            y_dist = abs(points[i][1] - points[i - 1][1])

            if x_dist >= y_dist:
                time += x_dist
            else:
                time += y_dist

        return time


if __name__ == "__main__":
    # Should return 7
    print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))

    # Should return 5
    print(Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]]))
