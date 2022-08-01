class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        group_count, grades = 0, len(grades)
        while grades:
            if grades <= group_count:
                return group_count
            group_count += 1
            grades -= group_count
            
        return group_count
            
            
            
           