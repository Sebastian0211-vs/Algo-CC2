
# Tic-Tac-Toe – Explorer tout l’espace de jeu (backtracking sur arbre de jeu)

## 1. Intuition générale

On reçoit :
- un plateau de morpion `3×3` représenté par un tableau de chaînes,
- un `next_player` qui vaut `'x'` ou `'o'`.

Certaines cases peuvent être déjà jouées (`'x'` ou `'o'`), d’autres vides (`''`).

Objectif :

> Explorer **toutes les parties possibles** à partir de ce plateau,
> en supposant que les deux joueurs peuvent jouer n’importe quel coup valide,
> et compter **combien de fins de partie** sont des victoires pour `x` et pour `o`.

On renvoie par exemple un dictionnaire :

```python
wins = get_proba(board, next_player)
print(wins['o'], wins['x'])
````

Dans les exemples du labo, les valeurs sont normalisées pour faire des probabilités,
mais le cœur de l’algorithme est de **compter** le nombre de fins gagnantes.

---

## 2. Quand utiliser cet algorithme ?

On utilise ce type d’exploration d’arbre de jeu lorsque :

* on veut **examiner tous les scénarios possibles** d’un jeu discret (morpion, puissance 4, etc.) ;
* le nombre de coups possibles est faible, ce qui rend l’exploration exhaustive réaliste ;
* on ne cherche pas forcément le “coup optimal”, mais à **quantifier** les issues
  (nombre de victoires, défaites, nuls).

Dans ce labo, il s’applique à :

* `get_proba(arr, next_player)`

---

## 3. Idée principale : backtracking sur l’arbre de jeu

On voit chaque configuration du plateau comme un **nœud** dans un arbre de jeu.

Pour une position donnée :

1. On vérifie si quelqu’un a **déjà gagné** ou si le plateau est **plein** :

   * si oui → position terminale :

     * si `'x'` gagne → `wins['x'] += 1`
     * si `'o'` gagne → `wins['o'] += 1`
     * sinon (nul) → ni l’un ni l’autre n’est incrémenté (on peut aussi compter les nuls séparément).

2. Sinon, on génère **tous les coups légaux** :

   * pour chaque case vide :

     * on joue `next_player` dans cette case,
     * on appelle récursivement la fonction avec l’autre joueur,
     * on annule le coup (backtrack).

On additionne les résultats de tous les sous-arbres.

---

## 4. Complexité

* Dans un morpion classique 3×3, le nombre de parties possibles est limité (≤ ~255k positions de fin),
  donc l’exploration exhaustive est tout à fait faisable.
* Complexité en pratique : **exponentielle** dans le nombre de cases vides, mais très faible en absolu pour 3×3.

---

## 5. Fonctions utilitaires

On a besoin de fonctions auxiliaires :

1. `check_winner(board)`
   → renvoie `'x'`, `'o'` ou `None` selon le plateau.

2. `is_full(board)`
   → renvoie `True` si plus aucune case n’est vide.

---

## 6. Implémentation Python complète

```python
from typing import List, Dict

def check_winner(board: List[List[str]]) -> str | None:
    """
    Vérifie si 'x' ou 'o' a gagné sur ce plateau.
    Renvoie 'x', 'o' ou None.
    """
    lines = []

    # Lignes
    for row in board:
        lines.append(row)

    # Colonnes
    for c in range(3):
        lines.append([board[r][c] for r in range(3)])

    # Diagonales
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] != '' and line[0] == line[1] == line[2]:
            return line[0]

    return None


def is_full(board: List[List[str]]) -> bool:
    """
    Renvoie True si le plateau ne contient plus de case vide.
    """
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True


def get_proba(board: List[List[str]], next_player: str) -> Dict[str, int]:
    """
    Explore toutes les parties possibles à partir du plateau donné
    et retourne un dictionnaire comptant les victoires de 'x' et de 'o'.

    Exemple de retour :
    {'x': nb_victoires_x, 'o': nb_victoires_o}
    """
    wins = {'x': 0, 'o': 0}

    def backtrack(current_player: str):
        winner = check_winner(board)
        if winner is not None:
            wins[winner] += 1
            return

        if is_full(board):
            # Match nul : on ne compte pas dans wins['x'] ou wins['o'],
            # mais on pourrait si on voulait suivre aussi les nuls.
            return

        # Essayer tous les coups possibles
        for r in range(3):
            for c in range(3):
                if board[r][c] == '':
                    # Jouer le coup
                    board[r][c] = current_player

                    # Joueur suivant
                    next_p = 'o' if current_player == 'x' else 'x'
                    backtrack(next_p)

                    # Annuler le coup (backtracking)
                    board[r][c] = ''

    backtrack(next_player)
    return wins
```

---

## 7. Exemple d’utilisation

```python
arr = [
    ['o', 'x', 'o'],
    ['o', 'o', 'x'],
    ['x', 'x', ''],
]
next_player = 'o'
wins = get_proba(arr, next_player)
assert wins['o'] == 1
assert wins['x'] == 0

arr = [
    ['o', 'x', 'x'],
    ['o', 'o', 'x'],
    ['x', '', ''],
]
next_player = 'o'
wins = get_proba(arr, next_player)
assert wins['o'] == 1
assert wins['x'] == 1
```

---

## 8. Pour aller plus loin (facultatif)

On pourrait :

* compter également les **matchs nuls** (`draws`),
* dériver de vrais **pourcentages** à partir des comptes :

  ```python
  total = wins['x'] + wins['o'] + draws
  proba_x = wins['x'] / total
  proba_o = wins['o'] / total
  ```
* implémenter un véritable **Minimax** pour choisir le *meilleur coup* plutôt que de juste compter.

Mais pour le labo, l’exploration exhaustive + comptage suffit largement.

---

# Conclusion

Le morpion est un cas parfait pour s’entraîner à :

* représenter un **arbre de jeu**,
* écrire un **backtracking propre** (coup → récursion → annulation),
* compter les nombres de fins gagnantes pour chaque joueur.

Ce schéma est réutilisable pour beaucoup d’autres petits jeux combinatoires.

