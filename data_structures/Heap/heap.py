class Heap:
    def __init__(self) -> None:
        self.data = []
        self.count = 0
    
    def root_node(self):
        return self.data[0]
    
    def last_node(self):
        return self.data[-1]
    def left_child(self, index):
        return (index * 2) + 1
    
    def right_child(self, index):
        return (index * 2) + 2
    
    def parent_index(self, index):
        return (index - 1) // 2
    
    def insert(self, value):
        self.data.append(value)
        self.count += 1
        new_node_index = len(self.data) - 1 
        
        # The following loop executes the "trickle up" algorithms.
        while (new_node_index > 0) and (self.data[new_node_index] > 
                                        self.data[self.parent_index(new_node_index)]):
            
            temp = self.data[self.parent_index(new_node_index)]
            self.data[self.parent_index(new_node_index)] = self.data[new_node_index]
            self.data[new_node_index] = temp
            
            new_node_index = self.parent_index(new_node_index)
    
    def delete(self):
        self.data[0] = self.data.pop()
        self.count -= 1
        trickle_node_index = 0
        
        self.trickle_down(trickle_node_index)
    
    def trickle_down(self, index):
        largest = index
        if self.left_child(index) < self.count and (
            self.data[self.left_child(index)] >= self.data[index]):
            largest = self.left_child(index)
            
        elif self.right_child(index) < self.count and (
            self.data[self.right_child(index)] >= self.data[index]):
            largest = self.right_child(index)
        
        if largest != index:
            temp = self.data[index]
            self.data[index] = self.data[largest]
            self.data[largest] = temp
            self.trickle_down(largest)

hp = Heap()
hp.insert(20)
hp.insert(80)
hp.insert(100)

print(hp.root_node())
print('hello')