from typing import List, Tuple
import heapq
"""
Author : Sebastian Morsch


l'algorithme que je vais utiliser est Dijkstra pour les points suivant :
Le graphe contient uniquement des poids positifs ou nuls.
On a besoin des plus courts chemins depuis une seule source.
Dans ce problème les coûts représentent une métrique additive.


On étend progressivement un ensemble de noeuds dont on connaît déjà la distance minimale, 
en choisissant toujours celui dont la distance actuelle est la plus faible.

"""



def dijkstra(n, map, start):
    """
    n      : nombre de noeuds (1..n)
    map  : liste [u, v, w] pour arêtes dirigées u -> v de coût w
    start  : noeud source
    """

    # Liste d'adjacence
    adj = [[] for _ in range(n + 1)]
    i =0
    while i< len(map):
        u, v, w = map[i]
        list = [v,w]
        adj[u].append(list)
        i +=1

    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[start] = 0

    # File de priorité contenant (distance, noeud)
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # Si ce n'est pas la meilleure distance connue, on ignore
        if current_dist > dist[u]:
            continue

        # Relaxation des voisins
        for v, w in adj[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist



def plan_tour(map: List[Tuple[int, int, int]], src: int, dest: int) -> float:
    def get_nbr_de_noeud(map):
        i = 0
        list_unique = []
        while i < len(map):
            a, b, c = map[i]
            if not list_unique.__contains__(a):
                list_unique.append(a)
            if not list_unique.__contains__(b):
                list_unique.append(b)
            i += 1
        return len(list_unique)

    i=0
    while i<len(map):
        a,b,c = map[i]
        print(a,b,c)
        i+=1

    dist = dijkstra(get_nbr_de_noeud(map), map, src)

    # On ignore dist[0] (noeuds indexés à partir de 1)
    reachable = dist[1:]
    print(reachable)
    return reachable[dest-1]
# tests
map = [(0, 1, 20),(1, 2, 30),(2, 3, 50),(2, 0, 10),(1, 3, 20),(0, 3, 60)]



print(plan_tour(map,0,3))