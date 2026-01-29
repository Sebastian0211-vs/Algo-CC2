# Goose Game – Minimum de sauts pour atteindre la fin (Greedy / Jump Game II)

## 1. Intuition générale

On reçoit un tableau `board` où chaque case `board[i]` contient :

> le **nombre maximal de cases** que l’on peut sauter depuis la position `i`.

On commence à l’index `0` et on veut atteindre (ou dépasser) l’index `len(board) - 1`  
avec **le plus petit nombre de tours (sauts)** possible.

Exemples (du labo) :

```python
board = [2,3,1,1,4]
res = goose_game(board)
assert res == 2   # 0 -> 1 -> 4

board = [2,3,0,1,4]
res = goose_game(board)
assert res == 2   # 0 -> 1 -> 4
````

Ce problème est une version directe de **Jump Game II**.

---

## 2. Quand utiliser cet algorithme ?

Tu utilises cet algorithme lorsque :

* tu dois atteindre la **fin d’un tableau** en un nombre minimal de “sauts” ;
* chaque position te donne la **portée maximale** à partir de cette position ;
* tu n’as pas de poids négatifs ou de coûts variés, uniquement un **compteur de sauts**.

Typiquement :

* jeux de plateau avec sauts,
* systèmes de téléportation / portées,
* planification de sauts dans un plan unidimensionnel.

Dans le labo, il sert pour :

* `goose_game(board)`

---

## 3. Approche naïve (à éviter)

On pourrait imaginer :

* un **BFS** sur les indices (chaque état = position actuelle),
* ou même un **DP** qui essaie tous les chemins possibles.

Problème : ces approches deviennent rapidement **trop lentes** (O(n²) voire pire)
pour de grands tableaux.

Heureusement, le problème a une structure spéciale qui permet un **greedy en O(n)**.

---

## 4. Idée de l’algorithme Greedy (O(n))

On parcourt le tableau **une seule fois** en maintenant trois variables :

* `steps` : nombre de sauts effectués jusqu’à maintenant,
* `current_end` : la **fin de la portée actuelle** (jusqu’où on peut aller avec `steps` sauts),
* `farthest` : la **position la plus lointaine** atteignable depuis toutes les cases déjà traversées dans la portée actuelle.

Logique :

1. On initialise :

   * `steps = 0`
   * `current_end = 0` (on est au début)
   * `farthest = 0`
2. On parcourt les indices `i` de `0` à `len(board) - 2` (on n’a pas besoin de traiter la dernière case) :

   * à chaque `i`, on met à jour :

     ```python
     farthest = max(farthest, i + board[i])
     ```
   * si on atteint `current_end` (i == current_end) :

     * cela signifie que tous les “points de départ” possible avec `steps` sauts ont été considérés ;
     * pour aller plus loin, on doit faire **un saut de plus** → `steps += 1`
     * on met à jour `current_end = farthest`
3. À la fin, `steps` est le **nombre minimal de sauts**.

Pourquoi ça marche ?

* Chaque segment `[start, current_end]` représente **les positions atteignables avec `steps` sauts**.
* On choisit toujours de “prolonger” ce segment avec la position qui donne la portée maximale (`farthest`) → stratégie gloutonne optimale.

---

## 5. Complexité

* **Temps : O(n)**
  Un seul passage sur le tableau.

* **Mémoire : O(1)**
  Trois entiers, aucune structure lourde.

---

## 6. Implémentation Python

```python
from typing import List

def goose_game(board: List[int]) -> int:
    """
    Retourne le nombre minimum de tours (sauts) nécessaires
    pour atteindre la dernière case du plateau.
    
    board[i] = portée maximale possible depuis la case i.
    """
    n = len(board)
    if n <= 1:
        return 0  # déjà sur la dernière case

    steps = 0          # nombre de sauts
    current_end = 0    # fin de la portée actuelle
    farthest = 0       # position la plus loin atteignable

    # On parcourt jusqu'à l'avant-dernière case
    for i in range(n - 1):
        # Met à jour la position maximale atteignable
        farthest = max(farthest, i + board[i])

        # Si on atteint la fin de la portée actuelle,
        # il faut faire un saut supplémentaire
        if i == current_end:
            steps += 1
            current_end = farthest

            # Optionnel : si on peut déjà atteindre la fin, on peut sortir
            if current_end >= n - 1:
                break

    return steps
```

---

## 7. Tests (labo)

```python
board = [2, 3, 1, 1, 4]
res = goose_game(board)
assert res == 2  # 0 -> 1 -> 4

board = [2, 3, 0, 1, 4]
res = goose_game(board)
assert res == 2  # 0 -> 1 -> 4
```

---

## 8. Points à retenir

* C’est un problème **classique** de type “Jump Game II”.
* La solution optimale utilise un **greedy en O(n)** basé sur :

  * `current_end` = fin de la zone couverte avec le nombre de sauts actuel,
  * `farthest` = meilleure portée possible depuis cette zone.
* On incrémente `steps` uniquement quand on a épuisé la portée actuelle et qu’on doit “sauter” pour prolonger.

---

# Conclusion

Le Goose Game est une excellente illustration de l’idée :

> “On peut parfois remplacer un BFS ou un DP coûteux par un greedy linéaire
> si on exploite bien la structure du problème.”

Cet algorithme est un incontournable à connaître par cœur.

