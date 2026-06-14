class Solution:
    def maxDistinct(self, s: str) -> int:
        distinct = set()
        for c in s:
            if c not in distinct:
                distinct.add(c)
        return len(distinct)
