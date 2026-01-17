# 📘 Algorithm Analysis

### **Understanding Time and Space Complexity (Big-O Notation)**

---

## ## 1. What is Algorithm Analysis?

Algorithm analysis helps us measure:

* **Time Complexity** → How fast an algorithm runs
* **Space Complexity** → How much extra memory it uses

We usually consider **worst-case complexity** using **Big-O notation**.

---

# ## 2. Big-O Notation

Big-O describes how runtime grows as input size **n** increases.

### ### Common Big-O Complexities

| Big-O          | Name         | Example                           |
| -------------- | ------------ | --------------------------------- |
| **O(1)**       | Constant     | Accessing array element           |
| **O(log n)**   | Logarithmic  | Binary search                     |
| **O(n)**       | Linear       | Loop through array                |
| **O(n log n)** | Linearithmic | Merge sort, Quick sort (avg)      |
| **O(n²)**      | Quadratic    | Nested loops                      |
| **O(2ⁿ)**      | Exponential  | Subset generation                 |
| **O(n!)**      | Factorial    | Travelling Salesman (brute force) |

---

## ## 3. Time Complexity Examples

### Example 1:

```python
for i in range(n):
    print(i)
```

➡️ **O(n)**

### Example 2:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

➡️ **O(n²)**

### Example 3:

```python
print(arr[0])
```

➡️ **O(1)**

---

## ## 4. Space Complexity

Measures additional memory:

### Example:

```python
arr2 = arr[:]   # copies n elements
```

➡️ **Space: O(n)**

### Recursion uses **call stack memory**

Each recursive call adds a frame → So recursion often consumes **O(n)** space.

---

# ---------------------------------------

# 📘 Recursion

### **Principles, Working, and Applications**

---

## ## 1. What is Recursion?

A function calling *itself* to solve a smaller version of the problem.

### A recursive function must have:

1. **Base Case** → stops recursion
2. **Recursive Case** → reduces the problem

---

## ## 2. Example: Factorial

```python
def fact(n):
    if n == 0:        # Base case
        return 1
    return n * fact(n-1)   # Recursive call
```

### Time Complexity: **O(n)**

### Space Complexity: **O(n)** (call stack)

---

## ## 3. Example: Fibonacci (naive)

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

### Time Complexity: **O(2ⁿ)** (very slow)

### Space Complexity: **O(n)**

---

## ## 4. When to Use Recursion?

* Tree/graph traversal
* Divide-and-Conquer algorithms
* Backtracking (e.g., N-Queens)
* Mathematical problems (factorial, Fibonacci)
* Solving problems that reduce into smaller versions

---

## ## 5. Tail Recursion (Python does not optimize it)

```python
def tail_rec(n, acc=1):
    if n == 0:
        return acc
    return tail_rec(n-1, acc*n)
```

Python still uses stack → **no optimization**.

---

# ---------------------------------------

# 📘 Divide and Conquer

### **Break → Solve → Combine Strategy**

---

## ## 1. What is Divide and Conquer?

Algorithm steps:

1. **Divide** → Split problem into subproblems
2. **Conquer** → Solve subproblems (often recursively)
3. **Combine** → Merge solutions

---

## ## 2. Common Examples

| Algorithm                            | Time Complexity               | Notes                        |
| ------------------------------------ | ----------------------------- | ---------------------------- |
| **Merge Sort**                       | O(n log n)                    | Stable, uses extra space     |
| **Quick Sort**                       | Avg: O(n log n), Worst: O(n²) | Faster in practice           |
| **Binary Search**                    | O(log n)                      | Divide array by 2 every step |
| **Strassen’s Matrix Multiplication** | O(n^2.8)                      | Faster than standard O(n^3)  |

---

# ## 3. Example: Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])      # Divide
    right = merge_sort(arr[mid:])
    
    return merge(left, right)         # Combine
```

### Time Complexity: **O(n log n)**

### Space Complexity: **O(n)**

---

# ## 4. Example: Binary Search

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low+high)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
```

➡️ Cuts search space in half → **O(log n)**

---

# ## 5. Why Divide & Conquer is Powerful?

✓ Works well for large datasets
✓ Reduces complexity drastically
✓ Enables parallel processing
✓ Forms basis of many algorithms in ML, DS, OS, and graphics

---

# ---------------------------------------

# 📌 Summary Table

| Topic              | Key Idea                | Typical Time | Space            |
| ------------------ | ----------------------- | ------------ | ---------------- |
| Algorithm Analysis | Measure efficiency      | varies       | varies           |
| Recursion          | Function calling itself | O(n), O(2ⁿ)  | O(n)             |
| Divide & Conquer   | Break-solve-merge       | O(n log n)   | O(log n) or O(n) |

---


