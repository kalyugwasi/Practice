#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visit = []
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            visit.append(root.val)
            dfs(root.right)
        dfs(root)
        return visit
# @lc code=end

