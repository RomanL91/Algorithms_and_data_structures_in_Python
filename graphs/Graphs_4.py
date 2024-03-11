# Продолжу изучение графов.
# Разобрался на данный момент просто в структурном понимании
# графов, покопался в классификации: взвешанные или нет, ориентированные
# или нет, мультиграф.
# В чем еще предстоит немного разобраться, так это в 
# понимании таблиц смежности, идентичности.
# Разобраться в понимаиии ребер графа, и это немного затрону сегодня.
# А конкретно, вершина может быть связна и сама с собой, образуя
# петлю - я пока не думал и не придумал примера, где это было бы полезно,
# но наверное такие ситуации есть.
# А еще меня заинтересовало понятие гипер-ребра!
# И как я писал уже в Graphs_1: граф имеющий хоть одно гиперребро - 
# ГИПЕРГРАФ!
# 
# Возьму код из Graphs_1 и на его основе будем делать ГИПЕР-граф.
# 
# Попробую пойти путем представления гипер-ребра отдельным объектом.
# Создам класс Hyperedge, без понятия чем его инициализировать - pass.
# А затем, по моей задумке это гипер-ребро будем "присваивать" графу,
# получая гипер-граф.
# Но что делать, если у нас есть граф уже со связями между узлами.
# Что если это гиперребро "наслаивается" на уже имеющиюся связь...
# Думаю стоит принять решение, что если добавляю гиперребро в имеющийся граф
# со своими связями, то ничего перезатирать не буду, а добавлять метку,
# что у этой вершины есть еще связь по гиперребру.
# Виду этого поднимаются вопросы о изначальной архитектуре и представления
# графа не просто матрицей, где на пересечении строки и колонки будет
# хранится значение связи узлов, а теперь на пересечении будет хранится
# список связей.
# Вот пример такой матрицы, где вершина А соединена с вершиной В силой = 1.
#                       [[0], [1], [0], [0]]
#                       [[1], [0], [0], [0]]
#                       [[0], [0], [0], [0]]
#                       [[0], [0], [0], [0]]
# 
# А при соединении вершин гипер-ребром буду добавлять в список еще значении.
# Посмотрим, что получу.
# 
# 
# 
from typing import List


class Node:
    def __init__(self, name_node: str, index_node = None) -> None:
        self.name_node = name_node
        self.index_node = index_node


    def __repr__(self) -> str:
        return self.name_node
    

class Hyperedge:
    def __init__(self, name_hyperedge: str, 
                 nodes: List[Node], route_length: int) -> None:
        self.name_hyperedge = name_hyperedge
        self.nodes = nodes
        self.route_length = route_length

    
    def __repr__(self) -> str:
        return f'{self.name_hyperedge} ({self.route_length})'


    def nodes_hyperedge_communication(self):
        return self.nodes


class Graph:
    def __init__(self, row, col, nodes = None) -> None:
        self.graph = [[[0]] * col for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index_node = i


    @classmethod
    def create_from_nodes(self, nodes: List[Node]):
        return Graph(len(nodes), len(nodes), nodes)


    def connect(self, node_from: Node, node_to: Node, 
                route_length: int) -> List[List[List[int]]]:
        self.graph[node_from.index_node][node_to.index_node] = [route_length]
        self.graph[node_to.index_node][node_from.index_node] = [route_length]
        
        return self.graph
    
    
    def create_link_hyperedge(self, node: Node, 
                              hyperedge: Hyperedge) -> List[List[List[int]]]:
        list_for_links = hyperedge.nodes_hyperedge_communication()
        indexs = [el.index_node for el in list_for_links]

        for i in indexs:
            row = self.graph[i]
            row[node.index_node] = [*row[node.index_node], hyperedge]
            self.graph[node.index_node][i] = [*self.graph[node.index_node][i], hyperedge]

        while indexs:
            el, *other_el = indexs
            for i in other_el:
                self.graph[el][i] = [*self.graph[el][i], hyperedge]
                self.graph[i][el] = [*self.graph[i][el], hyperedge]
            indexs.remove(el)

        return self.graph


    def show_graf(self):
        for i in self.graph:
            print(i)


if __name__ == '__main__':
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")

    # создаем граф из узлов
    graph = Graph.create_from_nodes([a,b,c,d])

    # соединяю узлы (a, b) силой 1
    graph.connect(a, b, 1)

    # а это уже моя реализация
    # создание будущего гиперребра
    # пока что это просто экземпляр, куда переданы 2 вершины (можно больше),
    # задано имя и сила связи.
    hyper = Hyperedge('hyper', [c, d], 4) 

    # тут задумка такая:
    # обраюсь к графу и говорю ему создать гиперребро 
    # от вершины А
    graph.create_link_hyperedge(a, hyper)

    graph.show_graf()


# Вот так будет представлен данный гиперграф
#  
# [        [0],           [1],    [0, hyper (4)],   [0, hyper (4)]   ]
# [        [1],           [0],          [0],              [0]        ]
# [   [0, hyper (4)],     [0],          [0],        [0, hyper (4)]   ]
# [   [0, hyper (4)],     [0],    [0, hyper (4)],         [0]        ]
