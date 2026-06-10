class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        int = 0

        for i in range(len(s)):
            if i < len(s) - 1 and values[s] < values[s+1]:
                int -= values[s]
            else:
                int += values[s]
        return int

