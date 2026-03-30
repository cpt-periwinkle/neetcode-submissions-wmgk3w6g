class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26

        for ch in s1:
            idx = ord(ch) - ord('a')
            s1_count[idx] += 1
        
        left = 0
        s2_count = [0] * 26
        for right in range(len(s2)):
            right_idx = ord(s2[right]) - ord('a')
            s2_count[right_idx] += 1

            while ((right - left + 1) > len(s1)):
                left_idx = ord(s2[left]) - ord('a')
                s2_count[left_idx] -= 1
                left += 1
            
            if s1_count == s2_count:
                return True
        
        return False
            
