class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        parens = []
        for c in s:
            if c in ['(', '{', '[']:
                parens.append(c)            
            if c in [')', '}', ']']:
                if not parens:
                    return False
                p = parens.pop()
                if c != close[p]:
                    return False
        return not parens
