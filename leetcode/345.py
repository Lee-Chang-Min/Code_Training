class Solution:
    def reverseVowels(self, s: str) -> str:


        set1= set('aeiouAEIOU')

        list1 = list(s)

        s_list = []

        for i in s:
            if i in set1:
                s_list.append(i)

        
        reversed_vowels = s_list[::-1]


        j = 0
        for i in range(len(s)):
            if list1[i] in set1:
                list1[i] = reversed_vowels[j]
                j +=1


        return "".join(list1)
