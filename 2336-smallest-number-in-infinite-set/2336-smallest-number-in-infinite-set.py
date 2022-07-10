class SmallestInfiniteSet:

    def __init__(self):
        self.sis = {i for i in range(1,1001)}
        
    def popSmallest(self) -> int:
        val = min(self.sis)
        self.sis.remove(val)
        return val 
        

    def addBack(self, num: int) -> None:
        self.sis.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)