class Node:
    ''' Node of a linked list in the adjacency list graph.
    '''

    def __init__(self, id, weight=1, next=None):
        ''' (Node, immutable object, num) -> NoneType
        Initializes this Node with id id, weight of the edge, and 
        an optional link to the next node next.
        '''

        self.id = id
        self.weight = weight
        self.next = next

    def __str__(self):
        ''' (Node) -> str
        String representation of this Node
        '''

        return "({0}, {1})".format(self.id, self.weight)


class AdjacencyList:
    ''' Iterator for for the Graph
    '''

    def __init__(self, head):
        ''' (AdjecencyList, Node or NoneType) -> NoneType
        Initializes this iterator with the head of the linked list.
        '''

        self.list = head

    def getNode(self):
        ''' (AdjacencyList) -> Node
        Returns the current node on the head of this AdjacencyList
        '''

        return self.list

    def __iter__(self):
        ''' (AdjacencyList) -> AdjacencyList
        Returns this AdjacencyList itereator.
        '''

        return self

    def __next__(self):
        ''' (AdjacencyList) -> Node
        Returns the next Node for this iterator. Raises StopIteration
        if this is None.
        '''

        if self.list:
            res = self.list
            self.list = self.list.next
            return res
        raise StopIteration

class Graph:
    ''' Adjacency list representation of a graph.
    '''

    def __init__(self):
        ''' Constructor for this Graph.
        '''

        self._graph = {}

    def addEdge(self, fromId, toId, weight, biDir=True):
        ''' (Graph, immutable object, immutable object, num) -> NoneType
        Adds the an edge to this Graph, edge from fromId to toId with
        the weight weight. If biDir is True then an edge from toId to fromId 
        is also created.
        '''

        self._graph[fromId] = Node(toId, weight, self._graph.get(fromId))
        if biDir: self._graph[toId] = Node(fromId, weight, self._graph.get(toId))

    def __getitem__(self, fromId):
        ''' (Graph, immutable object) -> 
        Returns the Adjacency list for the node fromId.
        '''

        return AdjacencyList(self._graph[fromId])

    def removeEdge(self, fromId, toId, biDir=True):
        ''' (Graph, immutable object, immutable object) -> NoneType
        Removes the edge from fromId to toId. If biDir is True then edge from toId
        to fromId is also removed.
        '''

        if self._graph[fromId].id == toId:
            self._graph[fromId] = self._graph[fromId].next

        prev = self._graph[fromId]
        curr = prev.next

        while curr:
            if curr.id == toId:
                prev.next = curr.next
                break
            else:
                prev = prev.next
                curr = curr.next

        if biDir: self.removeEdge(toId, fromId, False)


if __name__ == "__main__":
    gr = Graph()
    gr.addEdge("A", "B", 3)
    gr.addEdge("A", "C", 2)
    gr.addEdge("B", "C", 4)
    gr.addEdge("B", "D", 1)

    print([str(i) for i in gr["B"]])

    gr.removeEdge("B", "A")

    print([str(i) for i in gr["B"]])






	