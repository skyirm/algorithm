from queue import Queue


class Vertex:

    def __init__(self, key) -> None:
        self.id = key
        self.connet_to: dict[Vertex, int] = {}

    def add_neighbor(self, neighbor, weight):
        self.connet_to[neighbor] = weight

    def __str__(self) -> str:
        return str(self.id) + ' connect_to: '+str([x.id for x in self.connet_to])

    def get_connections(self):
        return self.connet_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connet_to[neighbor]


class Vertex_Extend(Vertex):

    def __init__(self, key) -> None:
        super().__init__(key)
        self.distance = 0
        self.color = 'White'
        self.predecessor: Vertex_Extend | None = None


class Graph:

    def __init__(self) -> None:
        self.vert_list: dict[str, Vertex] = {}
        self.vert_nums = 0

    def add_vertex(self, key):
        self.vert_nums += 1
        new_vertex = Vertex_Extend(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        return None

    def __contains__(self, n):
        return n in self.vert_list

    def add_edge(self, from_v, to_v, cost=0):
        if not from_v in self.vert_list:
            self.add_vertex(from_v)
        if not to_v in self.vert_list:
            self.add_vertex(to_v)
        self.vert_list[from_v].add_neighbor(self.vert_list[to_v], cost)

    def get_vertexs(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


def build_graph(word_file: str) -> Graph:
    d: dict[str, list] = {}
    g = Graph()
    with open(word_file, 'r') as wfile:
        for line in wfile:
            word = line[:-1]
            for i in range(len(word)):
                bucket = word[:i]+'_'+word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    for bucket in d.keys():
        for word_1 in d[bucket]:
            for word_2 in d[bucket]:
                if word_1 != word_2:
                    g.add_edge(word_1, word_2)
    return g


def bfs(g, start: Vertex_Extend):
    start.distance = 0
    start.predecessor = None
    vert_queue: Queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current_vert: Vertex_Extend = vert_queue.dequeue()
        for nbr in current_vert.get_connections():
            if nbr.color == "White":
                nbr.color = 'Grey'
                nbr.distance = current_vert.distance+1
                nbr.predecessor = current_vert
                vert_queue.enqueue(nbr)
        current_vert.color = 'Black'


if __name__ == "__main__":

    g = Graph()
    for i in range(6):
        g.add_vertex(i)
