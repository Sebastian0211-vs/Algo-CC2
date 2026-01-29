# **State-Augmented BFS — Parcours en largeur sur graphe d’états**

Le **State-Augmented BFS** (ou BFS sur graphe d’états) est une généralisation du BFS classique.
Il s’applique lorsque **l’état d’un problème ne se résume pas à un sommet**, mais dépend aussi d’un **contexte supplémentaire**.

Au lieu de visiter uniquement des nœuds `u`, on visite des **états** :

```
état = (sommet, état_supplémentaire)
```

Le BFS s’effectue alors sur ce **graphe d’états**.

---

# 1. **Problème résolu par le State-Augmented BFS**

Le State-Augmented BFS permet de résoudre des problèmes où :

* chaque action a un **coût constant** (souvent 1),
* mais la possibilité d’agir dépend d’un **contexte** :

  * temps (jour/nuit),
  * énergie restante,
  * nombre de jokers utilisés,
  * clé possédée ou non,
  * mode actif (normal / boost / cooldown),
  * etc.

Il permet de :

* trouver le **plus court chemin en nombre d’actions**,
* tout en tenant compte de **contraintes dynamiques**.

👉 C’est toujours un **plus court chemin non pondéré**, mais dans un espace d’états plus grand.

---

# 2. **Intuition du fonctionnement**

Dans un BFS classique :

```
nœud = position
```

Dans un BFS avec état :

```
nœud = (position, contexte)
```

Deux états peuvent :

* être sur le **même sommet**,
* mais être **différents** à cause du contexte.

Exemple :

```
(A, jour) ≠ (A, nuit)
```

Le BFS explore donc :

* toutes les combinaisons **position × état** atteignables,
* couche par couche (nombre minimal d’actions).

---

# 3. **Quand utiliser State-Augmented BFS ?**

### ✔ Utiliser State-Augmented BFS si :

* toutes les actions ont le **même coût**,
* mais certaines actions ne sont possibles **que dans certains états**,
* le problème peut être modélisé par :

  * déplacements,
  * attentes,
  * consommations / changements de mode.

### ✘ Ne pas utiliser si :

* les actions ont des coûts différents → **Dijkstra**,
* l’état n’influence pas les transitions → BFS classique.

---

# 4. **Représentation du graphe d’états**

## 4.1 État

Un état est généralement un tuple :

```python
(u, s)
```

où :

* `u` = sommet du graphe original,
* `s` = état supplémentaire (parité, énergie, clé, etc.).

## 4.2 Transitions

Chaque action devient une **arête dans le graphe d’états**.

Types fréquents de transitions :

* **Déplacement** : `(u, s) → (v, s')`
* **Attente** : `(u, s) → (u, s')`
* **Consommation** : `(u, s) → (u, s-1)`

---

# 5. **Algorithme (BFS généralisé)**

1. Initialiser une **file FIFO** avec un ou plusieurs états initiaux.
2. Maintenir une structure `visited` ou `dist` sur les **états**.
3. Tant que la file n’est pas vide :

   * extraire un état `(u, s)`,
   * générer tous les états voisins valides,
   * ajouter ceux non visités à la file.
4. Le premier moment où un état objectif est atteint correspond à la solution optimale.

---

# 6. **Implémentation Python (générique)**

```python
from collections import deque

def state_augmented_bfs(start_states, is_goal, get_neighbors):
    """
    start_states : liste d'états initiaux
    is_goal      : fonction(state) -> bool
    get_neighbors: fonction(state) -> iterable d'états voisins

    Retourne :
        parent : dictionnaire pour reconstruire un chemin
        goal_state : état objectif atteint (ou None)
    """
    queue = deque()
    visited = set()
    parent = {}

    for s in start_states:
        queue.append(s)
        visited.add(s)
        parent[s] = None

    while queue:
        state = queue.popleft()

        if is_goal(state):
            return parent, state

        for nxt in get_neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = state
                queue.append(nxt)

    return parent, None
```

---

# 7. **Complexité**

Soit :

* `V` le nombre de sommets,
* `K` le nombre de valeurs possibles de l’état supplémentaire,
* `E` le nombre d’arêtes du graphe original.

Le graphe d’états contient :

* `V × K` états,
* `O(E × K + V × K)` transitions.

### Complexité :

* **Temps : O(V·K + E·K)**
* **Mémoire : O(V·K)**

👉 En pratique, `K` est souvent petit (2, 3, quelques dizaines).

---

# 8. **Applications classiques**

State-Augmented BFS est utilisé pour :

* graphes avec **temps / parité**,
* labyrinthes avec **clés et portes**,
* jeux avec **cooldowns**,
* chemins avec **nombre limité de bonus**,
* planification sous contraintes simples,
* puzzles à états discrets.

---

# 9. **Résumé**

* On applique un BFS **non pas sur des sommets**, mais sur des **états**.
* Chaque état combine une position et un contexte.
* Toutes les actions coûtent 1 ⇒ BFS reste valide.
* Le premier état objectif atteint est optimal.
* C’est un pattern fondamental dès qu’un BFS “simple” ne suffit plus.

