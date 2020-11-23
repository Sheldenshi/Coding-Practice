# Question:
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

 

Constraints:

    The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    You may assume that there are no duplicate edges in the input prerequisites.
    1 <= numCourses <= 10^5
"""

# Solution:

class Solution:
     # return True if there is a circle
    def dfs(self, node: int) -> bool:
        if self.mark[node] == 2:
            return False
        if self.mark[node] == 1:
            return True
        self.mark[node] = 1
        for nei in self.adj[node]:
            if self.dfs(nei):
                return True
        self.mark[node] = 2
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj = [None] * numCourses
        for i in range(numCourses): # Time O(V)
            self.adj[i] = [] 
        for pre in prerequisites: # Time O(E)
            self.adj[pre[0]].append(pre[1])
            
        self.mark = [0] * numCourses
        # 0 is not visted
        # 1 is visiting
        # 2 is compleated
        for pre in prerequisites: # Time O(V + E)
            if not self.mark[pre[0]]:
                if self.dfs(pre[0]):
                    return False
        return True
