class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        group_count = 0
        while any(grades):
            if len(grades) <= group_count:
                return group_count
            group_count += 1
            grades = grades[group_count:]
        return group_count
            
            
            
           