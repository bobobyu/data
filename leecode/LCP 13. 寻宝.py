class Solution:
    def minimalSteps(self, maze: list) -> int:
        special_coordinates: dict = {'start': [], 'stone': [], 'target': [], 'trigger': []}
        length: int = len(maze[0])
        height: int = len(maze)
        for i in range(length):
            for j in range(height):
                current_mark: str = maze[j][i]
                if current_mark == 'S':
                    special_coordinates['start'] = (j, i)
                elif current_mark == 'T':
                    special_coordinates['target'] = (j, i)
                elif current_mark == 'O':
                    special_coordinates['stone'].append((j, i))
                elif current_mark == 'M':
                    special_coordinates['trigger'].append((j, i))
        print(special_coordinates)

        def BFS(start: tuple, target: tuple):
            start_list = [start]
            visited_set: set = set()
            step_count: int = 0
            while start_list and target not in start_list:
                next_start_list: list = []
                for coordinate in start_list:
                    if coordinate[0] < height - 1 and maze[coordinate[0] + 1][coordinate[1]] != '#' and (
                            coordinate[0] + 1, coordinate[1]) not in visited_set:
                        next_start_list.append((coordinate[0] + 1, coordinate[1]))
                        visited_set.add((coordinate[0] + 1, coordinate[1]))
                    if coordinate[0] > 0 and maze[coordinate[0] - 1][coordinate[1]] != '#' and (
                            coordinate[0] - 1, coordinate[1]) not in visited_set:
                        next_start_list.append((coordinate[0] - 1, coordinate[1]))
                        visited_set.add((coordinate[0] - 1, coordinate[1]))
                    if coordinate[1] < length - 1 and maze[coordinate[0]][coordinate[1] + 1] != '#' and (
                            coordinate[0], coordinate[1] + 1) not in visited_set:
                        next_start_list.append((coordinate[0], coordinate[1] + 1))
                        visited_set.add((coordinate[0], coordinate[1] + 1))
                    if coordinate[1] > 0 and maze[coordinate[0]][coordinate[1] - 1] != '#' and (
                            coordinate[0], coordinate[1] - 1) not in visited_set:
                        next_start_list.append((coordinate[0], coordinate[1] - 1))
                        visited_set.add((coordinate[0], coordinate[1] - 1))
                step_count += 1
                start_list = next_start_list.copy()
                next_start_list.clear()

            print(start_list)
            return -1 if not start_list else step_count

        print(BFS((0, 0), (2, 0)))


s = Solution()
s.minimalSteps(["S.O",
                "##.",
                "M.T"])
