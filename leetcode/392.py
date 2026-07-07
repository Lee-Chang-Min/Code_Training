class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_list = list(s)
        t_list = list(t)

        result = []

        s_idx = 0

        if len(s_list) == 0 and len(t_list) == 0:
            return True

        for i in t_list:

            if s and s[s_idx] == i :
                s_idx +=1

            if s_idx == len(s):
                return True

        return False
                