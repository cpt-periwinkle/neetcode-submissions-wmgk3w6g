class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # How many of each character does s1 need?
        freq = {}
        for c in s1:
            freq[c] = 1 + freq.get(c, 0)

        # need = number of unique characters we need to satisfy
        # act  = number of unique characters currently satisfied in window
        need = len(freq)
        act = 0

        count = {}  # character frequencies in current window
        l = 0

        for r in range(len(s2)):
            # Add s2[r] into the window
            count[s2[r]] = 1 + count.get(s2[r], 0)

            # Did adding s2[r] just satisfy its required frequency?
            if s2[r] in freq and count[s2[r]] == freq[s2[r]]:
                act += 1
            # Did adding s2[r] push it one over the required frequency?
            # That means it was satisfied before, now it's exceeded → lose a match
            elif s2[r] in freq and count[s2[r]] == freq[s2[r]] + 1:
                act -= 1

            # Window too big — shrink from left
            if r - l + 1 > len(s1):
                # Before removing s2[l], check how it affects act
                if s2[l] in freq and freq[s2[l]] == count[s2[l]]:
                    # s2[l] was exactly satisfied — removing it breaks the match
                    act -= 1
                elif s2[l] in freq and freq[s2[l]] + 1 == count[s2[l]]:
                    # s2[l] was one over required — removing it brings it back to exact match
                    act += 1
                count[s2[l]] -= 1
                l += 1

            # All unique characters in s1 are satisfied → valid permutation found
            if act == need:
                return True

        return False