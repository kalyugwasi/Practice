#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(r):
            if root == None:
                return 0
            if not r.children:
                return 1
            return 1 + max(dfs(i) for i in r.children)
        return dfs(root)
# @lc code=end

