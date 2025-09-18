#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row,col= len(mat),len(mat[0])
        res = []
        crow,ccol = 0,0
        goin = True
        while len(res) != row*col:
            if goin:
                while crow>=0 and ccol < col:
                    res.append(mat[crow][ccol])
                    crow -= 1
                    ccol += 1
                if ccol == col:
                    ccol -=1
                    crow +=2
                else:
                    crow+=1
                goin = False
            else:
                while crow<row and ccol >=0:
                    res.append(mat[crow][ccol])
                    crow +=1
                    ccol -=1
                if crow == row:
                    ccol +=2 
                    crow -=1
                else:
                    ccol +=1
                goin = True
        return res


# @lc code=end

