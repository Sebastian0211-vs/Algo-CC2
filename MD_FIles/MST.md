# Minimum Spanning Tree (MST) – Prim & Kruskal appliqués au câblage fibre optique

## 1. Intuition générale

On reçoit une liste de maisons, chacune définie par ses coordonnées `(x, y)`.  
On veut relier **toutes les maisons entre elles** au coût total **minimal**, en utilisant comme coût la **distance euclidienne** entre deux maisons.

L’objectif est de construire un **arbre couvrant minimal** (Minimum Spanning Tree ou MST).

Le MST garantit :
- que toutes les maisons sont connectées ;
- que le total des longueurs de fibre utilisées est **minimal possible** ;
- qu’il n’y a **pas de cycles**, donc aucune fibre inutile.

---

## 2. Quand utiliser un MST ?

On utilise un Minimum Spanning Tree lorsque :
- on connecte des points avec un **coût de liaison** entre chaque paire ;
- on veut **minimiser le coût total** tout en gardant un réseau entièrement connecté ;
- on modélise des infrastructures : électricité, fibre, routes, pipelines, etc.

Dans ton labo, le MST est utilisé pour :

- `find_optimal_connections(houses)`

où chaque maison doit être reliée à toutes les autres au coût minimal.

---

## 3. Deux algorithmes principaux

### 3.1 Kruskal (tri des arêtes + Union-Find)
1. Générer **toutes les arêtes possibles** (i.e., toutes les paires de maisons).  
2. Les trier par poids croissant.  
3. Parcourir les arêtes triées :  
   - Si l’arête ne forme pas un cycle → on l’ajoute dans le MST.  
   - On utilise une structure Union-Find pour gérer les composantes.  
4. Quand on a ajouté `n-1` arêtes, on a terminé.

**Complexité :** O(E log E) = O(n² log n)

→ E = n(n-1)/2 car toutes les paires sont possibles.

### 3.2 Prim (démarre d’un nœud et étend le MST)
1. Choisir une maison de départ.  
2. Ajouter progressivement la maison la plus proche non encore connectée.  
3. Répéter jusqu’à ce que toutes les maisons appartiennent au réseau.

**Complexité naïve :** O(n²)  
→ parfait pour n ≤ quelques milliers.

Pour ce labo, **Prim est plus simple** et parfaitement suffisant.

---

## 4. Distance utilisée

On utilise la distance euclidienne :

```

distance = |x1 - x2| + |…

````

En MST, on utilise la vraie distance :

    sqrt((x1 - x2)^2 + (y1 - y2)^2)

Mais comme on veut uniquement **minimiser l’ordre**, la racine carrée peut être omise si nécessaire.  
Ici on la garde pour le réalisme.

---

## 5. Implémentation Python – Prim (simple et optimal pour ce labo)

```python
import heapq
from math import sqrt

def find_optimal_connections(houses):
    """
    Calcule la longueur totale minimale de fibre optique
    pour relier toutes les maisons via un MST.
    """
    n = len(houses)
    if n <= 1:
        return 0

    # Min-heap pour sélectionner l'arête la moins chère
    pq = [(0, 0)]  # (cost, index)
    in_mst = [False] * n
    total_cost = 0
    edges_used = 0

    # distance helper
    def dist(i, j):
        x1, y1 = houses[i]
        x2, y2 = houses[j]
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)

    while edges_used < n:
        cost, u = heapq.heappop(pq)
        if in_mst[u]:
            continue

        # On ajoute cette maison au MST
        in_mst[u] = True
        total_cost += cost
        edges_used += 1

        # On met à jour les distances vers toutes les autres maisons non encore dans le MST
        for v in range(n):
            if not in_mst[v]:
                heapq.heappush(pq, (dist(u, v), v))

    return int(total_cost)
````

---

## 6. Exemple du labo

```python
houses = [[0,0],[2,2],[3,10],[5,2],[7,0]]
optical_fiber_distance = find_optimal_connections(houses)
assert optical_fiber_distance == 20
```

---

## 7. Pourquoi l'algorithme fonctionne ?

* Le MST connecte toutes les maisons **sans cycles**, donc sans gaspillage.
* Prim ou Kruskal garantissent un coût total **minimal**.
* En connectant toujours la maison non encore reliée la plus proche, on évite toute arête excessive.
* Le résultat est optimal, unique en termes de coût.

---

# Conclusion

Le Minimum Spanning Tree est la solution optimale pour relier un ensemble de points au coût minimal.
Dans le labo, il fournit la longueur totale de fibre optique à commander.
L’implémentation par Prim est à la fois simple, propre, et efficace pour des tailles de données réalistes.

