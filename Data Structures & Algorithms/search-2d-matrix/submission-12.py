class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #need to find if a value exists in a 2D matrix
        #idea: we should jump to the last value of every row starting from the first row
            #if the value is less than the value in the row but greater than the previous row, we should keep checking for it, otherwise check the next row
        ROWS, COLS = len(matrix), len(matrix[0])
        #use binary for the rows first, finding the most appropriate row
        top, bot = 0, ROWS-1
        while top <= bot:
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        #find the best row and then the best column
        row = (top + bot)//2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l+r)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False

            