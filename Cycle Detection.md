# Cycle Detection – Détection de cycles dans les graphes

## 1. Intuition générale

Un **cycle** est un chemin qui :

* commence et se termine au **même sommet**,
* contient au moins une arête.

La détection de cycles est fondamentale car :

* certains algorithmes **échouent** s’il y a des cycles,
* d’autres changent complètement de comportement.

Exemples :

* un tri topologique **n’existe pas** s’il y a un cycle,
* un cycle négatif rend les plus courts chemins **indéfinis**.

---

## 2. Quand détecter des cycles ?

Tu dois détecter des cycles lorsque :

* tu travailles sur des **graphes orientés** (dépendances) ;
* tu veux savoir si un graphe est un **DAG** ;
* tu construis un **MST** ;
* tu analyses des contraintes circulaires.

---

## 3. Cas 1 – Graphe non orienté (DFS)

### Idée

Dans un graphe non orienté :

* si on revisite un sommet **déjà visité**
* qui n’est **pas le parent immédiat**
  → **cycle détecté**

---

### Implémentation Python

```python
def has_cycle_undirected(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n

    def dfs(u, parent):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i, -1):
                return True

    return False
```

---

## 4. Cas 2 – Graphe orienté (DFS avec couleurs)

### Idée

On utilise **3 états** :

* `0` : non visité
* `1` : en cours de visite (pile DFS)
* `2` : complètement traité

Si on rencontre un sommet `v` avec état `1` :
→ **cycle détecté**

---

### Implémentation Python

```python
def has_cycle_directed(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    state = [0] * n  # 0=unvisited, 1=visiting, 2=done

    def dfs(u):
        state[u] = 1
        for v in adj[u]:
            if state[v] == 1:
                return True
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    for i in range(n):
        if state[i] == 0:
            if dfs(i):
                return True

    return False
```

---

## 5. Cas 3 – Union-Find (graphe non orienté)

### Idée

Lorsqu’on ajoute une arête `(u, v)` :

* si `u` et `v` sont déjà connectés → cycle

---

### Implémentation

```python
def has_cycle_union_find(n, edges):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True

    for u, v in edges:
        if not union(u, v):
            return True

    return False
```

---

## 6. Lien avec les autres algorithmes

| Problème         | Lien                                       |
| ---------------- | ------------------------------------------ |
| Topological sort | Cycle ⇔ impossible                         |
| MST (Kruskal)    | Cycle ⇒ arête rejetée                      |
| Bellman–Ford     | Cycle négatif                              |
| SCC              | Chaque SCC de taille > 1 contient un cycle |

---

## 7. Complexité

| Méthode    | Complexité    |
| ---------- | ------------- |
| DFS        | **O(V + E)**  |
| Union-Find | **O(E α(V))** |

---

## 8. Points à retenir

* Le type de graphe (orienté / non orienté) **change l’algorithme**.
* DFS est la méthode la plus générale.
* Union-Find est idéal pour les graphes non orientés dynamiques.
* Cycle detection est souvent implicite dans d’autres algorithmes.

---

# Conclusion

La détection de cycles est une brique fondamentale
de l’algorithmique des graphes.

Dès que tu vois :

* dépendances,
* contraintes circulaires,
* “DAG”,

pense immédiatement **Cycle Detection**.
