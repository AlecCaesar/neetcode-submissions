class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash = set()    #set up a hash set

        for num in nums:    #for every number in the array
            if num in hash: #if theres a number in the set that matches the number thats being iterated, return true
                return True
            hash.add(num)   # adds number in hash if there is no number matching
        return False        # False if there is no duplicates / outside for loop