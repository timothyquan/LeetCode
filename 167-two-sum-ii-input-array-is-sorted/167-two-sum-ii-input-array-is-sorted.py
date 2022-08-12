class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while True:
            cur = numbers[left] + numbers[right]
            if cur == target:
                return [left+1, right+1]
            
            if cur > target:
                right -= 1
                
            elif cur < target:
                left += 1
            