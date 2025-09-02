"""
Comprehensive tests for LeetCode Problem #133: Clone Graph.
Tests the graph cloning functionality with DFS approach.
"""

import pytest

from leetcode.clone_graph import Solution, Node


class TestCloneGraph:
    """Test cases for the clone graph problem."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()

    def test_example_case_1(self):
        """Test LeetCode example 1: adjList = [[2,4],[1,3],[2,4],[1,3]]."""
        # Create graph: 1-2, 1-4, 2-3, 3-4
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]
        
        cloned = self.solution.cloneGraph(node1)
        
        # Verify structure
        assert cloned.val == 1
        assert len(cloned.neighbors) == 2
        assert sorted([n.val for n in cloned.neighbors]) == [2, 4]
        
        # Verify it's a deep copy
        assert cloned is not node1
        assert all(n is not node1.neighbors[i] for i, n in enumerate(cloned.neighbors))

    def test_example_case_2(self):
        """Test LeetCode example 2: adjList = [[]]."""
        node1 = Node(1)
        
        cloned = self.solution.cloneGraph(node1)
        
        assert cloned.val == 1
        assert len(cloned.neighbors) == 0
        assert cloned is not node1

    def test_example_case_3(self):
        """Test LeetCode example 3: adjList = []."""
        cloned = self.solution.cloneGraph(None)
        assert cloned is None

    def test_single_node_with_self_loop(self):
        """Test a single node that points to itself."""
        node1 = Node(1)
        node1.neighbors = [node1]
        
        cloned = self.solution.cloneGraph(node1)
        
        assert cloned.val == 1
        assert len(cloned.neighbors) == 1
        assert cloned.neighbors[0] is cloned  # Self-reference maintained
        assert cloned is not node1

    def test_two_node_cycle(self):
        """Test a simple two-node cycle."""
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        
        cloned = self.solution.cloneGraph(node1)
        
        assert cloned.val == 1
        assert len(cloned.neighbors) == 1
        assert cloned.neighbors[0].val == 2
        assert cloned.neighbors[0].neighbors[0] is cloned
        assert cloned is not node1

    def test_linear_graph(self):
        """Test a linear graph: 1-2-3-4."""
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node3]
        
        cloned = self.solution.cloneGraph(node1)
        
        # Traverse the cloned graph
        current = cloned
        values = [current.val]
        prev = None
        
        while len(current.neighbors) > 0:
            next_node = None
            for neighbor in current.neighbors:
                if neighbor != prev:
                    next_node = neighbor
                    break
            if next_node is None:
                break
            values.append(next_node.val)
            prev = current
            current = next_node
            
        assert values == [1, 2, 3, 4]

    def test_star_graph(self):
        """Test a star graph where center connects to all others."""
        center = Node(1)
        nodes = [Node(i) for i in range(2, 6)]  # Nodes 2, 3, 4, 5
        
        center.neighbors = nodes
        for node in nodes:
            node.neighbors = [center]
        
        cloned = self.solution.cloneGraph(center)
        
        assert cloned.val == 1
        assert len(cloned.neighbors) == 4
        neighbor_vals = sorted([n.val for n in cloned.neighbors])
        assert neighbor_vals == [2, 3, 4, 5]
        
        # All neighbors should only connect back to center
        for neighbor in cloned.neighbors:
            assert len(neighbor.neighbors) == 1
            assert neighbor.neighbors[0] is cloned

    def test_triangle_graph(self):
        """Test a triangle graph: 1-2-3-1."""
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.neighbors = [node2, node3]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node1, node2]
        
        cloned = self.solution.cloneGraph(node1)
        
        assert cloned.val == 1
        assert len(cloned.neighbors) == 2
        
        # Find nodes 2 and 3
        node2_clone = None
        node3_clone = None
        for neighbor in cloned.neighbors:
            if neighbor.val == 2:
                node2_clone = neighbor
            elif neighbor.val == 3:
                node3_clone = neighbor
        
        assert node2_clone is not None
        assert node3_clone is not None
        
        # Verify triangle connections
        assert cloned in node2_clone.neighbors
        assert node3_clone in node2_clone.neighbors
        assert cloned in node3_clone.neighbors
        assert node2_clone in node3_clone.neighbors

    def test_complex_graph(self):
        """Test a more complex graph structure."""
        nodes = [Node(i) for i in range(1, 6)]  # Nodes 1-5
        
        # Create connections: 1->[2,3], 2->[1,4], 3->[1,4,5], 4->[2,3,5], 5->[3,4]
        nodes[0].neighbors = [nodes[1], nodes[2]]  # 1 -> [2, 3]
        nodes[1].neighbors = [nodes[0], nodes[3]]  # 2 -> [1, 4]
        nodes[2].neighbors = [nodes[0], nodes[3], nodes[4]]  # 3 -> [1, 4, 5]
        nodes[3].neighbors = [nodes[1], nodes[2], nodes[4]]  # 4 -> [2, 3, 5]
        nodes[4].neighbors = [nodes[2], nodes[3]]  # 5 -> [3, 4]
        
        cloned = self.solution.cloneGraph(nodes[0])
        
        # Verify all nodes are reachable and correctly connected
        visited = set()
        
        def verify_structure(node, original_val):
            if original_val in visited:
                return
            visited.add(original_val)
            
            assert node.val == original_val
            original_node = nodes[original_val - 1]
            
            assert len(node.neighbors) == len(original_node.neighbors)
            neighbor_vals = sorted([n.val for n in node.neighbors])
            expected_vals = sorted([n.val for n in original_node.neighbors])
            assert neighbor_vals == expected_vals
            
            for neighbor in node.neighbors:
                verify_structure(neighbor, neighbor.val)
        
        verify_structure(cloned, 1)
        assert len(visited) == 5

    def test_duplicate_node_values(self):
        """Test graph with duplicate node values."""
        node1a = Node(1)
        node1b = Node(1)
        node2 = Node(2)
        
        node1a.neighbors = [node1b, node2]
        node1b.neighbors = [node1a]
        node2.neighbors = [node1a]
        
        cloned = self.solution.cloneGraph(node1a)
        
        assert cloned.val == 1
        assert len(cloned.neighbors) == 2
        
        # Both neighbors should be distinct objects
        neighbor_vals = [n.val for n in cloned.neighbors]
        assert 1 in neighbor_vals
        assert 2 in neighbor_vals

    def test_large_graph_performance(self):
        """Test performance with a larger graph."""
        # Create a grid-like graph 10x10
        size = 10
        nodes = [[Node(i * size + j) for j in range(size)] for i in range(size)]
        
        # Connect each node to its neighbors (up, down, left, right)
        for i in range(size):
            for j in range(size):
                neighbors = []
                if i > 0:
                    neighbors.append(nodes[i-1][j])
                if i < size - 1:
                    neighbors.append(nodes[i+1][j])
                if j > 0:
                    neighbors.append(nodes[i][j-1])
                if j < size - 1:
                    neighbors.append(nodes[i][j+1])
                nodes[i][j].neighbors = neighbors
        
        # Clone from top-left corner
        cloned = self.solution.cloneGraph(nodes[0][0])
        
        # Verify the clone has the same structure
        assert cloned.val == 0
        
        # Do a BFS to count total nodes
        queue = [cloned]
        visited = {cloned}
        count = 0
        
        while queue:
            node = queue.pop(0)
            count += 1
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        assert count == size * size

    def test_return_type(self):
        """Test that the function returns the correct type."""
        node1 = Node(1)
        result = self.solution.cloneGraph(node1)
        assert isinstance(result, Node)
        
        result_none = self.solution.cloneGraph(None)
        assert result_none is None

    def test_deep_copy_verification(self):
        """Test that the clone is truly a deep copy."""
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors = [node2]
        node2.neighbors = [node1]
        
        cloned = self.solution.cloneGraph(node1)
        
        # Modify original
        node1.val = 999
        node2.val = 888
        
        # Clone should be unaffected
        assert cloned.val == 1
        assert cloned.neighbors[0].val == 2

    def test_node_identity_preservation(self):
        """Test that node identities are correctly preserved in clone."""
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        
        # Create multiple references to same nodes
        node1.neighbors = [node2, node3, node2]  # node2 appears twice
        node2.neighbors = [node1]
        node3.neighbors = [node1]
        
        cloned = self.solution.cloneGraph(node1)
        
        # The cloned node2 references should be the same object
        assert cloned.neighbors[0] is cloned.neighbors[2]
        assert cloned.neighbors[0].val == 2
        assert cloned.neighbors[1].val == 3

    def test_algorithm_correctness(self):
        """Test that DFS traversal maintains graph properties."""
        # Create a graph where order matters
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        
        # Specific connection pattern
        node1.neighbors = [node2, node3]
        node2.neighbors = [node4]
        node3.neighbors = [node4]
        node4.neighbors = []
        
        cloned = self.solution.cloneGraph(node1)
        
        # Verify the DAG structure is maintained
        assert cloned.val == 1
        assert len(cloned.neighbors) == 2
        
        # Both paths should lead to node 4
        node4_clones = []
        for neighbor in cloned.neighbors:
            if len(neighbor.neighbors) > 0:
                node4_clones.append(neighbor.neighbors[0])
        
        # Should be the same node 4 clone
        assert len(node4_clones) == 2
        assert node4_clones[0] is node4_clones[1]
        assert node4_clones[0].val == 4

    @pytest.mark.parametrize("node_count,expected_cloned", [
        (1, True),
        (2, True),
        (3, True),
        (5, True),
        (10, True),
    ])
    def test_parametrized_node_counts(self, node_count, expected_cloned):
        """Test cloning with different numbers of nodes."""
        # Create a cycle graph
        nodes = [Node(i) for i in range(1, node_count + 1)]
        
        for i in range(node_count):
            next_idx = (i + 1) % node_count
            nodes[i].neighbors = [nodes[next_idx]]
        
        cloned = self.solution.cloneGraph(nodes[0])
        
        if expected_cloned:
            assert cloned is not None
            assert cloned.val == 1
            
            # Traverse the cycle and count nodes
            visited_vals = set()
            current = cloned
            
            while current.val not in visited_vals:
                visited_vals.add(current.val)
                if len(current.neighbors) > 0:
                    current = current.neighbors[0]
                else:
                    break
            
            assert len(visited_vals) == node_count

    def test_empty_neighbors_list(self):
        """Test nodes with explicitly empty neighbors list."""
        node1 = Node(1, [])
        
        cloned = self.solution.cloneGraph(node1)
        
        assert cloned.val == 1
        assert len(cloned.neighbors) == 0
        assert cloned is not node1

    def test_cloning_maintains_graph_connectivity(self):
        """Test that all connectivity is maintained after cloning."""
        # Create a fully connected graph of 4 nodes
        nodes = [Node(i) for i in range(1, 5)]
        
        for i in range(4):
            nodes[i].neighbors = [nodes[j] for j in range(4) if j != i]
        
        cloned = self.solution.cloneGraph(nodes[0])
        
        # Collect all cloned nodes
        all_cloned = set()
        queue = [cloned]
        all_cloned.add(cloned)
        
        while queue:
            current = queue.pop(0)
            for neighbor in current.neighbors:
                if neighbor not in all_cloned:
                    all_cloned.add(neighbor)
                    queue.append(neighbor)
        
        assert len(all_cloned) == 4
        
        # Each node should connect to all others
        for node in all_cloned:
            assert len(node.neighbors) == 3
            neighbor_vals = {n.val for n in node.neighbors}
            expected_vals = {1, 2, 3, 4} - {node.val}
            assert neighbor_vals == expected_vals
