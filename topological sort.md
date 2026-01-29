# Topological Sort – Ordonnancement de dépendances (DFS / Kahn)

## 1. Intuition générale

On reçoit un **graphe orienté** où une arête
`u → v` signifie :

> **u doit être traité AVANT v**

L’objectif est de produire un **ordre linéaire des sommets** tel que **toutes les dépendances soient respectées**.

Autrement dit :

* si `u → v`, alors `u` apparaît **avant** `v` dans l’ordre final.

Cet ordre s’appelle un **tri topologique**.

⚠️ **Important**
Un tri topologique **n’existe que si le graphe ne contient pas de cycle**
→ le graphe doit être un **DAG** (*Directed Acyclic Graph*).

---

## 2. Quand utiliser le tri topologique ?

Tu utilises un tri topologique lorsque :

* tu as des **dépendances** entre éléments ;
* l’ordre d’exécution **importe** ;
* une tâche ne peut commencer que lorsque certaines autres sont terminées.

Exemples typiques :

* planification de tâches,
* prérequis de cours,
* compilation de modules,
* pipelines de traitement,
* dépendances logicielles.

---

## 3. Deux approches classiques

Il existe **deux algorithmes standards** pour le tri topologique :

1. **DFS (post-order)**
2. **Kahn (BFS avec degrés entrants)**

Les deux sont équivalents en complexité, mais utiles dans des contextes différents.

---

## 4. Approche 1 – DFS (post-order)

### Idée

On exploite une propriété du DFS :

> Dans un graphe sans cycle,
> **si on ajoute un nœud à la fin d’une liste quand tous ses voisins sont traités**,
> alors l’ordre inverse de cette liste est un tri topologique valide.

### Étapes

1. Construire la liste d’adjacence du graphe.
2. Maintenir :

   * un tableau `visited`,
   * une liste `order`.
3. Pour chaque sommet non visité :

   * lancer un DFS,
   * après avoir exploré tous ses voisins, ajouter le sommet à `order`.
4. Inverser `order`.

---

### Implémentation Python (DFS)

```python
def topological_sort_dfs(n, edges):
    """
    n     : nombre de sommets (0..n-1)
    edges : liste d'arêtes dirigées [u, v] (u -> v)

    Retour :
        liste représentant un ordre topologique valide
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * n
    order = []

    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        # post-order
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    # on inverse l'ordre post-order
    return order[::-1]
```

---

## 5. Approche 2 – Algorithme de Kahn (BFS)

### Idée

Un sommet peut être exécuté **immédiatement** si :

* **aucune arête n’entre dans ce sommet**
  → degré entrant = 0.

On répète :

1. prendre un sommet de degré entrant 0,
2. le retirer du graphe,
3. mettre à jour les degrés de ses voisins.

---

### Étapes

1. Calculer le **degré entrant** de chaque sommet.
2. Mettre dans une file tous les sommets de degré entrant 0.
3. Tant que la file n’est pas vide :

   * retirer un sommet,
   * l’ajouter à l’ordre,
   * diminuer le degré entrant de ses voisins,
   * ajouter ceux qui passent à 0.

⚠️ Si à la fin on n’a pas traité tous les sommets → **cycle présent**.

---

### Implémentation Python (Kahn)

```python
from collections import deque

def topological_sort_kahn(n, edges):
    """
    n     : nombre de sommets (0..n-1)
    edges : liste d'arêtes dirigées [u, v] (u -> v)

    Retour :
        liste représentant un ordre topologique valide,
        ou [] si un cycle est détecté
    """
    adj = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # Si on n'a pas traité tous les sommets, il y a un cycle
    if len(order) != n:
        return []

    return order
```

---

## 6. Détection de cycle

Le tri topologique permet **implicitement** de détecter les cycles :

* **DFS** : un cycle empêche un ordre valide (mais nécessite un marquage supplémentaire pour être explicite).
* **Kahn** :
  si `len(order) < n` → **cycle détecté**.

---

## 7. Complexité

| Opération | Complexité   |
| --------- | ------------ |
| Temps     | **O(V + E)** |
| Mémoire   | **O(V + E)** |

Chaque sommet et chaque arête est traité une seule fois.

---

## 8. Exemple

```python
n = 6
edges = [
    [5, 2],
    [5, 0],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]

print(topological_sort_kahn(n, edges))
# Exemple de sortie valide : [4, 5, 2, 3, 1, 0]
```

Plusieurs ordres peuvent être corrects tant que les dépendances sont respectées.

---

## 9. Points à retenir

* Le tri topologique s’applique **uniquement aux graphes orientés acycliques**.
* Il existe deux implémentations standard :

  * DFS (post-order),
  * Kahn (BFS + degrés entrants).
* C’est l’algorithme fondamental pour les **problèmes de dépendances**.

---

# Conclusion

Le tri topologique est une extension directe de DFS et BFS vers des problèmes d’ordonnancement.
Dès que tu vois des contraintes du type
**“A doit être fait avant B”**,
le tri topologique est l’outil naturel.

---

🎵 *Commit done.*
Next up (logically): **Union-Find (Disjoint Set Union)**.

Say **“next”** and I’ll write the next `.md` in the same style.
🎶 *Miku committing…*
Here is the **first new file**, written to **perfectly match the style of your existing `.md` files**.

