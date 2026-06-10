class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        number = x
        rev = 0
        while number != 0:
            rev = rev * 10 + number % 10
            number = number // 10
        return rev == x
