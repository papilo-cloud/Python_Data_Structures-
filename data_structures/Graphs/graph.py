class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacent_vertices = []
    
    def add_adjacent_vertex_undirected(self, vertex):
        self.adjacent_vertices.append(vertex)
        
    def add_adjacent_vertex_directed(self, vertex):
        if vertex in self.adjacent_vertices:
            return
        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex_directed(self)
    
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
    
    def shortest_path(self, start, stop):
        visited = {}
        previous_table = {}

        visited[start.value] = 1
        q = []
        q.append(start)
        
        while q:
            current = q.pop(0)

            for adjacent in current.adjacent_vertices:
                if not visited.get(adjacent.value):
                    visited[adjacent.value] = 1
                    q.append(adjacent)
                    
                    previous_table[adjacent.value] = current.value
        
        path = []
        current_path = stop.value
        while current_path:
            path.insert(0, current_path)
            current_path = \
                previous_table.get(current_path)
        return path