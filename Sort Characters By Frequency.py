
'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        s1=sorted(s,key=lambda x:(-dic[x],x))
        return "".join(s1)
