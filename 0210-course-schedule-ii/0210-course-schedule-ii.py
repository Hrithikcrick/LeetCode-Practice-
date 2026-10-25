class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph=[[] for _ in range(numCourses)]
        indegre=[0]*numCourses
        for a,b in prerequisites:
            graph[a].append(b)
            indegre[b]+=1
        queue=deque()
        for i in range(numCourses):
            if indegre[i]==0:
                queue.append(i)
        order=[]
        while queue:
            node=queue.popleft()
            order.append(node)
            for nei in graph[node]:
                indegre[nei]-=1
                if indegre[nei]==0:
                    queue.append(nei)
        return order[::-1] if len(order) == numCourses else []



        