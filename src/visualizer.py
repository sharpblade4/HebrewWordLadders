from typing import Set, Callable, List
import networkx as nx
import matplotlib.pyplot as plt


def visualize(path: List[str], get_neighbours: Callable[[str], Set[str]]) -> None:
    graph = nx.Graph()
    for node in path:
        graph.add_node(node[::-1])
        neighbours = get_neighbours(node)
        graph.add_nodes_from([e[::-1] for e in neighbours])
        graph.add_edges_from([[node[::-1], e[::-1]] for e in neighbours])
    nx.draw(graph, with_labels=True, node_color="cyan", node_size=1000)
    plt.show()


def visualize_full(path: List[str], get_neighbours: Callable[[str], Set[str]]) -> None:
    graph = nx.Graph()
    queue = [path[0]]
    next_queue = []
    i = 1
    span = 4
    colors = []
    visited = set()
    while i < span:
        node = queue.pop()
        visited.add(node)
        graph.add_node(node[::-1])
        neighbours = get_neighbours(node)
        graph.add_edges_from([[node[::-1], e[::-1]] for e in neighbours])
        colors.extend([i] * len(neighbours.difference(visited)))
        next_queue.extend(neighbours)
        if len(queue) == 0:
            i += 1
            queue = next_queue
            next_queue = []
    nx.draw(
        graph,
        with_labels=True,
        node_color="none",
        node_size=400,
        font_size=6,
        edge_cmap=plt.cm.Wistia_r,
        edge_color=colors[: len(graph.edges)],
        alpha=0.6,
    )
    plt.show()
