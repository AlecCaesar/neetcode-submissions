class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
       hash = set()

       for num in nums:
            if num in hash:     #If there is a number in the hash set already
                return True
            hash.add(num)           #If there isnt, add that number into the hash set
       return False