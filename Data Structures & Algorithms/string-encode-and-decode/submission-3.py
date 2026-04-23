class Solution:

    def encode(self, strs: List[str]) -> str:
        # For each word, store it as: <length>#<word>
        # The length helps us know exactly how many characters to read during decoding
        res = []
        for word in strs:
            # res.append(str(len(word)))
            # res.append("#")
            # res.append(word)
            res.append(f"{len(word)}#{word}")

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0

        # Traverse the encoded string and extract each word
        while i < len(s):
            j = i

            # Find the position of '#' which separates length and word
            while s[j] != "#":
                j += 1

            # Extract the length of the word
            length = int(s[i:j])

            # Extract the word using the known length
            # Word starts right after '#' and spans 'length' characters
            word = s[j + 1 : j + 1 + length]
            decode_list.append(word)

            # Move pointer to the start of the next encoded word
            i = j + 1 + length

        return decode_list