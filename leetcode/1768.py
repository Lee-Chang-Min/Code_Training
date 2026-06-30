class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        len1, len2 =  len(word1), len(word2)

        min_len = min(len1, len2)

        for i in range(min_len):
            answer.append(word1[i])
            answer.append(word2[i])

        if len1 > min_len:
            for i in range(min_len, len1):
                answer.append(word1[i])
        elif len2 > min_len:
            for i in range(min_len, len2):
                answer.append(word2[i])

        return ''.join(answer)