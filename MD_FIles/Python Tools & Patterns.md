# 🛠️ Python – Outils & Fonctions Utiles en Algorithmique

Ce fichier regroupe les **structures de données** et **fonctions Python** les plus utiles
en algorithmique (graphes, DP, backtracking, greedy, etc.).

Objectif :

> savoir **quoi utiliser**, **quand**, et **pourquoi**, sans perdre de temps.

---

## 🔹 Structures de données fondamentales

### `list`

Structure de base, ordonnée, indexable.

Usages typiques :

* tableaux
* piles (`append`, `pop`)
* chemins (`path.append`, `path.pop`)

```python
arr = []
arr.append(3)
arr.pop()
```

⚠️ `pop(0)` est **O(n)** → éviter pour les files.

---

### `set`

Ensemble **sans doublons**, accès très rapide.

Usages typiques :

* détection de doublons
* états visités
* contraintes d’unicité (backtracking)

```python
s = set()
s.add(5)
if 5 in s:
    ...
```

Complexité :

* ajout / test : **O(1)** en moyenne

---

### `dict`

Table de hachage clé → valeur.

Usages typiques :

* comptage de fréquences
* mapping d’états
* graphes (adjacency list)

```python
freq = {}
freq[x] = freq.get(x, 0) + 1
```

Astuce :

```python
from collections import defaultdict
freq = defaultdict(int)
```

---

## 🔹 Files & piles

### `collections.deque`

File **efficace** (O(1) aux deux extrémités).

Indispensable pour :

* BFS
* 0–1 BFS
* sliding window

```python
from collections import deque

q = deque()
q.append(1)
q.appendleft(0)
q.popleft()
```

---

### Pile (stack) avec `list`

Simple et efficace.

```python
stack = []
stack.append(x)
stack.pop()
```

---

## 🔹 Fonctions Python utiles

### `enumerate`

Parcours index + valeur.

```python
for i, val in enumerate(arr):
    ...
```

---

### `range`

Boucles contrôlées, souvent utilisées pour DP.

```python
for i in range(n):
    ...
```

---

### `sorted()` et `.sort()`

Tri indispensable en greedy et backtracking.

```python
arr.sort()
arr = sorted(arr, reverse=True)
```

---

### `min()` / `max()`

Utilisés partout (DP, greedy, minimax).

```python
best = min(a, b)
```

---

### `sum()`

Sommes rapides (DP, fenêtres glissantes).

```python
total = sum(arr)
```

---

## 🔹 Outils algorithmiques clés

### `float('inf')`

Représente l’infini.

```python
INF = float('inf')
dist = [INF] * n
```

Indispensable pour :

* Dijkstra
* Bellman-Ford
* DP minimisation

---

### `heapq` (tas minimum)

Pour Dijkstra et greedy avancé.

```python
import heapq

pq = []
heapq.heappush(pq, (0, node))
dist, u = heapq.heappop(pq)
```

---

## 🔹 Patterns très fréquents

### Tableau `visited`

Pour DFS / BFS.

```python
visited = [False] * n
```

---

### Tableau `parent` (reconstruction de chemin)

```python
parent = [-1] * n
parent[v] = u
```

---

### Backtracking – copie de liste

```python
res.append(current.copy())
```

⚠️ ne jamais stocker `current` directement.

---

## 🔹 Fonctions math utiles

### `abs()`

Distances, différences.

```python
abs(a - b)
```

---

### `math.log2`, `math.ceil`

Utiles pour LCA / binary lifting.

```python
from math import log2, ceil
LOG = ceil(log2(n))
```

---

## 🔹 Bonnes pratiques (exam-friendly)

* Préférer `set` à `list` pour les tests d’appartenance
* Préférer `deque` à `list` pour les files
* Toujours initialiser clairement (`INF`, `-1`)
* Nommer clairement : `dist`, `visited`, `parent`

---

## ✅ Résumé express

| Besoin      | Outil                 |
| ----------- | --------------------- |
| Unicité     | `set`                 |
| Comptage    | `dict`, `defaultdict` |
| BFS         | `deque`               |
| Dijkstra    | `heapq`               |
| DP / Greedy | `list`, `min`, `max`  |
| Chemins     | `parent[]`            |

---

# Conclusion

Python fournit **tout ce qu’il faut** pour écrire des algorithmes propres,
lisibles et efficaces.

Bien choisir la structure de données est souvent
**plus important que l’algorithme lui-même**.

