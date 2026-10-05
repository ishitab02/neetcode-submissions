class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #initialise
        left = right = 0
        seen = set()
        max_length = 0

        #loop
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            current_length = right - left + 1
            max_length = max(current_length, max_length)

        return max_length