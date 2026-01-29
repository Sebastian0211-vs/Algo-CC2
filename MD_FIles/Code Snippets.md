# 🧩 Code Snippets – Templates Python Essentiels

Ce fichier contient les **squelettes de code les plus utilisés** en algorithmique.
Objectif :

> ne jamais réécrire un algo depuis zéro,
> éviter les erreurs bêtes,
> gagner du temps en examen.

---

## 🔹 BFS (graphe non pondéré)

```python
from collections import deque

def bfs(n, adj, start):
    visited = [False] * n
    dist = [-1] * n

    visited[start] = True
    dist[start] = 0
    q = deque([start])

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                q.append(v)

    return dist
```

---

## 🔹 BFS avec reconstruction de chemin

```python
def bfs_path(n, adj, start):
    from collections import deque

    dist = [-1] * n
    parent = [-1] * n

    dist[start] = 0
    q = deque([start])

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)

    return dist, parent
```

---

## 🔹 DFS récursif

```python
def dfs(u, adj, visited):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v, adj, visited)
```

---

## 🔹 DFS avec détection de cycle (orienté)

```python
def has_cycle(n, adj):
    state = [0] * n  # 0=unvisited, 1=visiting, 2=done

    def dfs(u):
        state[u] = 1
        for v in adj[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    return any(dfs(i) for i in range(n) if state[i] == 0)
```

---

## 🔹 Dijkstra (poids positifs)

```python
import heapq

def dijkstra(n, adj, start):
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist
```

---

## 🔹 0–1 BFS

```python
from collections import deque

def zero_one_bfs(n, adj, start):
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0

    dq = deque([start])

    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                if w == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)

    return dist
```

---

## 🔹 Union-Find (DSU)

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.parent[rb] = ra
        return True
```

---

## 🔹 Binary Search (classique)

```python
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        if arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1
```

---

## 🔹 Binary Search sur l’espace des réponses

```python
def binary_search_answer(low, high, ok):
    while low < high:
        mid = (low + high) // 2
        if ok(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

---

## 🔹 Sliding Window (taille variable)

```python
def sliding_window(arr):
    left = 0
    seen = set()

    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1
        seen.add(arr[right])
```

---

## 🔹 Backtracking (template)

```python
def backtrack(start, current):
    if condition:
        result.append(current.copy())
        return

    for i in range(start, n):
        current.append(i)
        backtrack(i + 1, current)
        current.pop()
```

---

## 🔹 Minimax + Alpha-Beta

```python
def minimax(node, depth, alpha, beta, is_max):
    if depth == 0 or node.is_terminal():
        return node.value()

    if is_max:
        best = float('-inf')
        for child in node.children():
            best = max(best, minimax(child, depth-1, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for child in node.children():
            best = min(best, minimax(child, depth-1, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
```

---

## 🔹 Reconstruction de chemin

```python
def reconstruct(parent, start, end):
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path if path[0] == start else []
```

---

## ✅ Règle d’or (exam mode)

* **Graphe → BFS / DFS**
* **Distance → BFS / Dijkstra**
* **Optimisation → Greedy / DP**
* **Génération → Backtracking**
* **Adversaire → Minimax**

