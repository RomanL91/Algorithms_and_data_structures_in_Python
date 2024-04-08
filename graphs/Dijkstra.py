# Реализация алгоритма Дейкстры в завещанном неориентированном графе.

class Node:
    def __init__(self, name_node: str, index_node=None) -> None:
        self.name_node = name_node
        self.index_node = index_node

    def __repr__(self) -> str:
        return self.name_node


class Graph:
    def __init__(self, row, col, nodes=None) -> None:
        self.graph = [[0] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index_node = i


    @classmethod
    def create_from_nodes(cls, nodes):
        return cls(len(nodes), len(nodes), nodes)


    def connect(self, node_from: Node, node_to: Node, route_length: int) -> None:
        self.graph[node_from.index_node][node_to.index_node] = route_length
        self.graph[node_to.index_node][node_from.index_node] = route_length


    def show_graph(self) -> None:
        for row in self.graph:
            print(row)


    def dijkstra(self, src: Node) -> None:
        """_summary_

        Args:
            src (Node): Узел - источник от которого
            ведется измерение до других узлов.
        """
        # дистанции до узлов бесконечно большие
        # пока мы их не знаем
        dist = [float('inf')] * len(self.nodes)
        # устанавливаю дистанцию = 0 от узла источника
        dist[src.index_node] = 0
        # список посещенных узлов
        visited = [False] * len(self.nodes)

        for _ in range(len(self.nodes)): # обходим узлы
            analyzed_node = self.min_distance(dist, visited)
            visited[analyzed_node] = True

            for node in range(len(self.nodes)): # перебираем индексы смежных узлов
                # существует ли ребро между analyzed_node и node
                # был ли уже посещен узел
                # можно ли улучшить текущее значение кратчайшего пути до узла
                if self.graph[analyzed_node][node] > 0 \
                        and not visited[node] \
                        and dist[node] > dist[analyzed_node] + self.graph[analyzed_node][node]:
                    # обновляется значение кратчайшего пути до узла, если проверка пройдена
                    dist[node] = dist[analyzed_node] + self.graph[analyzed_node][node]

        self.print_solution(dist)


    def min_distance(self, dist: list, visited: list) -> int:
        """ 
        Вспомогательный метод для нахождения индекса вершины с 
        минимальным расстоянием от источника. 

        Args:
            dist (list): дистации
            visited (list): посещения

        Returns:
            int: индекс вершины с минимальный расстоянием
        """
        min_dist = float('inf')
        min_index = -1

        for v in range(len(self.nodes)):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v

        return min_index


    def print_solution(self, dist):
        print("Узел \t Расстояние от источника")
        for node in self.nodes:
            print(f"{node} \t {dist[node.index_node]}")


if __name__ == '__main__':
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")

    graph = Graph.create_from_nodes([a, b, c, d])

    graph.connect(a, b, 3)
    graph.connect(a, c, 5)
    graph.connect(b, c, 7)
    graph.connect(b, d, 1)
    graph.connect(a, d, 2)
    graph.connect(c, d, 2)

    graph.dijkstra(a)
