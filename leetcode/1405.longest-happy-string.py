#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        store = {"a":a,"b":b,"c":c}
        filt = [[-val,key] for key,val in store.items() if val != 0]
        heapq.heapify(filt)
        while filt:
            count,char = heapq.heappop(filt)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not filt:
                    break
                count2,char2 = heapq.heappop(filt)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(filt,[count2,char2])
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(filt,[count,char])  
        return res
        
# @lc code=end

