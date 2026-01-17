# # Core Algorithm Notes

---

# ## 1. Graph Algorithms

Graphs consist of **nodes (vertices)** and **edges**.
Can be **directed/undirected**, **weighted/unweighted**.

---

## ### 1.1 Graph Representations

* **Adjacency List** (most common)
* **Adjacency Matrix**
* **Edge List**

---

## ### 1.2 Graph Traversal Algorithms

### **Depth-First Search (DFS)**

* Explores as far as possible along a path before backtracking
* Implemented using **stack** (explicit or recursion)
* Time Complexity: **O(V + E)**
* Applications:

  * Cycle detection
  * Topological sort
  * Connected components
  * Solving mazes
  * Pathfinding (basic)

---

### **Breadth-First Search (BFS)**

* Explores level by level
* Implemented using **queue**
* Time Complexity: **O(V + E)**
* Applications:

  * Shortest path in unweighted graphs
  * Network broadcasting
  * Bipartite checking

---

## ### 1.3 Shortest Path Algorithms

### **Dijkstra’s Algorithm**

* Finds shortest path in **weighted, non-negative graphs**
* Uses a priority queue
* Time Complexity:

  * With heap: **O(E log V)**
* Applications:

  * GPS navigation
  * Network routing

---

### **Bellman-Ford Algorithm**

* Works with **negative weights**
* Detects negative cycles
* Time: **O(V × E)**

---

### **Floyd–Warshall**

* Computes shortest path between **all pairs**
* Works with negative edges (no negative cycles)
* Time: **O(V³)**

---

## ### 1.4 Minimum Spanning Tree Algorithms (MST)

### **Kruskal’s Algorithm**

* Sorts edges, uses Disjoint Set Union
* Time: **O(E log E)**
* Good for sparse graphs

### **Prim’s Algorithm**

* Grows MST from a starting node
* Time:

  * With heap: **O(E log V)**

---

## ### 1.5 Topological Sorting

* Ordering of nodes in a directed acyclic graph (DAG)
* Algorithms:

  * DFS-based
  * Kahn’s Algorithm (BFS-based)
* Applications:

  * Course scheduling
  * Task dependency ordering

---

# ---------------------------------------------

# ## 2. Searching Algorithms

---

## ### 2.1 Linear Search

* Check elements one by one
* Time: **O(n)**
* Works on **unsorted data**

---

## ### 2.2 Binary Search

* Works only on **sorted arrays**
* Divide search range by half each step
* Time: **O(log n)**
* Applications:

  * Searching in sorted arrays
  * Searching in infinite/unknown-sized arrays
  * Binary search on answer (optimization problems)

---

## ### 2.3 Depth/Breadth Search in Trees

* Tree DFS
* Tree BFS
* Common in:

  * File systems
  * Tree-based structures (BST, Heaps)

---

## ### 2.4 Searching in Graphs

* BFS
* DFS
* A* and Greedy Best First Search (heuristic-based)

---

# ---------------------------------------------

# ## 3. Sorting Algorithms

---

## ### 3.1 Comparison-Based Sorting

### **Bubble Sort**

* Swaps adjacent elements
* Time: **O(n²)**
* Easiest but slowest

---

### **Selection Sort**

* Select smallest each time
* Time: **O(n²)**
* Good for very small arrays or memory-limited systems

---

### **Insertion Sort**

* Build sorted array one element at a time
* Time: **O(n²)**
* Best case: **O(n)** (already sorted)
* Used in:

  * Small subarrays in QuickSort
  * Online sorting

---

### **Merge Sort**

* Divide and Conquer, stable
* Time: **O(n log n)**
* Space: **O(n)**
* Used in external sorting

---

### **Quick Sort**

* Partition-based
* Average: **O(n log n)**
* Worst: **O(n²)**
* Best in practice due to cache efficiency

---

### **Heap Sort**

* Uses binary heap
* Time: **O(n log n)**
* Space: **O(1)**
* Not stable but memory efficient

---

## ### 3.2 Non-Comparison Sorting

### **Counting Sort**

* For small integer ranges
* Time: **O(n + k)**
* Space: **O(k)**
* Stable

---

### **Radix Sort**

* Sorts digit by digit
* Uses Counting sort internally
* Time: **O(d(n + k))**
* Used for large integers, strings

---

### **Bucket Sort**

* Distribute into buckets and sort individually
* Time: **O(n)** average
* Good for uniform distribution data

---

# ---------------------------------------------

# ## Summary Table

| Category             | Core Algorithms                                                 | Typical Time       |
| -------------------- | --------------------------------------------------------------- | ------------------ |
| Graph Algorithms     | DFS, BFS, Dijkstra, Bellman-Ford, Floyd–Warshall, Kruskal, Prim | O(V+E), O(E log V) |
| Searching Algorithms | Linear, Binary, DFS/BFS                                         | O(n), O(log n)     |
| Sorting Algorithms   | Merge, Quick, Heap, Insertion, Bubble                           | O(n log n), O(n²)  |

---


