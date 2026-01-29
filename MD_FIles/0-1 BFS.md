> **`0-1 BFS.md`**

---

# 0–1 BFS – Plus courts chemins avec poids 0 ou 1

## 1. Intuition générale

On reçoit un **graphe pondéré** où chaque arête a un poids **soit 0, soit 1**.

Objectif :

> calculer les **plus courts chemins** depuis une source.

Problème :

* BFS classique ne marche que si **tous les poids sont identiques**,
* Dijkstra marche, mais est **sur-dimensionné** ici.

Solution :

> **0–1 BFS**
> une version optimisée de BFS utilisant une **deque** au lieu d’un tas.

---

## 2. Quand utiliser 0–1 BFS ?

Tu utilises 0–1 BFS lorsque :

* les poids des arêtes sont **uniquement 0 ou 1** ;
* tu veux un algorithme plus rapide que Dijkstra ;
* le graphe est relativement grand.

Cas typiques :

* grilles avec murs gratuits / payants,
* transitions “gratuites” vs “coûteuses”,
* problèmes de changement d’état minimal.

---

## 3. Positionnement par rapport aux autres algorithmes

| Poids des arêtes     | Algorithme   |
| -------------------- | ------------ |
| Tous égaux           | BFS          |
| Positifs quelconques | Dijkstra     |
| **0 ou 1**           | **0–1 BFS**  |
| Négatifs             | Bellman–Ford |

0–1 BFS est **strictement plus efficace** que Dijkstra dans ce cas précis.

---

## 4. Idée principale

On remplace la file FIFO de BFS par une **deque** :

* si on emprunte une arête de **poids 0** :

  * on ajoute le voisin **en tête** de la deque ;
* si on emprunte une arête de **poids 1** :

  * on ajoute le voisin **en fin** de la deque.

Cela garantit que :

* les sommets sont traités **dans l’ordre croissant de distance**,
* sans utiliser de file de priorité.

---

## 5. Algorithme détaillé

1. Initialiser toutes les distances à `+∞`.
2. Mettre la source dans la deque avec distance 0.
3. Tant que la deque n’est pas vide :

   * extraire un sommet `u`,
   * pour chaque arête `(u → v, w)` :

     * si `dist[u] + w < dist[v]` :

       * mettre à jour `dist[v]`,
       * ajouter `v` :

         * **à gauche** si `w == 0`,
         * **à droite** si `w == 1`.

---

## 6. Implémentation Python

```python
from collections import deque

def zero_one_bfs(n, edges, source):
    """
    n      : nombre de sommets (0..n-1)
    edges  : liste d'arêtes (u, v, w) avec w ∈ {0,1}
    source : sommet source

    Retour :
        dist : distances minimales depuis source
    """
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    INF = float('inf')
    dist = [INF] * n
    dist[source] = 0

    dq = deque([source])

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

## 7. Exemple

```python
n = 5
edges = [
    (0, 1, 0),
    (0, 2, 1),
    (1, 2, 0),
    (1, 3, 1),
    (2, 3, 0),
    (3, 4, 1)
]

dist = zero_one_bfs(n, edges, 0)
print(dist)  # [0, 0, 0, 0, 1]
```

---

## 8. Complexité

| Mesure  | Complexité   |
| ------- | ------------ |
| Temps   | **O(V + E)** |
| Mémoire | **O(V + E)** |

Même complexité qu’un BFS classique,
mais applicable à des graphes pondérés très spécifiques.

---

## 9. Points à retenir

* 0–1 BFS est un **cas particulier optimisé** de Dijkstra.
* Il utilise une **deque**, pas un tas.
* Il est optimal uniquement si les poids sont **0 ou 1**.
* Très fréquent dans les problèmes de grilles et de transitions d’état.

---

# Conclusion

Dès que tu vois :

* “coût gratuit” vs “coût 1”,
* ou “changer d’état coûte 1”,

pense immédiatement à **0–1 BFS**.

C’est un algorithme simple, rapide, et extrêmement élégant.

