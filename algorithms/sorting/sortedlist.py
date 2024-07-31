class SortedList:
    def __init__(self, array, target) -> None:
        self.array = array
        self.target = target
    
    def find_sorted_position(self):
        low = 0
        high = len(self.array) - 1
        
        while low <= high:
            midpoint = (low + high) // 2
            mid_value = self.array[midpoint]
            
            if mid_value == self.target:
                return midpoint
            if mid_value < self.target:
                low = midpoint + 1
            if mid_value > self.target:
                high = midpoint - 1
        return low
    
    def sortedArray(self):
        index = self.find_sorted_position()
        self.array.insert(index, self.target)

array = [10, 15, 35, 43, 45, 73, 85, 100]
sortedlist = SortedList(array, 9)
sortedlist.sortedArray()

print(sortedlist.array)