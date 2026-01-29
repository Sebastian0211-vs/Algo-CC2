# Lowest Common Ancestor – Ancêtre commun le plus proche (LCA)

## 1. Intuition générale

On travaille avec un **arbre enraciné**.

Pour deux nœuds `u` et `v`, le **Lowest Common Ancestor (LCA)** est :

> le **nœud le plus profond** de l’arbre
> qui est ancêtre de `u` **et** de `v`.

Autrement dit :

* c’est le **premier point de rencontre** des chemins de `u` et `v` vers la racine.

---

## 2. Quand utiliser LCA ?

Tu utilises le LCA lorsque :

* tu travailles sur des **arbres** ;
* tu dois répondre à **beaucoup de requêtes** du type :

  * “quel est l’ancêtre commun de u et v ?” ;
* tu calcules des **distances** dans un arbre.

Cas typiques :

* arbres généalogiques,
* réseaux hiérarchiques,
* calcul de distance entre deux nœuds,
* problèmes de routing sur arbres.

---

## 3. Propriété clé

Dans un arbre :

> distance(u, v) = depth[u] + depth[v] − 2 × depth[LCA(u, v)]

Cette formule rend LCA central pour les problèmes de distance.

---

## 4. Approche naïve (pour comprendre)

1. Remonter le nœud le plus profond jusqu’au même niveau.
2. Remonter `u` et `v` **ensemble** jusqu’à ce qu’ils coïncident.

Complexité :

* **O(n)** par requête → trop lent si beaucoup de requêtes.

---

## 5. Approche efficace – Binary Lifting

### Idée

Pré-calculer pour chaque nœud :

> son ancêtre à distance `2^k`

On peut ainsi “sauter” rapidement vers le haut de l’arbre.

---

## 6. Prétraitement

On maintient :

* `parent[k][v]` = ancêtre de `v` à distance `2^k`
* `depth[v]` = profondeur de `v`

Avec :

* `k` jusqu’à `log2(n)`.

---

## 7. Algorithme détaillé

### Étape 1 – DFS pour la profondeur et parent immédiat

```python
def dfs(u, p):
    parent[0][u] = p
    for v in adj[u]:
        if v != p:
            depth[v] = depth[u] + 1
            dfs(v, u)
```

---

### Étape 2 – Pré-calcul des ancêtres

```python
for k in range(1, LOG):
    for v in range(n):
        if parent[k-1][v] != -1:
            parent[k][v] = parent[k-1][ parent[k-1][v] ]
```

---

### Étape 3 – Requête LCA(u, v)

1. Remonter le nœud le plus profond.
2. Remonter `u` et `v` simultanément.
3. Le parent final est le LCA.

---

## 8. Implémentation Python complète

```python
def lca_preprocess(n, edges, root=0):
    from math import log2, ceil

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    LOG = ceil(log2(n))
    parent = [[-1] * n for _ in range(LOG)]
    depth = [0] * n

    def dfs(u, p):
        parent[0][u] = p
        for v in adj[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs(v, u)

    dfs(root, -1)

    for k in range(1, LOG):
        for v in range(n):
            if parent[k-1][v] != -1:
                parent[k][v] = parent[k-1][ parent[k-1][v] ]

    return parent, depth, LOG
```

---

### Requête LCA

```python
def lca(u, v, parent, depth, LOG):
    if depth[u] < depth[v]:
        u, v = v, u

    # Remonter u au même niveau que v
    for k in range(LOG):
        if (depth[u] - depth[v]) & (1 << k):
            u = parent[k][u]

    if u == v:
        return u

    # Remonter les deux simultanément
    for k in reversed(range(LOG)):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]

    return parent[0][u]
```

---

## 9. Exemple

```python
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (1, 4),
    (2, 5),
    (2, 6)
]

parent, depth, LOG = lca_preprocess(7, edges)

print(lca(3, 4, parent, depth, LOG))  # 1
print(lca(3, 5, parent, depth, LOG))  # 0
```

---

## 10. Complexité

| Phase         | Complexité     |
| ------------- | -------------- |
| Prétraitement | **O(n log n)** |
| Requête LCA   | **O(log n)**   |
| Mémoire       | **O(n log n)** |

---

## 11. Points à retenir

* LCA est fondamental sur les arbres.
* Binary lifting permet des requêtes rapides.
* Sert directement au calcul de distances.
* Très fréquent dans les problèmes avancés.

---

# Conclusion

Le Lowest Common Ancestor est un outil clé pour tous les problèmes sur arbres.

Dès que tu vois :

* “distance entre deux nœuds dans un arbre”,
* “ancêtre commun”,

pense immédiatement **LCA**.

