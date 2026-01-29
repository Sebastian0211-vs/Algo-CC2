# Shortest Path – Graphe non pondéré (BFS)

## 1. Intuition générale

On travaille avec un **graphe non pondéré**, ou équivalent :

* toutes les arêtes ont le **même coût** (souvent 1),
* chaque déplacement coûte exactement une étape.

Objectif :

> trouver le **plus court chemin** entre un sommet source et les autres sommets.

Dans ce contexte, **BFS donne directement les plus courts chemins**.

---

## 2. Pourquoi BFS fonctionne ?

Propriété clé :

> BFS explore le graphe **niveau par niveau**.

* niveau 0 : sommet source
* niveau 1 : sommets à distance 1
* niveau 2 : sommets à distance 2
* etc.

La **première fois** qu’un sommet est atteint par BFS,
le chemin utilisé est **forcément minimal**.

---

## 3. Quand utiliser BFS pour les plus courts chemins ?

Tu utilises BFS lorsque :

* le graphe est **non pondéré** ;
* ou tous les poids valent **1** ;
* ou tu cherches le **nombre minimal d’étapes**.

Cas typiques :

* labyrinthes,
* grilles,
* graphes sociaux (distance minimale),
* jeux de plateau simples.

⚠️ Si les poids sont différents → **Dijkstra ou 0–1 BFS**.

---

## 4. BFS avec distances

On maintient un tableau :

* `dist[v]` = distance minimale depuis la source

Initialisation :

* `dist[source] = 0`
* autres = `+∞` (ou `-1`)

---

## 5. Implémentation Python

```python
from collections import deque

def bfs_shortest_path(n, edges, source):
    """
    n      : nombre de sommets (0..n-1)
    edges  : liste d'arêtes non orientées [u, v]
    source : sommet source

    Retour :
        dist : distances minimales depuis source
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1] * n
    dist[source] = 0

    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist
```

---

## 6. Comparaison avec Dijkstra

| Situation          | Algorithme   |
| ------------------ | ------------ |
| Graphe non pondéré | **BFS**      |
| Poids = 0 ou 1     | 0–1 BFS      |
| Poids positifs     | Dijkstra     |
| Poids négatifs     | Bellman–Ford |

Utiliser Dijkstra sur un graphe non pondéré est **correct**, mais **inutilement complexe**.

---

## 7. Exemple

```python
n = 6
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5)
]

dist = bfs_shortest_path(n, edges, 0)
print(dist)  # [0, 1, 1, 2, 3, 4]
```

---

## 8. Complexité

| Mesure  | Complexité   |
| ------- | ------------ |
| Temps   | **O(V + E)** |
| Mémoire | **O(V)**     |

Optimal pour les graphes non pondérés.

---

## 9. Points à retenir

* BFS donne les plus courts chemins **si tous les poids sont égaux**.
* La distance correspond au **nombre minimal d’arêtes**.
* Plus simple et plus rapide que Dijkstra dans ce cas.

---

# Conclusion

Dès que tu vois :

* “graphe non pondéré”,
* “nombre minimal d’étapes”,

**BFS est l’algorithme optimal**.

