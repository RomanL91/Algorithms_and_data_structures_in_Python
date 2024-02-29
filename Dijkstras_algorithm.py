# Графы. Теория
# Деревья расширяют область применения связанных списков, позволяя иметь более одного дочернего узла. 
# При помощи графов можно расширить область применения и ослабить строгую «родительскую» связь в деревьях. 
# Узлы графа не имеют явной иерархии. 
# Каждый узел может быть соединен с любым другим узлом.
# Как правило, графы представлены в виде матриц смежности. 
# (как правило данные матрицы симметричны).
# Пример графа из 4 отдельных узлов никак не связанных между собой.
# В примере каждая строка и столбец представляют собой узел, а пересечение
# строки и столбца - в данной реализации условно длина маршрута между узлами.
# (в примере ниже, они пока никак не связаны и стоят обособленно).
# В данном разборе будем использовать списки, однако, стоит помнить о NumPy
# и его преводсходством над обычными списками (типизация, векторизованные операции и др.).
# [
    # [0, 0, 0, 0], 
    # [0, 0, 0, 0], 
    # [0, 0, 0, 0], 
    # [0, 0, 0, 0]
# ]

from typing import List


class Node:
    def __init__(self, name_node: str, index_node = None) -> None:
        self.name_node = name_node
        self.index_node = index_node


class Graph:
    def __init__(self, row, col, nodes = None) -> None:
        self.graph = [[0] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index_node = i


    @classmethod
    def create_from_nodes(self, nodes: List[Node]):
        return Graph(len(nodes), len(nodes), nodes)


    def connect(self, node_from: Node, node_to: Node, route_length: int) -> List[List[int]]:
        """
        Обновляем self.graph для соединения узлов.
        """
        self.graph[node_from.index_node][node_to.index_node] = route_length
        self.graph[node_to.index_node][node_from.index_node] = route_length
        return self.graph


    def disconnect(self, node_from: Node, node_to: Node) -> List[List[int]]:
        """
        Обновляем self.graph для разъединения узлов.
        """
        self.graph[node_from.index_node][node_to.index_node] = 0
        self.graph[node_to.index_node][node_from.index_node] = 0
        return self.graph
    

    def search_route(self, node_start: Node) -> List[List[int]]:
        print('----------------------')
        # [     A  B  C  D
        #    A [0, 3, 5, 2], 
        #    B [3, 0, 7, 1], 
        #    C [5, 7, 0, 2], 
        #    D [2, 1, 2, 0]
        # ]
        index_start_node = node_start.index_node

        dist = [float("inf")] * len(self.nodes)
        dist[index_start_node] = 0

        viewed_node = {index_start_node}

        for ind_nodes, noda in enumerate(self.nodes):
            print(ind_nodes, noda.name_node, ' -- узел и его связные --->>')
            link_this_noda = [self.graph[ind_nodes].index(i) for i in self.graph[ind_nodes] if i != 0]
            print(f'show_link  {link_this_noda}')
            for links_node in link_this_noda:
                if dist[links_node] > self.graph[links_node][ind_nodes]:
                    print(dist[links_node], self.graph[links_node][ind_nodes])
                    # w = self.graph[links_node][ind_nodes] + 
                    

        print(dist)



    def show_graf(self):
        for i in self.graph:
            print(i)


if __name__ == '__main__':
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    graph = Graph.create_from_nodes([a,b,c,d,e])

    graph.connect(a, e, 9)

    # # соединяем условно узел "А" с узлами "B" и "C".
    # # длина маршрута от "А" до "В" = 3
    # # длина маршрута от "А" до "С" = 5
    graph.connect(a, b, 3)
    graph.connect(a, c, 5)
    # # [     A  B  C  D
    # #   A  [0, 3, 5, 0], 
    # #   B  [3, 0, 0, 0], 
    # #   C  [5, 0, 0, 0], 
    # #   D  [0, 0, 0, 0]
    # # ]

    # # соединяем условно узел "B" с узлом "C" длиной маршрута = 7. 
    graph.connect(b, c, 7)
    # # [     A  B  C  D
    # #    A [0, 3, 5, 0], 
    # #    B [3, 0, 7, 0], 
    # #    C [5, 7, 0, 0], 
    # #    D [0, 0, 0, 0]
    # # ]

    # # соединяем условно узел "B" с узлом "D" длиной маршрута = 1. 
    graph.connect(b, d, 1)
    # # [     A  B  C  D
    # #    A [0, 3, 5, 0], 
    # #    B [3, 0, 7, 1], 
    # #    C [5, 7, 0, 0], 
    # #    D [0, 1, 0, 0]
    # # ]

    # # соединяем условно узел "A" с узлом "D" длиной маршрута = 2. 
    graph.connect(a, d, 2)
    # # [     A  B  C  D
    # #    A [0, 3, 5, 2], 
    # #    B [3, 0, 7, 1], 
    # #    C [5, 7, 0, 0], 
    # #    D [2, 1, 0, 0]
    # # ]

    # # соединяем условно узел "C" с узлом "D" длиной маршрута = 2. 
    graph.connect(c, d, 2)
    #  # [    A  B  C  D
    # #    A [0, 3, 5, 2], 
    # #    B [3, 0, 7, 1], 
    # #    C [5, 7, 0, 2], 
    # #    D [2, 1, 2, 0]
    # # ]

    graph.show_graf()
    graph.search_route(e)