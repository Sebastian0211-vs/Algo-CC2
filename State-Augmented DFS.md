# **State-Augmented DFS — Parcours en profondeur sur graphe d’états**

Le **State-Augmented DFS** est une extension du DFS classique.
Au lieu d’explorer uniquement des **sommets**, on explore des **états**, c’est-à-dire des couples :

```
état = (sommet, contexte)
```

Le contexte représente toute information supplémentaire nécessaire pour décrire correctement la situation courante.

---

## 1. **Problème résolu par le State-Augmented DFS**

State-Augmented DFS permet :

* d’explorer **complètement un espace d’états**,
* de vérifier **l’existence d’une solution** sous contraintes,
* de faire du **backtracking** avec mémoire d’état,
* d’analyser des **configurations dépendantes du passé**.

⚠️ Contrairement au BFS (classique ou augmenté) :

* **aucune garantie d’optimalité** (distance minimale, coût minimal).

---

## 2. **Intuition du fonctionnement**

DFS classique :

```
nœud = position
```

DFS augmenté :

```
nœud = (position, état)
```

Deux états peuvent :

* être au **même sommet**,
* mais être **différents** à cause du contexte.

Exemples :

```
(A, énergie=3) ≠ (A, énergie=1)
(A, clé=False) ≠ (A, clé=True)
```

DFS explore alors **en profondeur** toutes les branches possibles de cet espace d’états.

---

## 3. **Quand utiliser State-Augmented DFS ?**

### ✔ Utiliser si :

* tu veux savoir **s’il existe au moins une solution**,
* tu fais du **backtracking**,
* le problème est **combinatoire / exponentiel**,
* tu explores :

  * puzzles,
  * jeux,
  * configurations,
  * répartitions,
  * contraintes multiples.

### ✘ Ne pas utiliser si :

* tu cherches un **plus court chemin**,
* tu veux une **distance minimale**,
* tu veux une **solution optimale** en nombre d’actions.

👉 Dans ces cas-là : **State-Augmented BFS** ou **Dijkstra**.

---

## 4. **Représentation du graphe d’états**

### État

Un état est généralement un tuple immuable :

```python
(u, s)
```

où :

* `u` : sommet du graphe original,
* `s` : état supplémentaire (énergie, clé, parité, masque, etc.).

### Transitions

Chaque action valide génère une transition :

```
(u, s) → (v, s')
```

ou parfois :

```
(u, s) → (u, s')   # attente / transformation interne
```

---

## 5. **Algorithme (DFS sur états)**

1. Marquer l’état courant comme visité.
2. Explorer récursivement tous les **états voisins valides**.
3. Revenir en arrière (backtracking).
4. Répéter jusqu’à épuisement de l’espace ou atteinte d’un objectif.

---

## 6. **Implémentation Python (générique)**

### Version récursive (backtracking)

```python
def state_augmented_dfs(start_states, is_goal, get_neighbors):
    """
    start_states : iterable d'états initiaux
    is_goal      : fonction(state) -> bool
    get_neighbors: fonction(state) -> iterable d'états voisins
    """
    visited = set()

    def dfs(state):
        if state in visited:
            return False
        visited.add(state)

        if is_goal(state):
            return True  # solution trouvée

        for nxt in get_neighbors(state):
            if dfs(nxt):
                return True

        return False

    for s in start_states:
        if dfs(s):
            return True

    return False
```

---

## 7. **Complexité**

Soit :

* `V` le nombre de sommets,
* `K` le nombre d’états possibles par sommet.

### Complexité théorique :

* **Temps : O(V × K + transitions)**
* **Mémoire : O(V × K)** (ensemble `visited`)

⚠️ En pratique, souvent **exponentiel** → normal pour du backtracking.

---

## 8. **Applications classiques**

State-Augmented DFS est utilisé pour :

* puzzles (Sudoku, N-Queens),
* jeux (arbres de jeu),
* planification sous contraintes,
* exploration de configurations,
* problèmes NP-durs,
* backtracking avec contraintes dynamiques.

---

## 9. **Comparaison avec les autres parcours**

| Algorithme   | État | Optimalité | Usage                           |
| ------------ | ---- | ---------- | ------------------------------- |
| DFS          | ❌    | ❌          | exploration                     |
| BFS          | ❌    | ✅          | plus court chemin               |
| DFS augmenté | ✅    | ❌          | backtracking                    |
| BFS augmenté | ✅    | ✅          | chemin minimal sous contraintes |
| Dijkstra     | ✅    | ✅          | coûts pondérés                  |

---

## **Résumé**

* State-Augmented DFS = DFS sur un **graphe d’états**.
* Il explore **en profondeur**, sans notion de distance minimale.
* Idéal pour :

  * existence de solution,
  * backtracking,
  * exploration exhaustive.
* Pas adapté aux problèmes de plus court chemin.
