class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent_vertices = []
        
    def add_adjacent_vertex(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)
    
    def dfs_traverse(self, vertex, visited={}):
        visited[vertex.value] = 1
        print(vertex.value)
        
        for adj_vrtx in vertex.adjacent_vertices:
            if visited.get(adj_vrtx.value):
                continue
            self.dfs_traverse(adj_vrtx, visited)
    
    # Searching for a particular vertex.
    def dfs(self,vertex, search_val, visited={}):
        if vertex.value == search_val:
            return vertex
        
        visited[vertex.value] = 1
        
        for adj_vrtx in vertex.adjacent_vertices:
            if visited.get(adj_vrtx.value):
                continue
            if vertex.value == search_val:
                return vertex
            
            searched_value = self.dfs(adj_vrtx, search_val, visited)
            
            if searched_value:
                return searched_value
        return None