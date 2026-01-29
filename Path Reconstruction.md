# Path Reconstruction – Reconstruire un chemin optimal

## 1. Intuition générale

Dans de nombreux algorithmes :

* BFS,
* Dijkstra,
* Bellman–Ford,
* 0–1 BFS,

on calcule des **distances minimales**, mais ce n’est souvent **pas suffisant**.

On veut aussi :

> reconstruire **le chemin exact** utilisé pour atteindre un sommet.

C’est le rôle du **path reconstruction**.

---

## 2. Idée clé

Lorsqu’on explore le graphe,
chaque fois qu’on améliore la distance d’un sommet `v` depuis `u` :

> `u` devient le **parent** de `v` dans le chemin optimal.

On maintient donc :

* `parent[v]` = sommet précédent sur le chemin optimal vers `v`

---

## 3. Principe général

1. Initialiser `parent[source] = -1`
2. Lorsqu’un sommet `v` est découvert via `u` :

   ```python
   parent[v] = u
   ```
3. Une fois l’algorithme terminé :

   * remonter depuis la destination jusqu’à la source,
   * inverser le chemin.

---

## 4. Reconstruction d’un chemin

```python
def reconstruct_path(parent, start, end):
    """
    Reconstruit le chemin de start à end
    à partir du tableau parent.
    """
    path = []
    cur = end

    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    path.reverse()

    if path[0] == start:
        return path
    return []  # end inaccessible depuis start
```

---

## 5. Exemple avec BFS

```python
from collections import deque

def bfs_with_path(n, edges, source):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    dist = [-1] * n
    parent = [-1] * n

    dist[source] = 0
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                queue.append(v)

    return dist, parent
```

---

### Utilisation

```python
dist, parent = bfs_with_path(n, edges, 0)
path = reconstruct_path(parent, 0, 5)
print(path)
```

---

## 6. Exemple avec Dijkstra

Dans Dijkstra, le principe est **identique** :

* à chaque relaxation réussie,
* on met à jour `parent[v]`.

```python
if new_dist < dist[v]:
    dist[v] = new_dist
    parent[v] = u
```

---

## 7. Cas particuliers

### 7.1 Destination inaccessible

* `parent[end]` n’a jamais été mis à jour
* reconstruction renvoie `[]`

---

### 7.2 Plusieurs chemins optimaux

* un seul parent est stocké,
* on reconstruit **un** chemin optimal,
* pas forcément tous.

---

## 8. Complexité

| Opération            | Complexité                |
| -------------------- | ------------------------- |
| Stockage des parents | **O(V)**                  |
| Reconstruction       | **O(longueur du chemin)** |

Négligeable par rapport à l’algorithme principal.

---

## 9. Points à retenir

* Le path reconstruction est **indépendant** de l’algorithme.
* Il repose toujours sur un tableau `parent`.
* Fonctionne avec BFS, Dijkstra, Bellman–Ford, etc.
* Très souvent demandé en examen.

---

# Conclusion

Calculer une distance sans pouvoir expliquer **le chemin suivi**
est rarement suffisant.

Dès que tu veux :

* afficher un itinéraire,
* expliquer une solution,
* vérifier une trajectoire,

ajoute toujours **Path Reconstruction**.

