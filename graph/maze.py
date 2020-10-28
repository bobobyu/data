maze_map: list = [[1, 1, 1, 1, 1, 1],
                  [1, 0, 0, 0, 1, 1],
                  [1, 0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 1, 1],
                  [1, 1, 0, 0, 0, 1],
                  [1, 1, 1, 1, 1, 1]]

start_point: list = [1, 1]
end_point: list = [4, 4]
result: list = []

def find_path(current_position:list,each_result:list):
    global maze_map
    if current_position == end_point: #找到终点
        each_result.append(current_position)
        result.append(each_result)
    else:
        if not maze_map[current_position[0]-1][current_position[1]] and current_position not in each_result:    # 向上走
            find_path([current_position[0]-1, current_position[1]], each_result + [current_position])

        if not maze_map[current_position[0]+1][current_position[1]] and current_position not in each_result:    # 向下走
            find_path([current_position[0]+1, current_position[1]], each_result + [current_position])

        if not maze_map[current_position[0]][current_position[1]+1] and current_position not in each_result:    # 向右走
            find_path([current_position[0], current_position[1]+1], each_result + [current_position])

        if not maze_map[current_position[0]][current_position[1]-1] and current_position not in each_result:    # 向左走
            find_path([current_position[0], current_position[1]-1], each_result + [current_position])

find_path(current_position=start_point, each_result=[])
[print(i) for i in result]
