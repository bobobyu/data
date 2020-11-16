class Solution:
    def bestLine(self, points: list) -> list:
        index_dict: dict = {tuple(j): i for i, j in enumerate(points)}
        search_distance:dict = {}
        max_count: int = 0
        while points:
            current_point = points.pop()
            current_max_count: int = 0
            current_cross: list = []
            for point in points:

                #竖直

                row_ = abs(current_point[0] - point[0])
                col_ = abs(point[1] - current_point[1])
                if row_ == col_ or row_ == 0 or col_ == 0:
                    current_max_count += 1
                    current_cross.append(point)
            print(current_cross)
            if current_max_count >= max_count:
                max_count = current_max_count
                print(max_count)
                search_distance[max_count] = search_distance.get(max_count, []) + [current_cross]
        print(search_distance)
    '''
    1 0
    1 1
    1 0
    '''
s = Solution()
s.bestLine([[0,0],[1,1],[1,0],[2,0]])