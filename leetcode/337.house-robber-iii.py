#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0,0]
            leftpair = dfs(root.left)
            rightpair = dfs(root.right)
            withroot = root.val + leftpair[1] + rightpair[1]
            withoutroot = max(leftpair) + max(rightpair)
            return [withroot,withoutroot]
        return max(dfs(root))
# @lc code=end

