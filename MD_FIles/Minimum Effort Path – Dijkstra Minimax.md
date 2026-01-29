# Minimum Effort Path – Dijkstra Minimax (Chemin minimisant le saut maximal)

## 1. Intuition générale

On reçoit une carte d’altitudes sous forme d'une grille `M × N`.  
Pour aller du point `(0, 0)` au point `(M-1, N-1)`, le *coût* d’un déplacement entre deux cellules adjacentes est :

    effort = |hauteur_voisine - hauteur_actuelle|

Mais l’objectif **ne consiste PAS à minimiser la somme des efforts**.  
L’objectif est de minimiser :

> **le plus grand effort que l’on doit fournir sur un chemin donné**.

Autrement dit, parmi tous les chemins possibles, on veut celui dont **le pire saut vertical est le plus petit**.

C’est un problème classique appelé **Minimax Path**.

---

## 2. Quand utiliser cet algorithme ?

On utilise un *Dijkstra minimax* lorsque :

- le coût d’un chemin est défini comme la **valeur maximale d’une arête** sur le trajet ;
- on doit minimiser une contrainte de type :  
  « Trouver un chemin sûr où **le pire obstacle est le plus faible possible** » ;
- on traite des cartes d’altitude, niveaux de difficulté, risques, gradients, etc.

Dans ce labo, cet algorithme s’applique au problème :

- `minimum_effort_path(heights)`

---

## 3. Idée de la solution

La grille peut être vue comme un graphe où chaque cellule est un nœud et chaque déplacement est une arête pondérée par :

```

abs(heights[nr][nc] - heights[r][c])

```

On utilise une variante de **Dijkstra**, mais au lieu de :

- accumuler la somme des coûts,

on utilise :

- un score pour chaque cellule = **le maximum des efforts rencontrés depuis le départ jusqu'à cette cellule**.

Lorsque l’on explore un voisin, on met à jour :

```

new_effort = max(current_effort, effort_edge)

````

On choisit toujours la prochaine cellule ayant le **plus petit effort maximal actuel**.

Le premier moment où l’on atteint `(M-1, N-1)`, on est garanti d’avoir trouvé la solution optimale.

---

## 4. Complexité

- Temps : **O(M × N log(M × N))**  
  (Dijkstra avec un tas)

- Mémoire : **O(M × N)**  
  (tableau des efforts minimaux)

---

## 5. Implémentation Python (Dijkstra minimax)

```python
import heapq

def minimum_effort_path(heights):
    M, N = len(heights), len(heights[0])

    # effort[r][c] = meilleur effort maximal connu pour atteindre (r, c)
    effort = [[float('inf')] * N for _ in range(M)]
    effort[0][0] = 0

    # Min-heap : (effort_actuel, r, c)
    pq = [(0, 0, 0)]

    # Directions : haut, bas, gauche, droite
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while pq:
        cur_eff, r, c = heapq.heappop(pq)

        # Si on atteint la fin, on peut s'arrêter
        if r == M - 1 and c == N - 1:
            return cur_eff

        # Si une meilleure solution existe déjà, ignorer cette entrée
        if cur_eff > effort[r][c]:
            continue

        # Explore les voisins
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N:
                # Effort pour franchir cette arête
                edge_cost = abs(heights[nr][nc] - heights[r][c])
                # Le coût d'un chemin est le max des arêtes
                new_eff = max(cur_eff, edge_cost)

                # On met à jour si on peut améliorer
                if new_eff < effort[nr][nc]:
                    effort[nr][nc] = new_eff
                    heapq.heappush(pq, (new_eff, nr, nc))

    # Normalement jamais atteint
    return -1
````

---

## 6. Tests du labo

```python
heights = [
    [1,2,2],
    [3,8,2],
    [5,3,5]
]
res = minimum_effort_path(heights)
assert res == 2
```

---

## 7. Pourquoi cette solution fonctionne ?

La propriété clé de Dijkstra s’adapte ici :

* On explore toujours la cellule dont **le meilleur effort maximal connu est minimal**.
* Lorsque `(M-1, N-1)` est extraite du tas, on sait qu’aucun autre chemin ne peut l’atteindre avec un effort maximal plus petit.
* Cela marche car l’opération `max(cur_eff, edge_cost)` respecte une structure monotone permettant une variante de Dijkstra.

---

# Conclusion

Le problème “Minimum Effort Path” est un exemple parfait d’une adaptation de Dijkstra, où l’on minimise le **pire coût** plutôt que la somme.
C’est un outil fondamental pour toute analyse de chemins sous contrainte de risque, pente ou difficulté maximale.
