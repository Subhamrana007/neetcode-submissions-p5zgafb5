class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] != s[right]:
                L_str, r_str = s[left : right], s[left+1 : right+1]

                return (L_str == L_str[::-1] or r_str == r_str[::-1])
            left += 1
            right -= 1
        return True        