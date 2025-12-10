# Counting Ships – Détection de composantes avec contrainte d’espacement

## 1. Intuition générale

On reçoit un plateau M×N composé de :
- `"X"` : une case contenant un morceau de bateau  
- `"."` : une case vide  

Un bateau est une **composante connexe de cases "X"**, mais avec une règle spéciale :

> Deux bateaux **ne peuvent pas être adjacents horizontalement ni verticalement**.  
> Il doit toujours rester **au moins une case vide** entre eux.

Conséquence importante :

- Chaque bateau peut être compté en effectuant un **DFS/BFS flood fill**,  
- Et on n’a **pas besoin de gérer les connexions diagonales**,  
- On doit uniquement compter combien de composantes indépendantes existent.

---

## 2. Quand utiliser cet algorithme ?

Cette méthode s'applique quand :
- on doit compter le nombre d’objets isolés dans une grille (îlots, groupes, régions) ;
- les objets sont représentés par des cellules adjacentes (4 directions seulement) ;
- on veut ignorer les diagonales (≠ “Number of Islands” diagonales autorisées).

Dans le labo, cet algorithme sert pour :

- `count_ships(board)`

---

## 3. Idée de la solution

1. Parcourir chaque cellule de la grille.
2. Lorsqu’on tombe sur un `"X"` non encore visité :
   - c’est **un nouveau bateau**, donc on incrémente le compteur.
   - on lance un **DFS/BFS** pour marquer toutes les cases `"X"` connexes.
3. Continuer jusqu’à avoir parcouru toute la grille.

Rappel important :  
Grâce à la règle d’espacement, **deux bateaux ne peuvent jamais être connectés**, donc chaque flood-fill représente exactement 1 bateau.

---

## 4. Complexité

- **Temps : O(M × N)**  
  Chaque cellule est visitée au plus une fois.

- **Mémoire : O(M × N)** (pile/queue ou tableau de visited)

---

## 5. Implémentation Python (DFS itératif)

```python
def count_ships(board):
    """
    Compte le nombre de bateaux sur un plateau MxN.
    Un bateau est une composante connexe (haut/bas/gauche/droite) de 'X'.
    """
    if not board:
        return 0
    
    M, N = len(board), len(board[0])
    visited = [[False] * N for _ in range(M)]

    def dfs(r, c):
        stack = [(r, c)]
        visited[r][c] = True
        
        while stack:
            x, y = stack.pop()
            # 4 directions
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if not visited[nx][ny] and board[nx][ny] == "X":
                        visited[nx][ny] = True
                        stack.append((nx, ny))

    count = 0
    for r in range(M):
        for c in range(N):
            if board[r][c] == "X" and not visited[r][c]:
                count += 1
                dfs(r, c)
    
    return count
````

---

## 6. Tests du labo

```python
board = [
    ["X",".",".","X"],
    [".",".",".","X"],
    [".",".",".","X"]
]
assert count_ships(board) == 2

board = [
    ["X",".",".","X","X"],
    ["X",".",".","X","X"],
    [".","X",".","X","X"]
]
assert count_ships(board) == 3
```

---

## 7. Pourquoi cela fonctionne ?

* Le flood-fill garantit que **toutes les cases d’un bateau** sont visitées d’un coup.
* La règle imposant qu’aucun bateau ne peut être adjacent horizontalement/verticalement assure :

  * qu’il n’existe **jamais de collisions accidentelles** entre bateaux,
  * qu’un seul DFS correspond exactement à **un bateau**.

Ainsi, le comptage par composantes connexes est correct et optimal.

---

# Conclusion

Ce problème est un cas classique de détection de composantes sur grille avec DFS/BFS.
Le point essentiel est que chaque bateau doit être un groupe isolé, ce qui simplifie le comptage :
**un flood-fill = un bateau**.
