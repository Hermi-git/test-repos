class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # x_coords = [point[0] for point in points]
        # for i in range(len(x_coords)):
        #     min_idx = i
        #     for j in range(i+1, len(x_coords)):
        #         if x_coords[j] < x_coords[min_idx]:
        #             min_idx = j
        #     x_coords[i], x_coords[min_idx] = x_coords[min_idx], x_coords[i]

        # diff = 0
        # for i in range(1, len(x_coords)):
        #     diff = max(diff, x_coords[i] - x_coords[i-1])
        # return diff

        x_coords = [point[0] for point in points]
        x_coords = sorted(x_coords)
        diff = 0
        for i in range(1, len(x_coords)):
            diff = max(diff, x_coords[i] - x_coords[i-1])
        return diff


        # for i in range(len(points)):
        #     mini = i
        #     for j in range(i+1, len(points)):
        #         if points[j][0] < points[mini][0]:
        #             mini = j
        #     if i != mini:
        #         points[i][0], points[mini][0] = points[mini][0], points[i][0]
        # diff = 0
        # for i in range(1, len(points)):
        #     diff = max(diff, points[i][0] - points[i-1][0])
        # return diff


        