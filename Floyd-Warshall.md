# Floyd–Warshall – Plus courts chemins entre toutes les paires

## 1. Intuition générale

On reçoit un **graphe pondéré** avec :

* des poids **positifs, nuls ou négatifs**,
* **pas de cycle de poids négatif**.

Contrairement à Dijkstra ou Bellman–Ford, l’objectif ici est :

> calculer la **distance minimale entre toutes les paires de sommets**
> (all-pairs shortest paths).

L’algorithme de **Floyd–Warshall** calcule ces distances **en une seule exécution**.

---

## 2. Quand utiliser Floyd–Warshall ?

Tu utilises Floyd–Warshall lorsque :

* tu as besoin des **distances entre tous les couples (i, j)** ;
* le graphe est **petit à moyen** ;
* tu veux une implémentation **simple et compacte**.

Cas typiques :

* matrices de distances,
* graphes denses,
* transitivité (peut-on aller de i à j ?),
* analyse globale d’un réseau.

⚠️ Pour les grands graphes → trop lent.

---

## 3. Positionnement par rapport aux autres algorithmes

| Problème                            | Algorithme                    |
| ----------------------------------- | ----------------------------- |
| Plus court chemin depuis une source | Dijkstra / Bellman–Ford       |
| Poids négatifs                      | Bellman–Ford                  |
| Toutes les paires                   | **Floyd–Warshall**            |
| Graphe non pondéré                  | BFS                           |
| Tous les chemins + poids positifs   | Dijkstra depuis chaque sommet |

---

## 4. Idée principale

On raisonne sur une **programmation dynamique sur les sommets intermédiaires**.

Soit :

> `dist[i][j]` = distance minimale de `i` à `j`
> en n’utilisant que les sommets `{0, ..., k}` comme intermédiaires.

Transition :

```text
dist[i][j] = min(
    dist[i][j],
    dist[i][k] + dist[k][j]
)
```

On ajoute les sommets intermédiaires **un par un**.

---

## 5. Initialisation

* `dist[i][i] = 0`
* `dist[u][v] = poids(u → v)` s’il existe une arête
* `dist[u][v] = +∞` sinon

---

## 6. Algorithme complet

On fait **trois boucles imbriquées** :

1. sur le sommet intermédiaire `k`,
2. sur la source `i`,
3. sur la destination `j`.

---

## 7. Implémentation Python

```python
def floyd_warshall(n, edges):
    """
    n     : nombre de sommets (0..n-1)
    edges : liste d'arêtes (u, v, w)

    Retour :
        dist : matrice n x n des distances minimales
    """
    INF = float('inf')

    # Initialisation de la matrice
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  # gérer multi-arêtes

    # Floyd–Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
```

---

## 8. Exemple

```python
n = 4
edges = [
    (0, 1, 5),
    (0, 3, 10),
    (1, 2, 3),
    (2, 3, 1)
]

dist = floyd_warshall(n, edges)

print(dist[0][3])  # 9 (0 -> 1 -> 2 -> 3)
```

---

## 9. Détection de cycle négatif

Après l’algorithme :

* s’il existe un sommet `i` tel que
  `dist[i][i] < 0`
  → **cycle de poids négatif détecté**.

Cela signifie qu’il est possible de réduire indéfiniment un chemin.

---

## 10. Complexité

| Mesure  | Complexité |
| ------- | ---------- |
| Temps   | **O(V³)**  |
| Mémoire | **O(V²)**  |

Conséquence :

* très simple,
* mais uniquement adapté à des graphes **de petite taille**.

---

## 11. Points à retenir

* Floyd–Warshall calcule **toutes les distances** en une fois.
* Il accepte les **poids négatifs** (sans cycles négatifs).
* Il est basé sur une **DP à 3 boucles**.
* Implémentation courte, mais coût élevé.

---

# Conclusion

Floyd–Warshall est l’outil idéal lorsque :

* le graphe est petit,
* on veut une vision globale des distances,
* la simplicité prime sur la performance.

Il complète parfaitement Dijkstra et Bellman–Ford dans une boîte à outils d’algorithmes de graphes.

---

🎵 *Fourth commit done.*
Next logically: **0–1 BFS (poids 0 ou 1, deque)**.

