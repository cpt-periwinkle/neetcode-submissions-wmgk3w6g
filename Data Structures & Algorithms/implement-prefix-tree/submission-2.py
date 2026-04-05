# A TrieNode represents ONE character in the Trie
class TrieNode:
    def __init__(self):
        # Dictionary mapping character → next TrieNode
        # Example: {'a': node1, 'b': node2}
        self.children = {}
        
        # Marks if a word ends at this node
        # Important because "app" and "apple" share nodes
        self.endOfWord = False


class PrefixTree:

    def __init__(self):
        # Root is an empty node (does NOT store any character)
        self.root = TrieNode()


    # ---------------- INSERT ----------------
    # Goal: Add a word into the Trie
    def insert(self, word: str) -> None:
        curr = self.root  # Start from root
        
        # Traverse each character in the word
        for ch in word:
            # If path doesn't exist, create a new node
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            # Move to the next node
            curr = curr.children[ch]
        
        # After inserting all characters, mark end of word
        curr.endOfWord = True

        # Example:
        # Insert "cat"
        # root → c → a → t (endOfWord = True)


    # ---------------- SEARCH ----------------
    # Goal: Check if EXACT word exists in Trie
    def search(self, word: str) -> bool:
        curr = self.root
        
        # Traverse each character
        for ch in word:
            # If path breaks → word not present
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]
        
        # Only return True if it's a COMPLETE word
        # (not just a prefix)
        return curr.endOfWord

        # Example:
        # If "apple" inserted:
        # search("app") → False (unless explicitly inserted)
        # search("apple") → True


    # ---------------- STARTS WITH ----------------
    # Goal: Check if any word starts with given prefix
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        # Traverse prefix characters
        for ch in prefix:
            # If path breaks → no word has this prefix
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]
        
        # If we successfully traverse prefix → valid prefix
        return True

        # Example:
        # If "apple" inserted:
        # startsWith("app") → True
        # startsWith("apl") → False