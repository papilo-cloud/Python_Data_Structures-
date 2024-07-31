class SortableArray:
    def __init__(self, array) -> None:
        self.array = array
    
    def partition(self, left_pointer, right_pointer):
        pivot_index = left_pointer
        pivot = self.array[left_pointer]
        left_pointer += 1
        
        while left_pointer <= right_pointer:
            while left_pointer < right_pointer and self.array[left_pointer] < pivot:
                left_pointer += 1
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
            if left_pointer >= right_pointer:
                break
            else:
                temp = self.array[left_pointer]
                self.array[left_pointer] = self.array[right_pointer]
                self.array[right_pointer] = temp
                
        tempt = self.array[right_pointer]
        self.array[right_pointer] = self.array[pivot_index]
        self.array[pivot_index] = tempt
        return right_pointer
    
    def quickselect(self, kth_lowest_value, left_index, right_index):
        if right_index - left_index <= 0: 
            return self.array[left_index]
        
        # Partition the array and grab the index of the pivot
        pivot_index = self.partition(left_index, right_index)
        
        # If what we're looking for is to the left of the pivot
        if kth_lowest_value < pivot_index:
            self.quickselect(kth_lowest_value, left_index, pivot_index - 1)
            
        # If what we're looking for is to the left of the pivot
        elif kth_lowest_value > pivot_index:
            self.quickselect(kth_lowest_value, pivot_index + 1, right_index)
            
        else: # If the kth_lowest_value == pivot_index
            return self.array[pivot_index]
array = [100, 5, 20, 10, 60, 30]
sortable_array = SortableArray(array)

print(sortable_array.quickselect(0, 0, len(array) - 1))
print(sortable_array.array)
        