class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        if not strs:
            return ""
        strs.sort(key=len)
        for c in range(1,len(strs[0])+1):
            for s in range(0,len(strs)):
                if s == 0:
                    pre = strs[s][:c]
                if strs[s][:c] != pre:
                    break
            else:
                lcp = pre
        return lcp
