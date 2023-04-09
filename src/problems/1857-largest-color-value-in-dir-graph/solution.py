from typing import List, Set, Dict
from collections import Counter

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
      n = len(colors)
      adj = [[] for i in range(n)]
      indegree = [0 for i in range(n)]
      
      for edge in edges:
        adj[edge[0]].append(edge[1])
        indegree[edge[1]] += 1

      count = [[0 for i in range(26)] for j in range(n)]
      
      q = []
      
      for i in range(n):
        if indegree[i] == 0:
          q.append(i)
          
      answer = 0
      nodesSeen = 0
      
      while len(q) > 0:
        node = q.pop()
        nodeColorIndex = ord(colors[node]) - ord('a')

        count[node][nodeColorIndex] += 1
        answer = max(answer, count[node][nodeColorIndex])
        
        nodesSeen += 1
        
        for neighbor in adj[node]:
          for i in range(26):
            count[neighbor][i] = max(count[neighbor][i], count[node][i])
        
          indegree[neighbor] -= 1
          
          if indegree[neighbor] == 0:
            q.append(neighbor)

      return answer if nodesSeen >= n else -1

if __name__ == '__main__':
  sol = Solution()

  assert sol.largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]]) == 3

  assert sol.largestPathValue("a", [[0,0]]) == -1
  
  assert sol.largestPathValue("hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]) == 3

