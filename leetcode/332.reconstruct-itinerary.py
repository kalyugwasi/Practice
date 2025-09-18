#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        tickets.sort(reverse=True)
        for src, dest in tickets:
            adj[src].append(dest)
        res = []
        def dfs(src):
            while adj[src]:
                next_dest = adj[src].pop()
                dfs(next_dest)
            res.append(src)
        dfs("JFK")
        return res[::-1]
        
# @lc code=end

