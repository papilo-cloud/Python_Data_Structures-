class QuickSort:
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
    
    
    def quicksort(self, left_index, right_index):
        if left_index >= right_index:
            return
        
        pivot_pos = self.partition(left_index, right_index)
        
        self.quicksort(left_index, pivot_pos - 1)
        self.quicksort(pivot_pos + 1, right_index)


array = [10, 5, 2, 1, 6, 3]
quick_sort = QuickSort(array)
quick_sort.quicksort(0, len(array) - 1)
print(array)