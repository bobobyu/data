from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[0], -x[1]))
        length = len(people)
        res: List[List[int]] = []
        for i in range(length - 1, -1, -1):
            height, rank = people[i][0], people[i][1]
            print(height, rank)
            if not res:
                res.append(people[i])
            else:
                point = 0
                while rank:
                    if res[point][0] >=height:
                        rank -= 1
                    point += 1
                res.insert(point, people[i])
        return res

s = Solution()
print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
