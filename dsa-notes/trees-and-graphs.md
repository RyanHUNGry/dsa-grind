# Types of Trees:
- Properties of all Trees:
    1. Each tree has a root node, (Actually, this isn't strictly necessary in graph theory, but it's usually how we use trees in programming, and especially programming interviews.)
    2. The root node has zero or more child nodes
    3. Each child node has zero or more child nodes and so on

- Binary Tree:
    1. Tree in which node has up to 2 children

- Binary Search Tree:
    1. Binary tree in which node's left descendents are <= the node's value and right descendents are > than the node's value
    2. Certain BSTs do not allow duplicates, in which case the equalities are < and >; certain BSTS have the equalities < and >=
    3. Make sure to clarify the conditions of BST first with interviewer

- Balanced vs Unbalanced Trees:
    1. A balanced tree gaurantees O(logN) insertion and searching
    2. An unbalanced tree has O(N) insertion and searching because it is essentially a linked list
    3. Definition of balance varies, but most common is height balance such that left and right branches have heights that do not differ more than 1

- Complete Binary Tree:
    1. Every level of tree is filled
    2. If the last level is not filled fully but is filled from the left to right, tree is still complete

- Full Binary Trees:
    1. Every node has either 0 or 2 children
    2. Node never has 1 child

- Perfect Binary Trees:
    1. Tree that is both full (covers the last level as well) and complete 
    2. Perfect, model representation of a binary tree

# Binary Tree Traversal:
- In-order Traversal:
    1. Left, current, right
    2. If performed on binary search tree, it visits nodes in ascending order

- Pre-order Traversal:
    1. Current, left, right
    2. The root is always the first node visited

- Post-order Traversal:
    1. Left, right, current
    2. The root is always the last node visited

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Preorder-from-Inorder-and-Postorder-traversals.jpg)

# Heaps:
- Min-heap:
    1. Complete binary tree
    2. Each node is smaller than all its children
    3. Root node will be the minimum value
- Max-heap:
    1. Same as min-heap but root is the maximum value
- Insertion:
    1. We insert the element at the bottom, rightmost spot to maintain completeness
    2. Bubble up the inserted element so that it is in the correct spot
    3. O(logN)
- Extract Min or Max:
    1. The min or max will always be at the top of the tree depending on which heap you are using
    2. Remove topmost element and swap it with the bottom most
    3. Then, bubble down with the smaller/bigger element 
    4. O(logN)

# Tries (Prefix Trees):
- Definition of a Tree:
    1. N-ary tree in which characters are stored at each node
    2. Each path down the tree may represent a word
    3. Null nodes are used to indicate complete words
- Use Cases:
    1. Good for quick prefix lookups
    2. Can check if a string is a valid prefix in O(K) where K is the length of the string
    3. Better than hash tables

# Graphs:
- Adjacency List:
    1. Each ndoe in the graph stores a list of adjacent vertices
- Adjacency Matrix:
    1. NxN boolean matrix where N is the number of nodes
    2. A value of true at index (i, j) represents an edge from node i to node j
    3. If undirected, matrix will be symmetric; else, it will not necessarily be
    4. Not as easy to run common graph algorithms such as BFS/DFS
- Depth First Search:
    1. Explore each branch completely before moving on to the next branch
    2. Preferred if need to visit every node in the graph
    3. Tree traversals are essentially DFS
    4. Uses recursion/stack and relies on backtracking
    5. Better if destination is far from root node
- Breadth First Search:
    1. Explore each neighbor before going on to any of their children
    2. Better for finding shortest path (or just any path) between two nodes
    3. Uses a queue
    4. Better if destination is closer to root node
- Bidirectional Serach:
    1. Used to find shortest path between a source and destination node
    2. Runs two BFS from each node and when searches collide, there will be a path
    3. Shortens the runtime of utilizing just one BFS
