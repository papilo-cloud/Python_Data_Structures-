class Heap:
    def __init__(self) -> None:
        self.data = []
        self.count = 0
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def root_node(self):
        return self.data[0]
    
    def last_child(self):
        return self.data[-1]
    
    def parent_index(self, index):
        return (index - 1) // 2
    
    def insert(self, value):
        self.data.append(value)
        self.count += 1
        new_node_index = len(self.data) - 1
        self.trickle_up(new_node_index)

    def delete(self):
        value = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.count -= 1
        trickle_index = 0
        
        while self.has_greater_child(trickle_index):
            larger_index = self.calculate_greater_child_index(trickle_index)
            
            temp = self.data[trickle_index]
            self.data[trickle_index] = self.data[larger_index]
            self.data[larger_index] = temp
            
            trickle_index = larger_index
        return value
    
    def has_greater_child(self, index):
        
            return ((self.left_child_index(index) < self.count and (
                self.data[self.left_child_index(index)] > self.data[index])) or (
                    self.right_child_index(index) < self.count and (
                        self.data[self.right_child_index(index)] > self.data[index]
                    )
                ))
                
    def calculate_greater_child_index(self, index):
        if self.right_child_index(index) >= self.count:
            return self.left_child_index(index)
        if self.data[self.right_child_index(index)] > self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        else:
            return self.left_child_index(index)
                
            
    def trickle_up(self, index):
        if index > 0 and (
            self.data[index] > self.data[self.parent_index(index)]):
            temp = self.data[index]
            self.data[index] = self.data[self.parent_index(index)]
            self.data[self.parent_index(index)] = temp
            self.trickle_up(self.parent_index(index))

hp = Heap()

hp.insert(100)
hp.insert(80)
hp.insert(20)
hp.insert(101)
hp.insert(10)
hp.insert(9)
hp.insert(119)
hp.insert(90)
print(hp.data)
print(hp.delete())
print(hp.delete())
print(hp.delete())
print(hp.delete())
print(hp.delete())
print(hp.delete())

print(hp.data)