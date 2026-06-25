class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        temp_set = set()
        longest = 0
        n = len(s)

        for r in range(n):
            while(s[r] in temp_set):
                temp_set.remove(s[l])
                l+=1

            w = (r - l) +1
            longest = max(longest, w)
            temp_set.add(s[r])

        return longest





