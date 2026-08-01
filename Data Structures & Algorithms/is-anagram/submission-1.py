class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashOne, hashTwo = {}, {}

        for i in range(len(s)) :
            hashOne[s[i]] = 1 + hashOne.get(s[i],0)
            hashTwo[t[i]] = 1 + hashTwo.get(t[i],0)
            #Gets the current character and adds it into the map
            #As it goes through each string, it adds how many of that letter is in the string
            #After, if both strings match it returns True
        return hashOne == hashTwo