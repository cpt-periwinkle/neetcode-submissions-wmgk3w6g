class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for word in strs:
            encode_str += str(len(word)) + "#" + word   #length#word would be the encode string
        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1          # Reads until the hash so we get the total length

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]    # j is where hash is, our word starts after it
            decode_list.append(word)
            i = j + 1 + length      # so we can move onto the next word
        return decode_list

