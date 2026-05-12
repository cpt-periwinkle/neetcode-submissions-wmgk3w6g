# Topo Sort
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # Build adjacency list:
        # adj[a] contains all characters that must come AFTER 'a'
        #
        # Example:
        # "wrt" -> "wrf"
        # First different character is:
        # t -> f
        #
        # So:
        # adj['t'] = {'f'}
        adj = {c: set() for w in words for c in w}

        # Compare adjacent words to discover ordering rules
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Only compare up to the smaller word length
            minLen = min(len(w1), len(w2))

            # Invalid case:
            #
            # Example:
            # ["abc", "ab"]
            #
            # If two words share the same prefix,
            # the shorter word must come first.
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Find the FIRST different character
            #
            # That difference determines the ordering rule.
            for j in range(minLen):

                if w1[j] != w2[j]:

                    # Example:
                    # "wrt"
                    # "wrf"
                    #
                    # t must come before f
                    adj[w1[j]].add(w2[j])

                    # Only the first difference matters
                    break

        # visited states:
        #
        # True  -> currently in DFS path (cycle detection)
        # False -> fully processed already
        visited = {}

        # Stores characters in reverse topological order
        res = []

        def dfs(char):

            # If character already seen:
            #
            # True  -> cycle found
            # False -> already processed safely
            if char in visited:
                return visited[char]

            # Mark character as currently being explored
            visited[char] = True

            # Visit all characters that must come after current char
            for neighChar in adj[char]:

                # If neighbor DFS detects a cycle,
                # propagate failure upward
                if dfs(neighChar):
                    return True

            # Exploration finished safely,
            # so mark as fully processed
            visited[char] = False

            # Add character AFTER exploring neighbors.
            #
            # This is topological sort via postorder DFS.
            res.append(char)

        # Run DFS from every character
        #
        # Graph may be disconnected.
        for char in adj:

            # If a cycle exists,
            # no valid ordering is possible
            if dfs(char):
                return ""

        # Result was built backwards during DFS postorder
        res.reverse()

        # Convert list of chars into final string
        return "".join(res)