

# Minimax & Alpha–Beta Pruning – Prise de décision optimale dans les jeux

## 1. Intuition générale

On modélise un jeu à deux joueurs comme un **arbre de décisions** :

* les **nœuds** représentent des états du jeu,
* les **arêtes** représentent des coups possibles,
* les joueurs jouent **alternativement**.

Hypothèse clé :

> les deux joueurs jouent **de manière optimale**.

Objectif :

> déterminer le **meilleur coup possible** pour le joueur courant.

---

## 2. Quand utiliser Minimax ?

Tu utilises Minimax lorsque :

* le jeu est **à deux joueurs** ;
* les gains sont **opposés** (zéro-sum game) ;
* l’information est **parfaite** (pas de hasard, pas d’information cachée).

Exemples typiques :

* Tic-tac-toe,
* échecs (version simplifiée),
* dames,
* jeux de plateau abstraits.

---

## 3. Modélisation en arbre de jeu

Chaque nœud :

* contient un **état du jeu**,
* a des enfants correspondant aux coups possibles.

Types de nœuds :

* **MAX** : le joueur cherche à **maximiser** le score.
* **MIN** : l’adversaire cherche à **minimiser** le score.

Les feuilles ont une **valeur d’évaluation**.

---

## 4. Algorithme Minimax

### Principe

* MAX choisit le coup qui **maximise** la valeur.
* MIN choisit le coup qui **minimise** la valeur.
* La valeur d’un nœud est déterminée **récursivement**.

---

### Pseudo-logique

```text
MINIMAX(node):
    si node est terminal:
        retourner valeur(node)

    si node est MAX:
        retourner max(MINIMAX(enfant))
    sinon:
        retourner min(MINIMAX(enfant))
```

---

## 5. Implémentation Python (Minimax simple)

Exemple abstrait (arbre déjà construit) :

```python
def minimax(node, is_max):
    """
    node : nœud courant
    is_max : True si joueur MAX, False sinon
    """
    if node.is_terminal():
        return node.value()

    if is_max:
        best = float('-inf')
        for child in node.children():
            best = max(best, minimax(child, False))
        return best
    else:
        best = float('inf')
        for child in node.children():
            best = min(best, minimax(child, True))
        return best
```

---

## 6. Limite de Minimax

Le problème majeur :

* la taille de l’arbre explose rapidement ;
* complexité : **O(b^d)**
  où `b` = facteur de branchement, `d` = profondeur.

Même pour des jeux simples, c’est trop lent.

---

## 7. Alpha–Beta Pruning

### Idée clé

On peut **couper** des branches de l’arbre
qui **n’influenceront jamais la décision finale**.

On maintient deux bornes :

* **α (alpha)** : meilleure valeur garantie pour MAX
* **β (beta)** : meilleure valeur garantie pour MIN

Si :

```text
alpha >= beta
```

→ on **arrête l’exploration** de la branche.

---

## 8. Implémentation Python (Minimax + Alpha-Beta)

```python
def minimax_ab(node, depth, alpha, beta, is_max):
    """
    node  : état courant
    depth : profondeur restante
    alpha : borne inférieure (MAX)
    beta  : borne supérieure (MIN)
    """
    if depth == 0 or node.is_terminal():
        return node.value()

    if is_max:
        best = float('-inf')
        for child in node.children():
            val = minimax_ab(child, depth - 1, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # coupure beta
        return best
    else:
        best = float('inf')
        for child in node.children():
            val = minimax_ab(child, depth - 1, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # coupure alpha
        return best
```

---

## 9. Ordre des coups (important)

L’efficacité d’Alpha–Beta dépend fortement de l’ordre des coups :

* bons coups évalués **en premier** → pruning maximal ;
* mauvais ordre → presque aucun gain.

Dans les jeux réels :

* heuristiques de tri des coups,
* iterative deepening,
* tables de transposition.

---

## 10. Complexité

| Algorithme         | Complexité     |
| ------------------ | -------------- |
| Minimax            | **O(b^d)**     |
| Alpha–Beta (idéal) | **O(b^(d/2))** |
| Mémoire            | O(d)           |

Alpha–Beta permet **de doubler la profondeur atteignable**.

---

## 11. Points à retenir

* Minimax modélise la décision optimale à deux joueurs.
* Alpha–Beta évite des calculs inutiles.
* Toujours coupler avec :

  * limite de profondeur,
  * fonction d’évaluation.

---

# Conclusion

Minimax et Alpha–Beta sont les algorithmes fondamentaux
de l’**IA de jeux déterministes**.

Dès que tu vois :

* jeu à deux joueurs,
* décisions adversariales,
* recherche optimale,

pense immédiatement **Minimax + Alpha–Beta**.

