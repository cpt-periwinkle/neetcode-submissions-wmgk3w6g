class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes
        # Key = character, Value = TrieNode
        self.children = {}
        
        # True if a word ends at this node
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        # Root node does not store any character
        self.root = TrieNode()


    # ---------------- ADD WORD ----------------
    # Insert a word into the Trie
    def addWord(self, word: str) -> None:
        curr = self.root  # Start from root
        
        # Traverse each character in the word
        for ch in word:
            # If path doesn't exist, create a new node
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            # Move to the next node
            curr = curr.children[ch]
        
        # Mark the end of the word
        curr.endOfWord = True


    # ---------------- SEARCH ----------------
    # Search word in Trie (supports '.' wildcard)
    def search(self, word: str) -> bool:
        # Start DFS from index 0 and root node
        return self.dfs(word, 0, self.root)


    # ---------------- DFS HELPER ----------------
    # index = current position in word
    # curr = current TrieNode
    def dfs(self, word, index, curr):
        
        # Traverse characters from current index
        for i in range(index, len(word)):
            ch = word[i]

            # Case 1: Wildcard '.'
            # It can match ANY character
            if ch == ".":
                # Try all possible children
                for child in curr.children.values():
                    # Recursively check remaining string
                    if self.dfs(word, i + 1, child):
                        return True
                
                # If none of the paths worked → fail
                return False

            # Case 2: Normal character
            else:
                # If character path doesn't exist → fail
                if ch not in curr.children:
                    return False
                
                # Move to next node in Trie
                curr = curr.children[ch]

        # After processing all characters:
        # Return True ONLY if we are at end of a valid word
        return curr.endOfWord