# **DFS — Parcours en profondeur (Depth-First Search)**

L’algorithme **DFS** (Depth-First Search) explore un graphe en profondeur avant de revenir en arrière.
C’est l’un des trois parcours fondamentaux de la théorie des graphes avec **BFS** et **Dijkstra**.

DFS est extrêmement utile pour **l’analyse structurelle** d’un graphe : détection de cycles, composants connexes, topological sort, ponts, articulation points, etc.

---

# 1. **Problème résolu par DFS**

DFS permet :

* d’explorer entièrement un graphe,
* de déterminer si un nœud est atteignable depuis un autre,
* d’identifier les composantes connexes,
* de détecter la présence de cycles,
* d’effectuer un **tri topologique** (topological sort) dans un graphe orienté acyclique,
* d’identifier les **ponts** et **points d’articulation**,
* d'explorer des arbres ou sous-structures recursives.

Contrairement à BFS ou Dijkstra :

* DFS ne donne **pas** les distances minimales,
* DFS ne respecte **aucune priorité** d’exploration,
* DFS explore profondément avant de revenir en arrière.

---

# 2. **Intuition du fonctionnement**

DFS suit une logique simple :

1. On commence au nœud de départ.
2. On explore un voisin.
3. Puis un voisin de ce voisin.
4. Et ainsi de suite **jusqu’à ce qu’on ne puisse plus avancer**.
5. Alors on **revient en arrière** (backtracking) pour explorer d’autres branches.

C’est exactement ce que ferait :

* une personne explorant un labyrinthe "en longeant un mur",
* une stratégie d’arbre de recherche en profondeur.

DFS s’implémente généralement :

* soit **récursivement** (plus simple),
* soit avec une **pile explicite**.

---

# 3. **Quand utiliser DFS ?**

### ✔ Utiliser DFS lorsque :

* la priorité est d’**explorer toute la structure du graphe**,
* le graphe est **très vaste et profond**,
* on veut trouver :

  * composantes connexes,
  * cycles,
  * points d’articulation,
  * ponts,
  * ordre topologique,
  * chemins possibles (backtracking),
  * exploration d’états (IA, puzzles…).

### ✘ Ne pas utiliser DFS pour :

* les **plus courts chemins** → BFS ou Dijkstra.
* les graphes extrêmement profonds → risque de dépassement de pile (stack overflow).
* les graphes où l'ordre BFS est nécessaire (niveau par niveau).

---

# 4. **Représentation standard du graphe**

Comme pour BFS et Dijkstra, on utilise une **liste d'adjacence** :

```python
adj[u] = [v1, v2, v3]
```

---

# 5. **Implémentation Python simple (version récursive)**

```python
def dfs_recursive(n, edges, start):
    """
    n      : nombre de noeuds (1..n)
    edges  : arêtes dirigées [u, v]
    start  : noeud de départ

    Retour :
        visited = ensemble des noeuds atteignables depuis start
    """

    # Construction de la liste d'adjacence
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    visited = set()

    def dfs(u):
        visited.add(u)
        # On explore chaque voisin qui n'a pas encore été visité
        for v in adj[u]:
            if v not in visited:
                dfs(v)

    dfs(start)
    return visited
```

---

# 6. **Implémentation Python avec une pile (version itérative)**

Version utile lorsque la récursion peut dépasser la limite de profondeur.

```python
def dfs_iterative(n, edges, start):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
        adj[u].append(v)

    visited = set()
    stack = [start]  # pile LIFO

    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            # On empile les voisins
            # pour garder un comportement "profondeur d'abord"
            for v in adj[u]:
                if v not in visited:
                    stack.append(v)

    return visited
```

---

# 7. **Exemple d’utilisation**

```python
n = 6
edges = [
    [1, 2],
    [1, 3],
    [2, 4],
    [2, 5],
    [3, 6]
]

visited = dfs_recursive(n, edges, 1)
print(visited)
```

Sortie possible :

```
{1, 2, 4, 5, 3, 6}
```

Ou (pour la version itérative) :

```
{1, 3, 6, 2, 5, 4}
```

L'ordre **n’est pas garanti**, contrairement à BFS : l’important est d’explorer en profondeur.

---

# 8. **Complexité**

| Opération                    | Complexité                  |
| ---------------------------- | --------------------------- |
| Temps                        | **O(V + E)**                |
| Mémoire                      | O(V)                        |
| Risque de récursion profonde | Oui, si graphe très profond |

---

# 9. **Applications concrètes**

DFS est utilisé pour :

* détecter des cycles dans un graphe orienté,
* trouver les composantes connexes,
* déterminer si un graphe est biparti,
* faire un tri topologique,
* identifier les **ponts** et **articulation points**,
* résoudre des puzzles (labyrinthes, sudoku, n-queens),
* parcourir des arbres syntaxiques (compilateurs),
* faire de la recherche exhaustive dans l’IA.

---

# **Résumé**

* DFS explore un graphe en profondeur, contrairement au BFS qui explore par couches.
* Il est excellent pour l’analyse structurelle d’un graphe, la détection de cycles, et les algorithmes avancés.
* Il ne trouve pas les plus courts chemins.
* Il s’implémente facilement en récursif ou avec une pile explicite.
* Sa complexité est optimale : **O(V + E)**.

---
