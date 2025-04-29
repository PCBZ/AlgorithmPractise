from typing import List, Set

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def is_safe_node(node: int, visited: Set[int]) -> bool:
            if node in terminal_nodes or node in safe_nodes:
                return True
            if node in visited:
                return False
            visited.add(node)
            ret = True
            for next_node in graph[node]:
                ret &= is_safe_node(next_node, visited.copy())
            return ret
        
        terminal_nodes = set([i for i, nodes in enumerate(graph) if not nodes])
        safe_nodes = set()

        for node in range(len(graph)):
            if node not in terminal_nodes and is_safe_node(node, set()):
                safe_nodes.add(node)
        
        return list(safe_nodes | terminal_nodes)

if __name__ == "__main__":
    # graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    graph = [[],[0,2,3,4],[3],[4],[]]
    # graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    print(Solution().eventualSafeNodes(graph))
                    