from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


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

#################################################################################################

# visited rooms
rooms = {}

reverse_path = []

# opposite direction
reverse_dir = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Add room zero to rooms
rooms[0] = player.current_room.get_exits()

# While the number of rooms that you have visisted is less than the total amount of room
    # and if player hasn't visisted the room
        # get the exits
while len(rooms) < len(room_graph)-1:
    if player.current_room.id not in rooms:
        # Add exits for current room to rooms
        rooms[player.current_room.id] = player.current_room.get_exits()
        print("These are the exits: ", player.current_room.get_exits_string())
        # similar to prev in other assignment. getting last direction traveled
        last_dir = reverse_path[-1]
        print("Last direction traveld: ", last_dir)
        rooms[player.current_room.id].remove(last_dir)

    # when there are no more rooms left to traverse do
    while len(rooms[player.current_room.id]) < 1:
        r = reverse_path.pop()
        print("Pop last dir in reverse path:", r)
        # travel down the opposite path now
        # after you add it to the traversal path
        traversal_path.append(r)
        player.travel(r)

    exit_dir = rooms[player.current_room.id].pop(0)
    print("First exit direction in room: ",exit_dir)
    # append to traversal path
    traversal_path.append(exit_dir)
    # add reverse direction
    reverse_path.append(reverse_dir[exit_dir])
    player.travel(exit_dir)

##################################################################################################

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