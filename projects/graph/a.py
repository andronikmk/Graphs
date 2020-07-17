visited[player.current_room.id] = player.current_room.get_exits()

while len(visited) < len(room_graph):
    if player.current_room.id not in visited:
        visited[player.current_room.id] = player.current_room.get_exits()
        prev = reverse_path[-1]
        visited[player.current_room.id].remove(prev)
    if len(visited[player.current_room.id]) == 0:
        prev = reverse_path[-1]
        reverse_path.pop()
        traversal_path.append(prev)
        player.travel(prev)
    else:
        d = visited[player.current_room.id][-1]
        visited[player.current_room.id].pop()
        traversal_path.append(d)
        reverse_path.append(o[d])
        player.travel(d)