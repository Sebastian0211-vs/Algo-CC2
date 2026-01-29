
# Strongly Connected Components – Composantes fortement connexes (SCC)

## 1. Intuition générale

On travaille avec un **graphe orienté**.

Deux sommets `u` et `v` sont **fortement connexes** si :

* on peut aller de `u` vers `v`,
* **et** de `v` vers `u`.

Une **composante fortement connexe (SCC)** est un **ensemble maximal** de sommets
tous atteignables les uns depuis les autres.

Objectif :

> découper le graphe en **SCC**, puis éventuellement le **compresser** en un DAG.

---

## 2. Quand utiliser les SCC ?

Tu utilises les composantes fortement connexes lorsque :

* tu analyses des **graphes orientés** ;
* tu veux détecter des **cycles complexes** ;
* tu veux regrouper des sommets mutuellement dépendants.

Cas typiques :

* dépendances circulaires,
* analyse de modules logiciels,
* graphes de flux,
* condensation d’un graphe en DAG.

---

## 3. Propriété clé

Dans un graphe orienté :

* chaque sommet appartient à **exactement une SCC** ;
* le graphe des SCC (graphe condensé) est **toujours un DAG**.

---

## 4. Algorithme 1 – Kosaraju

### Idée générale

Kosaraju utilise **deux DFS** :

1. DFS sur le graphe original pour calculer un **ordre de fin**.
2. DFS sur le **graphe transposé** (arêtes inversées),
   en suivant l’ordre inverse des fins.

Chaque DFS du second passage correspond à **une SCC**.

---

### Étapes

1. Construire la liste d’adjacence.
2. DFS 1 : empiler les sommets selon leur **temps de fin**.
3. Inverser toutes les arêtes → graphe transposé.
4. DFS 2 : parcourir selon l’ordre inverse,
   chaque parcours = une SCC.

---

### Implémentation Python (Kosaraju)

```python
def kosaraju_scc(n, edges):
    """
    n     : nombre de sommets (0..n-1)
    edges : liste d'arêtes (u -> v)

    Retour :
        liste de SCC (chaque SCC est une liste de sommets)
    """
    adj = [[] for _ in range(n)]
    rev = [[] for _ in range(n)]

    for u, v in edges:
        adj[u].append(v)
        rev[v].append(u)

    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    visited = [False] * n
    sccs = []

    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in rev[u]:
            if not visited[v]:
                dfs2(v, component)

    for u in reversed(order):
        if not visited[u]:
            component = []
            dfs2(u, component)
            sccs.append(component)

    return sccs
```

---

## 5. Algorithme 2 – Tarjan

### Idée générale

Tarjan utilise **un seul DFS** avec :

* un index d’entrée,
* une pile,
* des valeurs `lowlink`.

Un sommet `u` est la racine d’une SCC si :

```text
lowlink[u] == index[u]
```

---

### Implémentation Python (Tarjan)

```python
def tarjan_scc(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    index = 0
    stack = []
    on_stack = [False] * n
    ids = [-1] * n
    low = [0] * n
    sccs = []

    def dfs(u):
        nonlocal index
        ids[u] = low[u] = index
        index += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if ids[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], ids[v])

        # Racine de SCC
        if ids[u] == low[u]:
            component = []
            while True:
                v = stack.pop()
                on_stack[v] = False
                component.append(v)
                if v == u:
                    break
            sccs.append(component)

    for i in range(n):
        if ids[i] == -1:
            dfs(i)

    return sccs
```

---

## 6. Comparaison Kosaraju vs Tarjan

| Algorithme | DFS | Mémoire          | Simplicité   |
| ---------- | --- | ---------------- | ------------ |
| Kosaraju   | 2   | + graphe inverse | Très lisible |
| Tarjan     | 1   | pile + lowlink   | Plus compact |

---

## 7. Complexité

| Mesure  | Complexité   |
| ------- | ------------ |
| Temps   | **O(V + E)** |
| Mémoire | **O(V + E)** |

Les deux algorithmes sont optimaux.

---

## 8. Exemple

```python
n = 5
edges = [
    (0, 1),
    (1, 2),
    (2, 0),
    (1, 3),
    (3, 4)
]

print(kosaraju_scc(n, edges))
# Exemple : [[0,2,1], [3], [4]]
```

---

## 9. Points à retenir

* Les SCC regroupent des sommets **mutuellement atteignables**.
* Le graphe des SCC est toujours un **DAG**.
* Kosaraju est plus pédagogique.
* Tarjan est plus élégant et plus compact.

---

# Conclusion

Les composantes fortement connexes sont un outil fondamental
pour analyser les graphes orientés complexes.

Dès que tu dois :

* détecter des cycles orientés,
* regrouper des dépendances circulaires,

pense immédiatement **SCC (Kosaraju / Tarjan)**.
