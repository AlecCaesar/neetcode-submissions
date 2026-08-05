class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        #TODO:
        for i in nums:
            count[i] = count.get(i, 0) + 1

        arr = []
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort()  #sorts ascending order

        result = []
        #while the length of the result is less than k most freq.
        while len(result) < k:
            print(arr)
            result.append(arr.pop()[1]) #FIFO / pops element and appends to result
            
        return result



        

