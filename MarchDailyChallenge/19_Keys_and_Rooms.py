class Solution:
    def canVisitAllRooms(self, R: list) -> bool:
        vis, stack, count = [False for _ in range(len(R))], [0], 1
        vis[0] = 1
        while stack:
            keys = R[stack.pop()]
            for k in keys:
                if not vis[k]:
                    stack.append(k)
                    vis[k] = True
                    count += 1
        return len(R) == count
