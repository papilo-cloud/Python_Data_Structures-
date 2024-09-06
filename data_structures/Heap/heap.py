class Heap:
    def __init__(self) -> None:
        self.data = []
    
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
        new_node_index = len(self.data) - 1 
        
        # The following loop executes the "trickle up" algorithms.