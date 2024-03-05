# Прошлый пример я делал неориентированный взвешанный граф.
# И представлял его в виде матрицы смежности.
# # [    A  B  C  D
# #    A [0, 3, 5, 2], 
# #    B [3, 0, 7, 1], 
# #    C [5, 7, 0, 2], 
# #    D [2, 1, 2, 0]
# # ]
# Она семмитрична и этим может экономить место,но сейчас о 
# другом. Как будет выглядеть эта матрица для 
# ориентированного графа?
# И да, что такое матрица смежности вообще?
# Нужно как всегда дать определение и классификацию.
# Может есть еще друге варианты матриц? (да =)).
# 
# И так начнем с философии и закрепления ассоциаций.
# Если дорожная сеть - это неориетированный взвешанный граф, где
# собственно дорога это двучстороняя связь между узлами. То иеархия 
# в компании или армии или где-нибудь еще - можно представить как
# ориентированный взвешанный граф, где начальник может отдавать 
# поручения, а вес ребра это некая степень любви/не любви начальника
# к подчинненому или вес ребра будет скоростью исполнения задания
# подчиненным (более удачный пример) и пусть чем меньше вес ребра -
# тем быстрее выполнение задачи.


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
        # и граф стал ориетированым =)
        # self.graph[node_to.index_node][node_from.index_node] = route_length
        
        return self.graph


    def disconnect(self, node_from: Node, node_to: Node) -> List[List[int]]:
        pass


    def show_graf(self):
        for i in self.graph:
            print(i)


if __name__ == '__main__':
    boss = Node("Роман")

    worker_1 = Node("Вадим")
    worker_2 = Node("Кирил")
    worker_3 = Node("Олег")

    graph = Graph.create_from_nodes(
        [
            boss,
            worker_1,
            worker_2,
            worker_3
        ]
    )

    graph.connect(boss, worker_1, 5)
    graph.connect(boss, worker_2, 9)
    graph.connect(boss, worker_3, 13)

    graph.show_graf()

    #            b  w  w  w
    #            o  o  o  o
    #            s  r  r  r
    #            s  k  k  k
    # boss      [0, 5, 9, 13]
    # worker_1  [0, 0, 0, 0]
    # worker_2  [0, 0, 0, 0]
    # worker_3  [0, 0, 0, 0]
# 
# пояснения.
# В такой таблице представлен ориентированный граф.
# Если брать строку boss получим ребра, которые выходят из этой
# вершины boss, а вес ребра будет характеристика как рабочий
# справляется со своей задачей. Если же взять стобец worker_1 - 
# получим ребро, которое входит в вершину worker_1, "силу" этого
# ребра, и можем впоследствии узнать откуда это ребро идет.
# 
# Чтобы добиться такого состояния был взят код и прошлого примера и
# буквально закомметированна 58 строка кода.
# 
# Не плохое определение подстмотренное из сети и поясняющее, что такое 
# матрица смежности.
# Смежность – понятие, используемое только в отношении двух ребер 
# или в отношении двух вершин: два ребра инцидентные одной вершине, называются смежными; 
# две вершины, инцидентные одному ребру, также называются смежными.
