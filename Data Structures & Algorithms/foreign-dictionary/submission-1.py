class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            min_len = min(len(w1), len(w2))
            
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            
        res = []
        visit = {}

        def dfs(ch):
            if ch in visit:
                return visit[ch]
            
            visit[ch] = True
            for child in adj[ch]:
                if dfs(child):
                    return True
            visit[ch] = False
            res.append(ch)

        for ch in adj:
            if dfs(ch):
                return ""
        
        res.reverse()
        return "".join(res)