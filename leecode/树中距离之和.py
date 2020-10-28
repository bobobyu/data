edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
N = 6


class Solution:
    def sumOfDistancesInTree_(self, N: int, edges: list):
        stack: list = [N]
        edges_copy = edges[:]

        def dp(stack: list, edges: list, sum_count: int = 0, distance: int = 1):
            if stack:
                length: int = len(edges)
                next_edges: list = edges.copy()
                next_stack: list = []
                for i in stack:
                    for j in range(length):
                        if i == edges[j][0]:
                            next_stack.append(edges[j][1])
                            next_edges.remove(edges[j])
                            next_edges.remove(edges[j][::-1])
                sum_count += len(next_stack) * distance
                return dp(stack=next_stack, edges=next_edges, sum_count=sum_count, distance=distance + 1)
            else:
                return sum_count

        return dp(stack=stack, edges=edges_copy)

    def sumOfDistancesInTree(self, N: int, edges: list):
        length = len(edges)
        for i in range(length):
            edges.append(edges[i][::-1])
        return [self.sumOfDistancesInTree_(i, edges=edges) for i in range(N)]


a = Solution()
print(a.sumOfDistancesInTree(6, edges))
# print(a.sumOfDistancesInTree_(0, edges))
