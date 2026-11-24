class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded_str = ""
        for s in strs:
            es = str(len(s)) + "#" + s
            encoded_str += es

        # print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        result = []
        i = 0
        num = ""
        while i < len(s):
            if s[i] != "#":
                num += s[i]
                i += 1
            else:
                word_length = int(num)
                result.append(s[i + 1 : i + 1 + word_length])
                num = ""
                i = i + 1 + word_length

        return result

