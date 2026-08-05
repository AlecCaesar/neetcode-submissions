class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # mapping charCount to list of Anagrams

        for s in strs:  #For every string in the array "strs"
            count = [0] * 26 # 26 0's. one for each letter (a-z)

            for c in s: # go through every single character in each string
                count[ord(c) - ord('a')] += 1 # current ascii value - ascii value of a. Maps the value and adds the amount of that char
            res.setdefault(tuple(count),[]).append(s) #append - add that element into the tuple
        return list(res.values())