# **Algorithme de Dijkstra — Comprendre, Utiliser, Implémenter**

L’algorithme de **Dijkstra** est un algorithme classique de théorie des graphes permettant de calculer les **plus courts chemins à partir d’un nœud source**, dans un graphe orienté ou non orienté, lorsque **tous les poids sont positifs**.

Il est largement utilisé en **réseau**, **planification**, **routing**, **IA**, et dans les systèmes de **diagnostic distribués**.

---

## **1. Problème résolu par Dijkstra**

Étant donné :

* un graphe orienté ou non orienté,
* un ensemble d’arêtes pondérées de poids positifs,
* un nœud source `s`,

Dijkstra calcule :

* la **distance minimale** entre `s` et chaque nœud du graphe,
* et, si besoin, le **chemin exact** qui réalise cette distance.

Ce qu’il ne fait pas :

* il **ne fonctionne pas** lorsque des poids négatifs existent,
* il ne détecte pas de cycles négatifs.

---

## **2. Intuition derrière l’algorithme**

L’idée fondamentale :

> On étend progressivement un ensemble de nœuds dont on connaît déjà la distance minimale, en choisissant toujours celui dont la distance actuelle est la plus faible (principe glouton).

À chaque étape :

1. On sélectionne le nœud non encore traité ayant la plus petite distance connue.
2. On met à jour (“relaxe”) les distances des nœuds voisins.
3. On répète jusqu’à avoir traité tous les nœuds atteignables.

Ce fonctionnement nécessite une **file de priorité (min-heap)** afin de toujours extraire rapidement le nœud avec la distance la plus faible.

---

## **3. Conditions d’utilisation de Dijkstra**

Vous pouvez l’utiliser lorsque :

### ✔ Les conditions sont réunies

* Le graphe contient **uniquement des poids positifs** ou nuls.
* Vous avez besoin des **plus courts chemins depuis une seule source**.
* Vous devez résoudre un problème où les coûts représentent du **temps**, de la **distance**, du **poids**, ou n’importe quelle métrique additive.

### ✘ À éviter si

* Le graphe contient des **poids négatifs** → utiliser **Bellman-Ford**.
* Vous devez calculer **tous les plus courts chemins entre toutes les paires de nœuds** → utiliser **Floyd–Warshall**.
* Le graphe est **non pondéré** → utiliser **BFS**, plus simple et plus rapide.

---

## **4. Représentation usuelle du graphe**

Dijkstra s’utilise le plus souvent avec une **liste d’adjacence**, car elle est plus efficace qu’une matrice si le graphe est sparse.

Exemple :

```python
adj[u] = [(v1, w1), (v2, w2), ...]
```

---

## **5. Implémentation basique en Python (avec commentaires)**

```python
import heapq

def dijkstra(n, edges, start):
    """
    n      : nombre de noeuds (1..n)
    edges  : liste [u, v, w] pour arêtes dirigées u -> v de coût w
    start  : noeud source
    """

    # Liste d'adjacence
    adj = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0

    # File de priorité contenant (distance, noeud)
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Si ce n'est pas la meilleure distance connue, on ignore.
        if current_dist > dist[u]:
            continue

        # Relaxation des voisins
        for v, w in adj[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist
```

---

## **6. Complexité**

| Structure utilisée         | Complexité                                     |
| -------------------------- | ---------------------------------------------- |
| Avec min-heap (`heapq`)    | **O((V + E) log V)**                           |
| Sans heap (tableau simple) | **O(V²)** (inefficace pour les grands graphes) |

Dijkstra est optimal pour les graphes avec poids positifs et relativement sparse.

---

## **7. Exemple d’utilisation**

### Problème :

Calculer le temps minimal pour atteindre tous les nœuds d’un réseau.

```python
def minimum_time_to_reach_all(n, times, k):
    dist = dijkstra(n, times, k)

    # On ignore dist[0] (noeuds indexés à partir de 1)
    reachable = dist[1:]

    if float('inf') in reachable:
        return -1  # au moins un noeud inatteignable

    return max(reachable)
```

---

## **8. Quand choisir une autre approche ?**

| Situation                                        | Algorithme recommandé                     |
| ------------------------------------------------ | ----------------------------------------- |
| Poids négatifs                                   | Bellman-Ford                              |
| Détection de cycles négatifs                     | Bellman-Ford                              |
| Multi-source                                     | BFS (si poids 1) ou Dijkstra multi-source |
| Tous les plus courts chemins entre toutes paires | Floyd–Warshall                            |
| Graphe non pondéré                               | BFS                                       |

---

## **9. Applications concrètes**

Dijkstra est utilisé dans :

* les protocoles réseau (OSPF utilise une version de Dijkstra),
* la navigation GPS (routes les plus rapides),
* les jeux vidéo (pathfinding pondéré),
* l’analyse de propagation de signaux,
* les systèmes de diagnostic distribués (comme dans ton exercice),
* l'optimisation logistique.

---

## **Résumé**

Dijkstra est l’algorithme standard pour calculer les plus courts chemins dans un graphe pondéré **sans poids négatifs**, grâce à une approche gloutonne pilotée par une **file de priorité**.

Il fournit la solution optimale dans un temps efficace et constitue un pilier de nombreux systèmes modernes de calcul et de routage.

---
