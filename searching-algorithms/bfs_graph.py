from queue import SimpleQueue


def bfs(graph: dict, initial_vertex: str, search_value: str):
    visited_vertices = []
    bfs_queue = SimpleQueue()
    visited_vertices.append(initial_vertex)
    bfs_queue.put(initial_vertex)

    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        # Check if you found the search value
        if search_value == current_vertex:
            return True

        # Check if the adjacent vertex has been visited
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
                bfs_queue.put(adjacent_vertex)

    return False


if __name__ == "__main__":
    graph = {
        "4": ["6", "7"],
        "6": ["4", "7", "8"],
        "7": ["4", "6", "9"],
        "8": ["6", "9"],
        "9": ["7", "8"],
    }
    print(bfs(graph, "4", "8"))
