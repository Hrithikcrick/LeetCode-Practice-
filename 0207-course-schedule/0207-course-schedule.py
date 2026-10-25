from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        count=0
        while queue:
            node=queue.popleft()
            count+=1
            for nei in graph[node]:
                indegree[nei]-=1
               
                if indegree[nei]==0:
                    queue.append(nei)
        return count==numCourses

    
        
