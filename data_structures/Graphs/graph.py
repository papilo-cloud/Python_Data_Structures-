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