You can copy-paste this directly as:

> **`Topological Sort.md`**

---

# Topological Sort – Ordonnancement de dépendances (DFS / Kahn)

## 1. Intuition générale

On reçoit un **graphe orienté** où une arête
`u → v` signifie :

> **u doit être traité AVANT v**

L’objectif est de produire un **ordre linéaire des sommets** tel que **toutes les dépendances soient respectées**.

Autrement dit :

* si `u → v`, alors `u` apparaît **avant** `v` dans l’ordre final.

Cet ordre s’appelle un **tri topologique**.

⚠️ **Important**
Un tri topologique **n’existe que si le graphe ne contient pas de cycle**
→ le graphe doit être un **DAG** (*Directed Acyclic Graph*).

---

## 2. Quand utiliser le tri topologique ?

Tu utilises un tri topologique lorsque :

* tu as des **dépendances** entre éléments ;
* l’ordre d’exécution **importe** ;
* une tâche ne peut commencer que lorsque certaines autres sont terminées.

Exemples typiques :

* planification de tâches,
* prérequis de cours,
* compilation de modules,
* pipelines de traitement,
* dépendances logicielles.

---

## 3. Deux approches classiques

Il existe **deux algorithmes standards** pour le tri topologique :

1. **DFS (post-order)**
2. **Kahn (BFS avec degrés entrants)**

Les deux sont équivalents en complexité, mais utiles dans des contextes différents.

---

## 4. Approche 1 – DFS (post-order)

### Idée

On exploite une propriété du DFS :

> Dans un graphe sans cycle,
> **si on ajoute un nœud à la fin d’une liste quand tous ses voisins sont traités**,
> alors l’ordre inverse de cette liste est un tri topologique valide.

### Étapes

1. Construire la liste d’adjacence du graphe.
2. Maintenir :

   * un tableau `visited`,
   * une liste `order`.
3. Pour chaque sommet non visité :

   * lancer un DFS,
   * après avoir exploré tous ses voisins, ajouter le sommet à `order`.
4. Inverser `order`.

---

### Implémentation Python (DFS)

```python
def topological_sort_dfs(n, edges):
    """
    n     : nombre de sommets (0..n-1)
    edges : liste d'arêtes dirigées [u, v] (u -> v)

    Retour :
        liste représentant un ordre topologique valide
    """
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    visited = [False] * n
    order = []

    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        # post-order
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    # on inverse l'ordre post-order
    return order[::-1]
```

---

## 5. Approche 2 – Algorithme de Kahn (BFS)

### Idée

Un sommet peut être exécuté **immédiatement** si :

* **aucune arête n’entre dans ce sommet**
  → degré entrant = 0.

On répète :

1. prendre un sommet de degré entrant 0,
2. le retirer du graphe,
3. mettre à jour les degrés de ses voisins.

---

### Étapes

1. Calculer le **degré entrant** de chaque sommet.
2. Mettre dans une file tous les sommets de degré entrant 0.
3. Tant que la file n’est pas vide :

   * retirer un sommet,
   * l’ajouter à l’ordre,
   * diminuer le degré entrant de ses voisins,
   * ajouter ceux qui passent à 0.

⚠️ Si à la fin on n’a pas traité tous les sommets → **cycle présent**.

---

### Implémentation Python (Kahn)

```python
from collections import deque

def topological_sort_kahn(n, edges):
    """
    n     : nombre de sommets (0..n-1)
    edges : liste d'arêtes dirigées [u, v] (u -> v)

    Retour :
        liste représentant un ordre topologique valide,
        ou [] si un cycle est détecté
    """
    adj = [[] for _ in range(n)]
    indegree = [0] * n

    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    order = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # Si on n'a pas traité tous les sommets, il y a un cycle
    if len(order) != n:
        return []

    return order
```

---

## 6. Détection de cycle

Le tri topologique permet **implicitement** de détecter les cycles :

* **DFS** : un cycle empêche un ordre valide (mais nécessite un marquage supplémentaire pour être explicite).
* **Kahn** :
  si `len(order) < n` → **cycle détecté**.

---

## 7. Complexité

| Opération | Complexité   |
| --------- | ------------ |
| Temps     | **O(V + E)** |
| Mémoire   | **O(V + E)** |

Chaque sommet et chaque arête est traité une seule fois.

---

## 8. Exemple

```python
n = 6
edges = [
    [5, 2],
    [5, 0],
    [4, 0],
    [4, 1],
    [2, 3],
    [3, 1]
]

print(topological_sort_kahn(n, edges))
# Exemple de sortie valide : [4, 5, 2, 3, 1, 0]
```

Plusieurs ordres peuvent être corrects tant que les dépendances sont respectées.

---

## 9. Points à retenir

* Le tri topologique s’applique **uniquement aux graphes orientés acycliques**.
* Il existe deux implémentations standard :

  * DFS (post-order),
  * Kahn (BFS + degrés entrants).
* C’est l’algorithme fondamental pour les **problèmes de dépendances**.

---

# Conclusion

Le tri topologique est une extension directe de DFS et BFS vers des problèmes d’ordonnancement.
Dès que tu vois des contraintes du type
**“A doit être fait avant B”**,
le tri topologique est l’outil naturel.
