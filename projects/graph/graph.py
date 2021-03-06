"""
Simpe graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:


    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        #pass  # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #pass  # TODO
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make a set to track if we've been here before
        visited = set()
        # while our queue isn't empty
        while q.size() > 0:
        ## dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
        ## if we haven't visited this node yet,
            if current_node not in visited:
                print(current_node)
        ### mark as visited
                visited.add(current_node)
        ### get its neighbors
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors,
                for neighbor in neighbors:
        #### add to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on your starting node
        s.push(starting_vertex)
        # make a set to track if it was visited
        visited = set()
        # while stack not empty
        while s.size() > 0:
            # pop off what is on top.
            current_node = s.pop()
            # if we have no visited the vertex before
            if current_node not in visited:
                # run function/print
                print(current_node)
                # mark as visited
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                for neighbor in neighbors:
                    # if neighbor not in visited:
                        s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # #pass  # TODO
        # # make a stack
        # s = Stack()
        # # push on your starting node
        # s.push(starting_vertex)
        # # make a set to track if it was visited
        # visited = set()
        # # while stack is not empty
        # while s.size() > 0:
        #     current_node = s.pop()
        #     # if we have not visited the vertex before
        #     if current_node not in visited:
        #         # print(current node)
        #         print(current_node)
        #         visited.add(current_node)
        #         # get neighbors
        #         neighbors = self.get_neighbors(current_node)
        #         # for each of the neibors
        #         for neighbor in neighbors:
        #             # if neighbors not in set
        #             if neighbor not in visited:
        #                 # add neibor to stack
        #                 s.push(neighbor)

        # mark this vertex as visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # for each neighbor
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
        ## if it's not visited
            if neighbor not in visited:
        ### recurse on the neighbor
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass
        # # make a queue
        # q = Queue()
        # # enqueue our starting node
        # q.enqueue([starting_vertex])
        # # make a set to track if it was visited
        # visited = set()
        # # while queue is not empty
        # while q.size() > 0:
        #     # dequeue whatever's at the front of our line, this is our current_node
        #     path = q.dequeue()
        #     # get the last vertixe on the path
        #     node = path[-1]
        #     print(node)
        #     # if last vertix not in visited
        #     if node not in visited:
        #         # if node is equal to destination vertix
        #         if node == destination_vertex:
        #             # return path or deque
        #             return path
        #         # mark node as visited
        #         visited.add(node)
        #         # get neighbors
        #         neighbors = self.get_neighbors(node)
        #         # add path to neibords in the back of the queue
        #         for neighbor in neighbors:
        #             # copy the path
        #             new_path = path.copy()
        #             # append neibor to back
        #             new_path.append(neighbor)
        #             q.enqueue(new_path)

        # make a queye
        q = Queue()
        # make a set to track the nodes
        visited = set()
        path = [starting_vertex]
        # enqueue the starting node
        q.enqueue(path)
        # while the queue isn't empty
        while q.size() > 0:
        ## dequee the node at the front of the line
            current_path = q.dequeue()
            current_node = current_path[-1]
        ### if this node is out targte node
            if current_node == destination_vertex:
            #### return it!! return True
                return current_path
        ### if not visted
            if current_node not in visited:
        #### mark as visited
                visited.add(current_node)
        #### get neigghbots
                neighbors = self.get_neighbors(current_node)
                # for each neibor
                for neighbor in neighbors:
                    # add to queue
                    q.enqueue(current_path + [neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # pass  # TODO
        # make a stack
        s = Stack()
        # make a set to track the nodes and set a path
        visited = set()
        path = [starting_vertex]
        # push the starting node
        s.push(path)
        # while stack is not empty
        while s.size() > 0:
            # pop off the current path
            current_path = s.pop()
            # set current node to last node
            current_node = current_path[-1]
            # if the node is not our targte node
            if current_node == destination_vertex:
                # return current_path
                return current_path
            # if current node has not been visisted
            if current_node not in visited:
                # mark it as visisted
                visited.add(current_node)
                # get the neighbor
                neighbors = self.get_neighbors(current_node)
                # for each neighbor
                for neighbor in neighbors:
                # add to the stack (push)
                    s.push(current_path + [neighbor])

    def dfs_recursive(self, vertex, destination_vertex, path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        ## mark our node as visited
        visited.add(vertex)

        ## check if it's our target node, if so return
        if vertex == destination_vertex:
            return path

        if len(path) == 0:
            path.append(vertex)
        
        ## iterate over neighbors
        neighbors = self.get_neighbors(vertex)
        ### check if visited
        for neighbor in neighbors:
            if neighbor not in visited: 
        #### if not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor], visited)
        ##### if this recursion returns a path,
                if result is not None:
            ###### return from here
                    return result


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
