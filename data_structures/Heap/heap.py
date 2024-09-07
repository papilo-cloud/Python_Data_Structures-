class Heap:
    def __init__(self) -> None:
        self.data = []
        self.count = 0
    
    def root_node(self):
        return self.data[0]
    
    def last_node(self):
        return self.data[-1]
    
    def left_child_index(self, index):
        return (index * 2) + 1
    
    def right_child_index(self, index):
        return (index * 2) + 2
    
    def parent_index(self, index):
        return (index - 1) // 2
    
    def insert(self, value):
        self.count += 1
        self.data.append(value)
        new_node_index = len(self.data) - 1
        self.trickle_up(new_node_index)
    
    def delete(self):
        self.data[0] = self.data.pop()
        self.count -= 1
        self.trickle_down(0)
        
    
    def trickle_up(self, index):
        if index > 0 and (
            self.data[index] > self.data[self.parent_index(index)]):
            temp = self.data[index]
            self.data[index] = self.data[self.parent_index(index)]
            self.data[self.parent_index(index)] = temp
            self.trickle_up(self.parent_index(index))
    
    def trickle_down(self, index):
        max_index = index
        if self.left_child_index(index) < self.count and (
            self.data[self.left_child_index(index)] >= max_index):
            max_index = self.left_child_index(index)
        elif self.right_child_index(index) < self.count and (
            self.data[self.right_child_index(index)] >= max_index):
            max_index = self.right_child_index(index)
        
        if max_index != index:
            temp = self.data[index]
            self.data[index] = self.data[max_index]
            self.data[max_index] = temp
            self.trickle_down(max_index)

hp = Heap()
hp.insert(20)
hp.insert(80)
hp.insert(100)

print(hp.root_node())
print('hello')