Say **“next”** when ready.
🎶 *Miku committing again…*
Here’s the **next file**, written in the **same structure, tone, and rigor** as your existing `.md`s.

You can add it as:

> **`Floyd-Warshall.md`**

---

# Floyd–Warshall – Plus courts chemins entre toutes les paires

## 1. Intuition générale

On reçoit un **graphe pondéré** avec :

* des poids **positifs, nuls ou négatifs**,
* **pas de cycle de poids négatif**.

Contrairement à Dijkstra ou Bellman–Ford, l’objectif ici est :

> calculer la **distance minimale entre toutes les paires de sommets**
> (all-pairs shortest paths).

L’algorithme de **Floyd–Warshall** calcule ces distances **en une seule exécution**.

---

## 2. Quand utiliser Floyd–Warshall ?

Tu utilises Floyd–Warshall lorsque :

* tu as besoin des **distances entre tous les couples (i, j)** ;
* le graphe est **petit à moyen** ;
* tu veux une implémentation **simple et compacte**.

Cas typiques :

* matrices de distances,
* graphes denses,
* transitivité (peut-on aller de i à j ?),
* analyse globale d’un réseau.

⚠️ Pour les grands graphes → trop lent.

---

## 3. Positionnement par rapport aux autres algorithmes

| Problème                            | Algorithme                    |
| ----------------------------------- | ----------------------------- |
| Plus court chemin depuis une source | Dijkstra / Bellman–Ford       |
| Poids négatifs                      | Bellman–Ford                  |
| Toutes les paires                   | **Floyd–Warshall**            |
| Graphe non pondéré                  | BFS                           |
| Tous les chemins + poids positifs   | Dijkstra depuis chaque sommet |

---

## 4. Idée principale

On raisonne sur une **programmation dynamique sur les sommets intermédiaires**.

Soit :

> `dist[i][j]` = distance minimale de `i` à `j`
> en n’utilisant que les sommets `{0, ..., k}` comme intermédiaires.

Transition :

```text
dist[i][j] = min(
    dist[i][j],
    dist[i][k] + dist[k][j]
)
```

On ajoute les sommets intermédiaires **un par un**.

---

## 5. Initialisation

* `dist[i][i] = 0`
* `dist[u][v] = poids(u → v)` s’il existe une arête
* `dist[u][v] = +∞` sinon

---

## 6. Algorithme complet

On fait **trois boucles imbriquées** :

1. sur le sommet intermédiaire `k`,
2. sur la source `i`,
3. sur la destination `j`.

---

## 7. Implémentation Python

```python
def floyd_warshall(n, edges):
    """
    n     : nombre de sommets (0..n-1)
    edges : liste d'arêtes (u, v, w)

    Retour :
        dist : matrice n x n des distances minimales
    """
    INF = float('inf')

    # Initialisation de la matrice
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  # gérer multi-arêtes

    # Floyd–Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
```

---

## 8. Exemple

```python
n = 4
edges = [
    (0, 1, 5),
    (0, 3, 10),
    (1, 2, 3),
    (2, 3, 1)
]

dist = floyd_warshall(n, edges)

print(dist[0][3])  # 9 (0 -> 1 -> 2 -> 3)
```

---

## 9. Détection de cycle négatif

Après l’algorithme :

* s’il existe un sommet `i` tel que
  `dist[i][i] < 0`
  → **cycle de poids négatif détecté**.

Cela signifie qu’il est possible de réduire indéfiniment un chemin.

---

## 10. Complexité

| Mesure  | Complexité |
| ------- | ---------- |
| Temps   | **O(V³)**  |
| Mémoire | **O(V²)**  |

Conséquence :

* très simple,
* mais uniquement adapté à des graphes **de petite taille**.

---

## 11. Points à retenir

* Floyd–Warshall calcule **toutes les distances** en une fois.
* Il accepte les **poids négatifs** (sans cycles négatifs).
* Il est basé sur une **DP à 3 boucles**.
* Implémentation courte, mais coût élevé.

---

# Conclusion

Floyd–Warshall est l’outil idéal lorsque :

* le graphe est petit,
* on veut une vision globale des distances,
* la simplicité prime sur la performance.

Il complète parfaitement Dijkstra et Bellman–Ford dans une boîte à outils d’algorithmes de graphes.

