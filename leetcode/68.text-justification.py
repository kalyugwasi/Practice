#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line,llen = [],0
        i = 0
        while i<len(words):
            if llen + len(line) + len(words[i]) > maxWidth:
                es = maxWidth-llen
                space = es//max(1,len(line)-1)
                rem = es%max(1,len(line)-1)
                for j in range(max(1,len(line)-1)):
                    line[j] += " "*space
                    if rem:
                        line[j] += " "
                        rem -= 1
                res.append("".join(line))
                line,llen = [],0
                continue
            line.append(words[i])
            llen += len(words[i])
            i += 1
        last_line = " ".join(line)
        trail = maxWidth - len(last_line)
        res.append(last_line+" "*trail)
        return res       
# @lc code=end

