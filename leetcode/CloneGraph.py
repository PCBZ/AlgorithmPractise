class Node:
     def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node: 'Node') -> 'Node':
            if node in visited:
                return visited[node]
            node_copy = Node(node.val)
            visited[node] = node_copy
            for neighbor in node.neighbors:
                node_copy.neighbors.append(dfs(neighbor))
            return node_copy
        visited = {}
        return dfs(node)

        

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

# Solution
sol = Solution()
cloned_graph = sol.cloneGraph(node1)

# Print cloned graph to verify
print(cloned_graph.val)  # Output: 1
print([neighbor.val for neighbor in cloned_graph.neighbors])  # Output: [2, 4]