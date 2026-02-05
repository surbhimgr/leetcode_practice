''' Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]] '''


from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)  # dictionary with list as default value
        for s in strs:
            key = tuple(sorted(s))  # use tuple as hashable key
            dic[key].append(s)
        return list(dic.values())
