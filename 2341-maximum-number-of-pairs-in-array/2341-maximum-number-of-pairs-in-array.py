class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nmap = {}
        answer = [0]
        for n in nums:
            nmap.setdefault(n, 0)
            nmap[n] += 1
        for n in nmap:
            answer[0] += nmap[n]//2
            
        answer.append(len([k for k,v in nmap.items() if v%2>0]))
        return answer
         