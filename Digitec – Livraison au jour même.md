# Digitec – Livraison au jour même (pruning sur arbre + distance de lancer 2)

## 1. Intuition générale

On a :
- un village modélisé par un **arbre** (un graphe connexe sans cycle) ;
- un tableau `colis` de taille `n` :
  - `colis[i] == 1` si la maison `i` doit recevoir un colis,
  - `colis[i] == 0` sinon ;
- une liste `routes` d’arêtes non orientées `[[u, v], ...]` qui forme un arbre.

Le livreur se déplace le long des routes (arêtes) **à pied / en camion**.  
À chaque position sur une maison, il peut :

> lancer un colis vers une maison située à **distance ≤ 2** (en nombre d’arêtes).

Objectif :

> Trouver **le nombre minimal d’étapes (arêtes parcourues)** pour  
> livrer tous les colis **ET revenir au point de départ**,  
> sachant qu’on peut choisir le point de départ comme on veut.

Exemple du labo :

```python
# On doit livrer un colis à la maison 0 et à la maison 5
colis =  [1, 0, 0, 0, 0, 1]
routes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
path = find_optimal_path(colis, routes)
assert path == 2
````

Intuition : en se promenant seulement entre les maisons `2` et `3`,
on reste à **distance ≤ 2** de la maison `0` et de la maison `5`, donc
on peut tout livrer avec un aller-retour minimal.

---

## 2. Vue globale de la solution

L’idée clé : on n’a pas besoin de parcourir **tout** l’arbre.

On peut raisonner en 2 phases :

1. **Garder uniquement la partie de l’arbre vraiment nécessaire**
   (celle qui est liée à au moins un colis).
2. **Réduire encore l’arbre de 2 “couches” de feuilles**
   (car on peut lancer à distance 2).

Au final, on obtient un **“noyau”** de l’arbre qu’on est obligé de parcourir,
et la longueur minimale du trajet (aller + retour) est simplement :

> `2 * (nombre d’arêtes restantes dans ce noyau)`

Si le noyau est vide ou réduit à un seul nœud → on peut tout livrer **sans bouger** → `0`.

---

## 3. Phase 1 – Garder seulement la partie utile (Steiner tree des colis)

On commence par supprimer tout ce qui est *évidemment inutile*.

1. On construit l’arbre sous forme de liste d’adjacence.
2. On calcule le degré de chaque nœud.
3. Puis on **supprime récursivement** toutes les feuilles (degré 1) qui :

   * n’ont **pas de colis** (`colis[i] == 0`).

À chaque fois qu’on supprime une feuille :

* on enlève l’arête vers son voisin,
* on décrémente le degré du voisin,
* si le voisin devient une feuille **et** n’a pas de colis, on le supprime aussi, etc.

Résultat :
Il ne reste que le **plus petit sous-arbre** qui contient tous les nœuds avec colis.

---

## 4. Phase 2 – Réduction de 2 couches de feuilles (distance de lancer = 2)

Même après la phase 1, on n’a pas besoin d’aller **jusqu’aux maisons avec colis** :

* On peut s’arrêter **2 arêtes avant** et lancer le colis.

Graphiquement : on peut **“rentrer” de 2 niveaux** à partir des feuilles.

Donc :

1. On répète **2 fois** :

   * on collecte toutes les feuilles restantes (degré 1),
   * on les supprime (comme avant) en retirant les arêtes correspondantes.

Attention :

* Si l’arbre devient vide ou ne contient plus qu’un seul nœud avant d’avoir fait 2 tours,
  on peut s’arrêter : **le coût sera 0**.

À la fin de ces 2 tours de pruning, il nous reste un noyau d’arbre :

* c’est la zone dans laquelle le livreur **doit réellement se déplacer**.

---

## 5. Calcul de la réponse

À ce stade, il reste un certain nombre d’arêtes `E_core` dans le noyau.

Un trajet optimal qui :

* part de n’importe quel nœud de ce noyau,
* parcourt toutes les arêtes nécessaires,
* revient au point de départ

a une longueur minimale de :

> `2 * E_core`

car dans un arbre, pour faire une boucle qui visite tous les bords et revient au départ,
chaque arête est parcourue **exactement 2 fois**.

Cas particulier :

* Si `E_core == 0` → réponse `0`.

---

## 6. Complexité

* Construction + pruning : chaque arête est supprimée **au plus une fois**.
* Complexité en temps : **O(n)**
* Complexité en mémoire : **O(n)**

---

## 7. Implémentation Python

```python
from collections import deque
from typing import List

def find_optimal_path(colis: List[int], routes: List[List[int]]) -> int:
    n = len(colis)
    if n == 0:
        return 0

    # -------------------------
    # Construire l'arbre
    # -------------------------
    adj = [[] for _ in range(n)]
    degree = [0] * n

    for u, v in routes:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Nombre initial d'arêtes restantes
    edges_remaining = len(routes)

    # -------------------------
    # Phase 1 : supprimer les feuilles sans colis
    # -------------------------
    q = deque()

    # Initialiser la file avec toutes les feuilles sans colis
    for i in range(n):
        if degree[i] == 1 and colis[i] == 0:
            q.append(i)

    removed = [False] * n

    while q:
        u = q.popleft()
        if removed[u]:
            continue
        removed[u] = True

        for v in adj[u]:
            if removed[v]:
                continue
            # On supprime l'arête (u, v)
            degree[v] -= 1
            edges_remaining -= 1

            if degree[v] == 1 and colis[v] == 0:
                q.append(v)

        degree[u] = 0  # u n'a plus de voisins

    # Si plus aucune arête -> soit aucun colis, soit tout est dans une "boule" réductible à un point
    if edges_remaining <= 0:
        return 0

    # -------------------------
    # Phase 2 : retirer 2 couches de feuilles (distance de lancer = 2)
    # -------------------------
    for _ in range(2):  # distance = 2
        leaves = deque()

        for i in range(n):
            if not removed[i] and degree[i] == 1:
                leaves.append(i)

        # Si rien à retirer -> plus d'arêtes ou arbre réduit à un point
        if not leaves:
            return 0

        while leaves:
            u = leaves.popleft()
            if removed[u] or degree[u] == 0:
                continue
            removed[u] = True

            for v in adj[u]:
                if removed[v]:
                    continue
                degree[v] -= 1
                edges_remaining -= 1
                if degree[v] == 1:
                    # Ce sera une feuille pour le prochain tour
                    # mais pour cette phase on les collecte tous d'un coup
                    leaves.append(v)

            degree[u] = 0

        if edges_remaining <= 0:
            return 0

    # -------------------------
    # Résultat : 2 * nb d'arêtes restantes dans le noyau
    # -------------------------
    return 2 * edges_remaining
```

---

## 8. Vérification avec l’exemple du labo

```python
colis =  [1, 0, 0, 0, 0, 1]
routes = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
path = find_optimal_path(colis, routes)
assert path == 2
```

---

# Résumé à retenir

1. **Phase 1 :** on enlève toutes les feuilles sans colis → plus petit sous-arbre contenant tous les colis.
2. **Phase 2 :** on enlève 2 couches de feuilles → on utilise le fait qu’on peut lancer à distance 2.
3. **Coût = 2 × (nombre d’arêtes restantes)**.
4. Si plus aucune arête → le livreur peut livrer en restant au même endroit → coût 0.

Cet algorithme est un très bon exemple de **pruning sur arbre** + utilisation intelligente de la distance maximale autorisée.

