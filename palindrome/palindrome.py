class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reverse = str_x[::-1]
        if reverse == str_x:
            return True
        else:
            return False

