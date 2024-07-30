class QuickSort:
    def __init__(self, array) -> None:
        self.array = array
        
    def partition(self, left_pointer, right_pointer):
        pivot_index = right_pointer
        pivot = self.array[right_pointer]
        right_pointer -= 1
        
        while left_pointer <= right_pointer:
            while self.array[left_pointer] < pivot:
                left_pointer += 1
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
            if left_pointer >= right_pointer:
                break 
            else:
                temp = self.array[left_pointer]
                self.array[left_pointer] = self.array[right_pointer]
                self.array[right_pointer] = temp
                
        tempt = self.array[left_pointer]
        self.array[left_pointer] = self.array[pivot_index]
        self.array[pivot_index] = tempt
        
        return left_pointer
    
    def quick_sort(self, left_index, right_index):
        if left_index >= right_index:
            return
        
        # Partition the range of elements and grab the index of the pivot:
        pivot_index = self.partition(left_index, right_index)

        # Recursively call this quicksort method on whatever is to the 
        # left of the pivot:
        self.quick_sort(left_index, pivot_index - 1 )

        # Recursively call this quicksort method on whatever is to the 
        # right of the pivot:
        self.quick_sort(pivot_index + 1, right_index)

array = [0, 5, 2, 1, 6, 3] #[10, 23, 51, 18, 4, 31, 5, 13]
quicksort = QuickSort(array)
quicksort.quick_sort(0, len(array) - 1)
print(quicksort.array)