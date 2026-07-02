class Solution:
    def reverseWords(self, s: str) -> str:

        word = []

        word = s.split()

        return " ".join(word[::-1])



        
        