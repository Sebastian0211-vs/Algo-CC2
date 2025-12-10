# Avalanche Chain Reaction – Portée de détonation & composantes atteignables

## 1. Intuition générale

On reçoit une liste de bombes, chacune définie par :

    [x_i, y_i, r_i]

où `(x_i, y_i)` est sa position et `r_i` son rayon d’action.

Quand une bombe explose :
- elle fait exploser toutes les bombes situées **dans son rayon** ;
- chaque bombe déclenchée agit à son tour ;
- l’objectif est de trouver **la première bombe à déclencher** pour provoquer **le plus grand nombre total d’explosions**.

Ce problème revient à construire un **graphe dirigé** :

- Il existe une arête `i → j` si la bombe `j` se trouve dans le rayon de `i`.

Ensuite, pour chaque bombe, on calcule combien de bombes on peut atteindre via un parcours **DFS/BFS**.  
Le maximum de ces nombres est la réponse finale.

---

## 2. Quand utiliser cet algorithme ?

Ce schéma s’applique dès que :
- tu dois modéliser des interactions de proximité (rayons, zones d’influence, impacts) ;
- chaque élément déclenche d’autres éléments de façon **orientée** ;
- tu dois comptabiliser la **taille d’une propagation** dans un graphe dirigé.

Dans ton labo, cela correspond à :

- `find_first_detonation(bombs)`

---

## 3. Idée principale

1. Construire un graphe dirigé `G` où :
   - chaque nœud représente une bombe,
   - une arête `i → j` signifie “si j’explose quand i explose”.

2. Pour chaque bombe `i` :
   - exécuter un DFS/BFS pour compter combien de bombes explosent au total.

3. Retourner le maximum obtenu.

La relation de portée se teste via :

```

distance(i, j) = sqrt((x_i - x_j)^2 + (y_i - y_j)^2)
j est atteint si distance(i, j) <= r_i

````

(La racine carrée peut être évitée pour optimiser.)

---

## 4. Complexité

- Construction du graphe :  
  O(n²) tests de portée.

- DFS/BFS pour chaque bombe :  
  O(n + arcs) ≈ O(n²) au total.

Complexité globale :  
**O(n²)**, acceptable pour n ≤ quelques milliers.

---

## 5. Implémentation Python (DFS)

```python
def find_first_detonation(bombs):
    """
    Retourne le nombre maximal de bombes pouvant exploser
    après avoir déclenché une seule bombe.
    """
    n = len(bombs)

    # ---------------------------------------------------
    # 1. Construire le graphe dirigé (adjacency list)
    # ---------------------------------------------------
    graph = [[] for _ in range(n)]

    for i in range(n):
        x1, y1, r1 = bombs[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2, _ = bombs[j]

            # Test de portée sans la racine : d^2 <= r^2
            if (x1 - x2)**2 + (y1 - y2)**2 <= r1 * r1:
                graph[i].append(j)

    # ---------------------------------------------------
    # 2. DFS pour compter la cascade à partir d'une bombe
    # ---------------------------------------------------
    def count_from(start):
        stack = [start]
        visited = set([start])

        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

        return len(visited)

    # ---------------------------------------------------
    # 3. Tester chaque bombe en point de départ
    # ---------------------------------------------------
    best = 0
    for i in range(n):
        best = max(best, count_from(i))

    return best
````

---

## 6. Tests du labo

```python
bombs = [[2,1,3],[6,1,4]]
assert find_first_detonation(bombs) == 2

bombs = [[1,1,5],[10,10,5]]
assert find_first_detonation(bombs) == 1
```

---

## 7. Pourquoi cette approche fonctionne ?

* L’explosion suit une logique de **propagation dirigée**, donc elle se modélise naturellement en graphe orienté.
* Une bombe peut en activer plusieurs, qui activent à leur tour d’autres bombes → chaîne de causalité = **parcours complet depuis un nœud**.
* En prenant le maximum sur toutes les bombes, on trouve le **meilleur point de départ**.

L’algorithme est optimal pour ce modèle : chaque relation doit de toute façon être testée une fois.

---

# Conclusion

Le problème de l’avalanche est un excellent exemple de **reachability dans un graphe dirigé**.
La construction O(n²) est inévitable, mais le DFS/BFS derrière est simple et garantit la solution optimale.

