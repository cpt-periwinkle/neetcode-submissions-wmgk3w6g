class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        s_dict = dict()
        t_dict = dict()
        for index in range(len(s)):
            if s[index] in s_dict:
                s_dict[s[index]] += 1
            else:
                s_dict[s[index]] = 1
            
            if t[index] in t_dict:
                t_dict[t[index]] += 1
            else:
                t_dict[t[index]] = 1

        return s_dict == t_dict
