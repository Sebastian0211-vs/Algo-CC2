
# Diameter of a Tree – Double BFS/DFS (Max Latency)

## 1. Intuition générale

On te donne un réseau sous forme d’**arbre** :
- chaque nœud est une machine/maison,
- chaque arête est un lien,
- il n’y a **qu’un seul chemin possible** entre deux nœuds (pas de cycles, pas de multi-chemins).

On cherche la **latence maximale** du réseau, c’est-à-dire :

> la distance (en nombre d’arêtes) entre les deux nœuds les plus éloignés.

C’est exactement ce qu’on appelle le **diamètre d’un arbre**.

Dans le labo, ce problème correspond à :

- `max_latency(network)`

où `network` est une liste d’arêtes non orientées (par exemple `[[1,2], [1,3], ...]`).

---

## 2. Quand utiliser cet algorithme ?

Tu utilises cet algorithme quand :

- le graphe est un **arbre** (connecté, sans cycles) ;
- tu dois connaître la **plus longue distance minimale** entre deux nœuds ;
- tu veux mesurer la “taille” ou “profondeur maximale” du réseau.

Exemples d’applications :
- latence maximale dans un réseau (ton labo),
- profondeur maximale d’une hiérarchie,
- longueur maximale d’un chemin simple dans un arbre.

---

## 3. Idée clé : double BFS/DFS

Propriété fondamentale des arbres :

> Si tu choisis un nœud quelconque `s` et tu fais un BFS/DFS,  
> le nœud le plus éloigné trouvé, appelons-le `A`,  
> est **forcément une extrémité du diamètre**.

Ensuite :

1. BFS/DFS depuis un nœud quelconque `s` → trouve le nœud le plus éloigné `A`.
2. BFS/DFS depuis `A` → trouve le nœud le plus éloigné `B` et la distance `dist(A, B)`.
3. Cette distance `dist(A, B)` est le **diamètre de l’arbre**, donc la **latence maximale**.

Pourquoi ça marche ?  
Dans un arbre, tout chemin simple est unique. Le BFS trouve un nœud extrémal du chemin le plus long, et un second BFS depuis cette extrémité donne la longueur exacte de ce chemin.

---

## 4. Complexité

- Construction du graphe : O(n)
- Deux BFS/DFS : O(n) chacun
- Total : **O(n)** en temps, **O(n)** en mémoire

---

## 5. Représentation du réseau

On reçoit :

```python
network = [[1, 2], [1, 3], [1, 4], [4, 5], ...]
````

On construit une **liste d’adjacence** pour un graphe non orienté :

```python
graph[u].append(v)
graph[v].append(u)
```

Les nœuds peuvent être 1..N, on les récupère à partir des arêtes.

---

## 6. Implémentation Python (double BFS)

```python
from collections import deque
from typing import List

def max_latency(network: List[List[int]]) -> int:
    """
    Calcule la latence maximale (diamètre) d'un réseau en forme d'arbre.
    network est une liste d'arêtes non orientées, par exemple :
      [[1,2], [1,3], [1,4], ...]
    """
    if not network:
        return 0  # un seul nœud ou réseau vide -> pas de distance

    # ----------------------------
    # 1. Construire le graphe
    # ----------------------------
    nodes = set()
    for u, v in network:
        nodes.add(u)
        nodes.add(v)

    # On suppose que les nœuds sont des entiers
    graph = {node: [] for node in nodes}
    for u, v in network:
        graph[u].append(v)
        graph[v].append(u)

    # ----------------------------
    # BFS qui renvoie :
    # - le nœud le plus éloigné
    # - sa distance maximale
    # ----------------------------
    def bfs(start):
        queue = deque([start])
        dist = {start: 0}

        farthest_node = start
        max_dist = 0

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    queue.append(v)

                    # mise à jour du plus éloigné
                    if dist[v] > max_dist:
                        max_dist = dist[v]
                        farthest_node = v

        return farthest_node, max_dist

    # ----------------------------
    # 2. Premier BFS depuis un nœud arbitraire
    # ----------------------------
    arbitrary_start = next(iter(nodes))   # on prend n'importe quel nœud
    A, _ = bfs(arbitrary_start)

    # ----------------------------
    # 3. Deuxième BFS depuis A
    # ----------------------------
    B, diameter = bfs(A)

    # La distance entre A et B = diamètre = latence maximale
    return diameter
```

---

## 7. Tests du labo

```python
# Exemple 1
# 3 — 1 — 2
# |
# 5 — 4 — 6
# |
# 7
network = [[1, 2], [1, 3], [1, 4], [4, 5], [4, 6], [6, 7]]
assert max_latency(network) == 4

# Exemple 2
# 1 — 2 — 3 — 4
# |     |
# 7     5 — 6
# |
# 8
# |
# 9
network = [[1, 2], [2, 3], [3, 4], [3, 5], [5, 6], [2, 7], [7, 8], [8, 9]]
assert max_latency(network) == 6
```

---

## 8. Résumé à retenir

* On cherche la **plus longue distance** dans un arbre → **diamètre**.
* Technique standard : **double BFS/DFS**.
* Complexité linéaire, très efficace.

---

# Conclusion

L’algorithme de diamètre d’un arbre par double BFS est un pattern classique à connaître :
dès que tu as un arbre et que tu cherches le chemin le plus long, pense automatiquement à cette technique.

