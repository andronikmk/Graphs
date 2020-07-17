"""
Simple graph implementation
"""
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from utils import Stack, Queue  # These may come in handy

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

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        # push on your starting node
        s.push([starting_vertex])
        # make a set to track if it was visited
        visited = set()
        # while stack not empty
        while s.size() > 0:
            # pop off what is on top.
            current_node = s.pop()
            # if we have no visited the vertex before
            if current_node not in visited:
                # run function/print
                # print(current_node)
                # mark as visited
                # visited.add(current_node)
                # get its neighbors
                # neighbors = self.get_neighbors(current_node)
                # for each of the neighbors

                self.vertices[room.id] = {}
                for neighbor in room.get_exits():
                    self.vertices[room.id][room.get_room_in_direction(possible_direction).id]= neighbor
                
                visited.add(room)
                exits = room.get_exits()
                while len(exits) > 0:
                    # select first neighbors on list
                    direct = exits[0]
                    # beej: create neighbor object
                    path = list(current_node)
                    # add possibles directions to move
                    path.append(room.get_room_in_direction(direct))
                    # add to stack
                    s.push(path)
                    # remove to contine
                    exits.remove(direct)
        return self.vertices

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
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
                neighbors = self.vertices[current_node].keys()
                # for each neibor
                for neighbor in neighbors:
                    path = list(current_node)
                    # add to queue
                    path.append(neighbor)
                    q.enqueue(path)