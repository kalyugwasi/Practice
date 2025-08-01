#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        res = 1
        nai = collection.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nai[pattern].append(word)
        visit = set([beginWord])
        q = deque([beginWord])
        while q:
            for i in range(len(q)):
                if word == endWord:
                    return res
                 for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for naiWord in nai[pattern]:
                        if naiWord not in visit:
                            visit.add(naiWord)
                            q.append(naiWord)
            r += 1
        return 0

        
# @lc code=end

