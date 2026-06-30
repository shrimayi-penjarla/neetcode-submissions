class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        for i in range(len(mat)):
            #primary diagonal
            sum += mat[i][i]
            sum += mat[i][len(mat)-i-1]
        if (len(mat)%2==1):
            half = (int) (len(mat))//2
            sum -= mat[half][half]
        return sum

        