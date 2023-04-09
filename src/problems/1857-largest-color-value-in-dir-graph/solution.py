from typing import List, Set, Dict
from collections import Counter

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:    			

      def colorLeaves(node: int, color: str = ""):
        color += colors[node]

        if node in map:
          for adjNode in map[node]:
            colorLeaves(adjNode, color)
        else:
          if not node in leavesColors:
            leavesColors[node] = set()
            
          leavesColors[node].add(color)

      n = len(colors)
      map = self.buildAdjMap(edges)
      roots = self.findRoots(edges, n)

      if len(roots) == 0:
        return -1

      leavesColors = { }

      for root in roots:
        colorLeaves(root)	

      max = 0

      for leaf in leavesColors:
        for leafColor in leavesColors[leaf]:
          counter = Counter(leafColor)
          leafMax = counter.most_common(1)[0][1]
          max = max if max > leafMax else leafMax

      return max
    
    def buildAdjMap(self, edges: List[List[int]]) -> Dict[int, Set[int]]:
      map = {}

      for edge in edges:
        n1 = edge[0]
        n2 = edge[1]

        if not n1 in map:
          map[n1] = set()

        map[n1].add(n2)

      return map
    
    def findRoots(self, edges: List[List[int]], n: int) -> Set[int]:
      roots = set(i for i in range(n))

      for edge in edges:
        if edge[1] in roots:
          roots.remove(edge[1])
    
      return roots

if __name__ == '__main__':
  sol = Solution()

  assert sol.largestPathValue("hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]) == 3

  assert sol.largestPathValue("abaca", [[0,1],[0,2],[2,3],[3,4]]) == 3

  assert sol.largestPathValue("a", [[0,0]]) == -1
