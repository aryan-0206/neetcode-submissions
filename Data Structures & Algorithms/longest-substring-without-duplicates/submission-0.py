class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):

            #Remove Duplicate Characters
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            #Add CCurrent Character
            seen.add(s[right])

            #Calculate Window Lenght
            length = right - left + 1

            max_len = max(max_len, length)
        return max_len