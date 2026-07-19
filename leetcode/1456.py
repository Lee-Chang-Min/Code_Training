class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        set1 = set(['a', 'e', 'i', 'o','u'])
        curr = 0

        list2 = list(s[:k])
        for l in list2:
            if l in set1:
                curr +=1

        
        ans = curr
        for i in range(k,len(s)):
            if s[i] in set1:
                ans+=1
            if s[i-k] in set1:
                ans -=1
            
            curr = max(curr, ans)
            
            if curr == k:
                break

        
        return curr

            
