class Solution:
    def checkInclusion(self, s1: str, s2: str):
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26         # frequency count of characters in s1
        s2_count = [0] * 26         # frequency count of characters in current window of s2

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1    # build frequency count for s1
            s2_count[ord(s2[i]) - ord('a')] += 1    # build frequency count for first window of s2

        matches = 0                 # number of positions where s1_count[i] == s2_count[i]
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):   # slide the window one step at a time
            if matches == 26:                   # all 26 counts match, so current window is a permutation
                break

            index = ord(s2[right]) - ord('a')   # character entering the window
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1                    # this character count now matches
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1                    # this character count matched before, but adding one broke it

            index = ord(s2[left]) - ord('a')    # character leaving the window
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1                    # removing restored the match
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1                    # removing broke a previous match

            left += 1

        return matches == 26                    # true if every character frequency matches