class Dijkstar:
    def __init__(self, dis_matrix: list):
        height: int = len(dis_matrix)
        length: int = len(dis_matrix[0])
        all_vertex = [(i, j) for i in range(height) for j in range(length)]
        all_dis: dict = {j: float('inf') for j in all_vertex}
        self.dis_dict: dict = {i: all_dis.copy() for i in all_vertex}
        for row_index, _ in enumerate(dis_matrix):
            for col_index, __ in enumerate(dis_matrix[0]):
                if dis_matrix[row_index][col_index]:
                    self.dis_dict[(row_index, col_index)][(row_index, col_index)] = 0
                    if row_index < height - 1 and dis_matrix[row_index + 1][col_index]:
                        self.dis_dict[(row_index, col_index)][(row_index + 1, col_index)] = 1
                    if row_index > 0 and dis_matrix[row_index - 1][col_index]:
                        self.dis_dict[(row_index, col_index)][(row_index - 1, col_index)] = 1
                    if col_index < length - 1 and dis_matrix[row_index][col_index + 1]:
                        self.dis_dict[(row_index, col_index)][(row_index, col_index + 1)] = 1
                    if col_index > 0 and dis_matrix[row_index][col_index - 1]:
                        self.dis_dict[(row_index, col_index)][(row_index, col_index - 1)] = 1
        self.alternative_vertexes: set = set(all_vertex)

    def search(self, search_pos: tuple) -> dict:
        search_pos: tuple = search_pos
        alternative_vertexes_ = self.alternative_vertexes.copy()
        alternative_vertexes_.discard(search_pos)
        fixed_vertexes: set = {search_pos}
        select_vertex: tuple = ()
        pre_vertex: tuple = ()

        while alternative_vertexes_:
            min_distance: float = float('inf')
            for search_ in fixed_vertexes:
                min_next_vertex = min(alternative_vertexes_, key=lambda x: self.dis_dict[search_][x])
                min_dis = self.dis_dict[search_][min_next_vertex]
                if min_dis <= min_distance:
                    pre_vertex = search_
                    select_vertex = min_next_vertex
                    min_distance = min_dis
            alternative_vertexes_.discard(select_vertex)
            fixed_vertexes.add(select_vertex)
            self.dis_dict[search_pos][select_vertex] = self.dis_dict[search_pos][pre_vertex] + \
                                                       self.dis_dict[pre_vertex][select_vertex]
        return self.dis_dict[search_pos]


class Solution:
    def minimalSteps(self, maze: list) -> int:
        start_coordinate: tuple = ()
        target_coordinate: tuple = ()
        stone_coordinate: list = []
        trigger_coordinate: list = []
        for i, _ in enumerate(maze):
            for j, mark in enumerate(maze[i]):
                if mark == 'S':
                    start_coordinate: tuple = (i, j)
                elif mark == 'O':
                    stone_coordinate.append((i, j))
                elif mark == 'T':
                    target_coordinate = (i, j)
                elif mark == 'M':
                    trigger_coordinate.append((i, j))
        maze = [[1 if i != '#' else 0 for i in maze[j]] for j in range(len(maze))]
        min_dict: Dijkstar = Dijkstar(maze)
        start_dict: dict = min_dict.search(start_coordinate)
        target_dict: dict = min_dict.search(target_coordinate)
        stone_dict: dict = {i: min_dict.search(i) for i in stone_coordinate}
        trigger_dict: dict = {i: min_dict.search(i) for i in trigger_coordinate}
        print(trigger_dict)



s = Solution()
s.minimalSteps(["S#O", "M..", "M.T", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M..", "M.."])
