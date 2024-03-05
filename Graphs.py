# Графы. Немного теории.
# Здесь нужно уделить внимание данной структуре, так как
# много алгоритмов работает с этой структорой. Так что такое граф?
# Для меня эта структура, которая отображает данные в виде 
# вершин (узлов - чаще я использую это обозначение) и ребер (связей).
# Другими словами граф - это набор вершин и ребер. Как правило, вершина - 
# это что-либо близкое к реальному миру, а ребра - отображения взаимосвязи 
# между ними. Про что я? Например, вершинами могут быть представлены люди,
# а ребрами между ними (друзья ли они, или иеархия и тому подобное).
# 
# Как говорится, глибина определения рвскрывается в классификации (так
# говорил мой преподователь по патофизиологической анатомии). Поэтому
# немного классификации. 
# 
# Графы могут быть:
#   |-> неоринтированными
#   |-> оринтированными
#   |-> неориентированные мультиграфы
#   |-> ориентированные мультиграфы
# 
# Так же можно выделить особые типы ребер:
#   |-> петля
#   |-> гиперребро
# 
# Интересно, что граф имеющий одно или несколько гиперребер,
# называется гиперграфом.
# 
# Создам неориентированный граф.
#
# 
# 
# 
# 
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


    def __repr__(self) -> str:
        return self.name_node


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
        self.graph[node_from.index_node][node_to.index_node] = route_length
        self.graph[node_to.index_node][node_from.index_node] = route_length
        
        return self.graph


    def disconnect(self, node_from: Node, node_to: Node) -> List[List[int]]:
        pass


    def show_graf(self):
        for i in self.graph:
            print(i)


if __name__ == '__main__':
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")

    graph = Graph.create_from_nodes([a,b,c,d])

    # graph.connect(a, e, 9)

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
    