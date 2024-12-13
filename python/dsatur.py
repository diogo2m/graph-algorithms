def get_neighbors(v, graph):
    return [w for (w, u) in graph[1] if w == v or u == v]

def get_uncolored(vertices, color):
    return [v for v in vertices if color[v] == 0]

def get_degree(v, graph, color):
    uncolored_neighbors = get_neighbors(v, graph)
    return len([w for w in uncolored_neighbors if color[w] == 0])

def get_saturation(v, color):
    count = 0
    for w in get_neighbors(v, G):
        if color[w] != -1:
            count += 1
    return count

def get_degree_saturation(v, graph, color):
    degree = get_degree(v, graph, color)
    saturation = get_saturation(v, color)
    return (degree, saturation)

def get_vertex_with_highest_degree_saturation(uncolored_vertices):
    max_dsatur = (-1, -1)
    selected_vertex = None

    for v in uncolored_vertices:
        dsatur = get_degree_saturation(v, G, color)
        if dsatur > max_dsatur:
            max_dsatur = dsatur
            selected_vertex = v

    return selected_vertex

def get_lowest_available_color(v, available_colors, color):
    for w in get_neighbors(v, G):
        if color[w] in available_colors:
            available_colors.remove(color[w])
    
    if not available_colors:
        print("There are no sufficient colors.")
        return -1
    
    return min(available_colors)

# Example using complete k-5 graph
V = [v for v in range(5)]
E = [(e, f) for e in V for f in V if e < f]
G = (V, E)

print("Graph: ", G)

color = [-1] * len(V)
available_colors = [c for c in range(5)]
uncolored_vertices = set(G[0])

while uncolored_vertices:
    v = get_vertex_with_highest_degree_saturation(uncolored_vertices)
    color[v] = get_lowest_available_color(v, available_colors, color)
    uncolored_vertices.remove(v)

print("Coloring: ", color)
