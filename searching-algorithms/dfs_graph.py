def dfs(visited_vertices: set, graph: dict, current_vertex: str):
    # Check if current vertex hasn't been visited yet
    if current_vertex not in visited_vertices:
        print(current_vertex)
        # Add current_vertex to visited_vertices
        visited_vertices.add(current_vertex)
        # Call dfs recursively with the appropriate values
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)


if __name__ == "__main__":
    graph = {
        "0": ["1", "2"],
        "1": ["0", "2", "3"],
        "2": ["0", "1", "4"],
        "3": ["1", "4"],
        "4": ["2", "3"],
    }
    dfs(set(), graph, "0")
