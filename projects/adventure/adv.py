from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# my imports
from adv_graph import Graph
from utils import Stack, Queue

# Load world
world = World()
# Load graph
graph = Graph()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# create a map of the world and get length
rooms_object = graph.dft(player.current_room)
rooms_object_length = len(rooms_object)

# room ids to list
room_lists = [k for k in rooms_object.keys()]

while rooms_object_length > 1:
    # current room position
    current_room = room_lists[0]
    next_room = room_lists[1]
    current_room_n = rooms_object[current_room]
    # if there are neighbors add them to the traversal path
    if next_room in current_room_n.keys():
        # append to traversal path
        traversal_path.append(current_room_n[next_room])
    else:
        # use breadth first search to find shortest path if not neighbors
        s_path = graph.bfs(current_room, next_room)
        s_path_length = len(s_path)
        while s_path_length > 1:
            pass



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")