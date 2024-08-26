class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.prefix_sum[r][c] += matrix[r][c]
                
                if r > 0:
                    self.prefix_sum[r][c] += self.prefix_sum[r-1][c]
                if c > 0:
                    self.prefix_sum[r][c] += self.prefix_sum[r][c-1]
                if r > 0 and c > 0:
                    self.prefix_sum[r][c] -= self.prefix_sum[r-1][c-1]
        
       
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        current = self.prefix_sum[row2][col2]
        print(current)
        if row1 > 0:
            current -= self.prefix_sum[row1 -1][col2]
        if col1 > 0:
            current -= self.prefix_sum[row2][col1 -1]
        if row1 > 0 and col1 > 0:
            current += self.prefix_sum[row1-1][col1-1]
        return current


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)