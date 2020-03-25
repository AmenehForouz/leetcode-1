class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        
        for i in range(1, len(points)):
            x_dist = abs(points[i][0] - points[i-1][0])
            y_dist = abs(points[i][1] - points[i-1][1])
            
            if x_dist >= y_dist:
                time += x_dist
            else:
                time += y_dist
        
        return time