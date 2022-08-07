class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplets_count = 0
        for num in nums:
            seek = num + diff
            if seek in nums:
                j = nums.index(num + diff)
                seek += diff
                if  seek in nums:
                    triplets_count += 1
        return triplets_count             
                    

                    
                    
        