class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln_map = dict()
        for word in strs:
            count = [0] * 26
            for ltr in word:
                count[ord(ltr) - ord('a')] += 1

            key = tuple(count)
            if key in soln_map:
                soln_map[key].append(word)
            else:
                soln_map[key] = [word]

        return list(soln_map.values())
        
        