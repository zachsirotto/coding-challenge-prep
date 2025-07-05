# Coding Challenge Prep

Structured plan to refresh DFS, BFS, Stacks, Queues, Caches, DP.

---

## ✅ Goals

- Refresh fundamentals of DFS, BFS, Queues, Stacks, Caches, and Hashmaps  
- Understand real-world and algorithmic applications  
- Practice interview-level problems involving combinations of these, including memoization/DP  
- Build intuition for when to use what  

---

## 📆 Day-by-Day Plan

---

### 🗓️ Day 1 AM: Core Concepts & Implementation

#### 🔹 1. Stacks & Queues

- **Theory**: LIFO vs FIFO  
- **Use cases**: Undo functionality, tree/graph traversal, level-order processing  

**Implement**:
- Stack (array & linked list)
- Queue (array & circular buffer)
- Deque

**Practice**:

- [ ] [Day 18: Queues and Stacks (Hackerrank)](https://www.hackerrank.com/challenges/30-queues-stacks/problem)

#### 🔹 2. DFS vs BFS

**DFS**:
- Use: Topological sort, connected components, backtracking (e.g., permutations)  
- Implement: Recursive & iterative  

**BFS**:
- Use: Shortest path (unweighted graphs), level-order traversal  
- Implement: With Queue  

**Practice (1–2 easy-medium per topic)**:
- [ ] LeetCode 102 – Binary Tree Level Order Traversal  
- [ ] LeetCode 200 – Number of Islands (DFS/BFS)  
- [ ] LeetCode 22 – Generate Parentheses (Backtracking/DFS)

---

### 🗓️ Day 1 PM: Hashmaps, Caches, and Real-World Patterns

#### 🔹 3. Hashmaps

- **Use cases**: Frequency counting, lookups in O(1), sliding window  

**Practice**:
- [ ] LeetCode 1 – Two Sum  
- [ ] LeetCode 387 – First Unique Character in a String  

#### 🔹 4. Caches

- **LRU Cache**: Implement with HashMap + Doubly Linked List  
- **Understand**:
  - Why HashMap alone doesn’t work  
  - O(1) eviction strategy  
  - Implement LRU from scratch  
  - [ ] LeetCode 146 – LRU Cache  

---

### 🗓️ Day 2 AM: Applications in Dynamic Programming & Memoization

#### 🔹 5. DFS + Memoization

- **Use**: Optimal substructure problems, avoiding recomputation  

**Practice**:
- [ ] LeetCode 70 – Climbing Stairs  
- [ ] LeetCode 198 – House Robber  
- [ ] LeetCode 494 – Target Sum (DFS + Memo)  

#### 🔹 6. BFS in Grid Problems

**Practice**:
- [ ] LeetCode 542 – 01 Matrix  
- [ ] LeetCode 127 – Word Ladder  

---

### 🗓️ Day 2 PM: Mixed Practice & Mock

#### 🔹 7. Integrating Concepts

- Choose problems involving:
  - Stack + Hashmap (e.g., LeetCode 20 – Valid Parentheses)  
  - BFS + HashSet  
  - DFS + Memo + HashMap  

**Practice**:
- [ ] LeetCode 155 – Min Stack  
- [ ] LeetCode 560 – Subarray Sum Equals K (Prefix sums + HashMap)  
- [ ] LeetCode 124 – Binary Tree Max Path Sum (DFS + DP)  

#### 🔹 8. Mock Challenge

- Set timer: pick 2–3 random problems across these concepts  
- Simulate coding environment  

---

## 📚 Optional Review Resources

- [NeetCode’s playlist](https://www.youtube.com/c/NeetCode) – curated for interviews  
- [LeetCode Explore Cards](https://leetcode.com/explore/) – for topic-based refreshers  
- [VisuAlgo](https://visualgo.net/en) – for animation-based understanding  
