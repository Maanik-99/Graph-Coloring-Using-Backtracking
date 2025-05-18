# Graph Coloring using Backtracking

This project solves the Graph Coloring problem using the Backtracking algorithm. The goal is to determine whether a graph can be colored using **K colors** such that **no two adjacent vertices share the same color**.

## 🧠 Algorithm

The algorithm uses a recursive backtracking approach:
- Try to assign colors to each vertex from 1 to K.
- Ensure no two adjacent vertices have the same color.
- Backtrack when a conflict occurs.

## 📥 Input Format

The input is read from a file named `input.txt`.

- First line: `N M K`
  - N = Number of vertices (0 to N-1)
  - M = Number of edges
  - K = Number of colors
- Next M lines: Each line contains two integers `u` and `v` indicating an edge between vertex u and vertex v.

### Example `input.txt`
```bash

4 5 3
0 1
0 2
1 2
1 3
2 3
```

## ▶️ How to Run

```bash
python graph_coloring.py
```
##📌  Output 
![image](https://github.com/user-attachments/assets/469a4085-c6e5-45ed-9f19-a0c3133963d7)
