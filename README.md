## 📊 Algorithms Basics — Complexity Analysis

### Problem: Search Algorithms
Comparing Linear Search O(n) vs Binary Search O(log n)

| Algorithm     | Best Case | Worst Case | Array of 1M elements |
|---------------|-----------|------------|----------------------|
| Linear Search | O(1)      | O(n)       | up to 1,000,000 ops  |
| Binary Search | O(1)      | O(log n)   | up to 20 ops         |

### Key Insight
This directly maps to database indexing: a table without
an index performs a full scan (Linear), while a B-Tree
index performs logarithmic lookups (Binary).