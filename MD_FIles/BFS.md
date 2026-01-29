# **BFS — Parcours en largeur (Breadth-First Search)**

L’algorithme **BFS** (Breadth-First Search) est un parcours fondamental de graphes permettant d’explorer un réseau **couche par couche** (niveau par niveau).
Il est particulièrement utile pour trouver des **distances minimales en nombre d’arêtes** dans les graphes **non pondérés**.

---

# 1. **Ce que résout BFS**

Étant donné un graphe (orienté ou non), BFS permet :

* de déterminer si un nœud est atteignable depuis une source,
* de calculer la **distance minimale en nombre de sauts** entre deux nœuds,
* de reconstruire le chemin le plus court (en arêtes),
* de tester la connexité du graphe.

### BFS trouve **le plus court chemin quand toutes les arêtes ont le même poids** (ou un poids constant, typiquement 1).

Si le graphe possède des poids différents, BFS n’est **pas correct** → il faut utiliser **Dijkstra**.

---

# 2. **Intuition du fonctionnement**

BFS utilise une **file FIFO** pour explorer :

1. On commence par le nœud source.
2. On visite tous ses voisins directs (niveau 1).
3. Puis tous les voisins des voisins (niveau 2).
4. On continue jusqu’à avoir exploré tout ce qui est atteignable.

L’idée :

> On traite toujours en premier les nœuds les plus proches de la source.

---

# 3. **Quand utiliser BFS ?**

### ✔ Utiliser BFS si :

* les arêtes n’ont pas de poids,
* les arêtes ont toutes un poids identique,
* on cherche un **plus court chemin en nombre de sauts**,
* on teste la **connexité** ou la **distance minimale** dans un réseau simple.

### ✘ Ne pas utiliser BFS si :

* les arêtes ont des poids différents → utiliser **Dijkstra**,
* il y a des poids négatifs → utiliser **Bellman-Ford**.

---

# 4. **Représentation standard du graphe**

Comme pour Dijkstra, BFS utilise typiquement une **liste d'adjacence** :

```python
adj[u] = [v1, v2, v3]
```

---

# 5. **Implémentation Python simple et commentée**

Voici une version pédagogique, permettant de calculer les distances (en nombre d’arêtes) depuis une source.

```python
from collections import deque

def bfs(n, edges, start):
    """
    n      : nombre de noeuds (1..n)
    edges  : liste [u, v] pour arêtes dirigées u -> v
    start  : noeud source

    Retour :
        dist[i] = distance minimale (en nombre d'arêtes) entre start et i
                   ou inf si inatteignable.
    """

    # Construction de la liste d'adjacence
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    # Distance initiale : infini
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0

    # File FIFO
    queue = deque([start])

    while queue:
        u = queue.popleft()

        # Exploration des voisins
        for v in adj[u]:
            # Si v est encore non visité
            if dist[v] == INF:
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist
```

---

# 6. **Exemple d’utilisation**

```python
n = 6
edges = [
    [1, 2],
    [1, 3],
    [2, 4],
    [2, 5],
    [3, 6]
]

distances = bfs(n, edges, 1)

print(distances)  # dist[1..6]
```

Sortie :

```
[inf, 0, 1, 1, 2, 2, 2]
```

Interprétation :

* Distance de 1 → 1 : 0
* Distance de 1 → 2 : 1
* Distance de 1 → 3 : 1
* Distance de 1 → 4 : 2
* Distance de 1 → 5 : 2
* Distance de 1 → 6 : 2

---

# 7. **Complexité**

| Opération | Complexité   |
| --------- | ------------ |
| Temps     | **O(V + E)** |
| Mémoire   | **O(V)**     |

BFS est extrêmement performant et souvent utilisé comme sous-routine dans d’autres algorithmes.

---

# 8. **Applications pratiques**

BFS est utilisé pour :

* trouver des distances minimales dans un réseau non pondéré,
* détecter des cycles,
* vérifier si un graphe est biparti,
* explorer des états possibles (IA, jeux),
* résoudre des problèmes de grille (labyrinthes, shortest path),
* déterminer les composantes connexes.

---

# 9. **Résumé**

* BFS explore un graphe **niveau par niveau**, grâce à une file FIFO.
* Il retourne les **plus courts chemins** lorsque les arêtes ont toutes le même coût.
* C’est l’un des algorithmes les plus simples et puissants en informatique.
* Pour les graphes pondérés → utiliser **Dijkstra** ou **Bellman-Ford** selon le cas.

