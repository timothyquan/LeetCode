class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortdict = sorted(enumerate(nums),key= lambda i: i[1])
        f, l = 0, len(nums) - 1
        while f < l:
            twosum = sortdict[f][1] + sortdict[l][1]
            if twosum == target:
                return sortdict[f][0], sortdict[l][0]
            elif twosum > target:
                l -= 1
            elif twosum < target:
                f += 1
                
            