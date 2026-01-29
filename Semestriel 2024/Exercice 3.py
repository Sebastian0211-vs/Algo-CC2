

def findTightlyLinkedConsoles(n: int, consoles: list[tuple(int, int)]) -> list[int]:
    def find_clique_k(n, edges, k)-> list[int]:
        """
        Détermine s'il existe une clique de taille k dans un graphe non orienté.

        n     : nombre de sommets (0..n-1)
        edges : liste d'arêtes [u, v]
        k     : taille recherchée
        """
        # -------------------------
        # Construire la liste d'adjacence
        # -------------------------
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        # -------------------------
        # Backtracking
        # -------------------------
        def backtrack(current, candidates):
            # Si on a atteint la taille k
            if len(current) == k:
                return current.copy()

            # Pruning : impossible d'atteindre k
            if len(current) + len(candidates) < k:
                return None

            for v in list(candidates):
                # Nouveaux candidats = voisins communs
                new_candidates = candidates.intersection(adj[v])

                res = backtrack(current + [v], new_candidates)
                if res is not None:
                    return res  # on propage la solution trouvée

                # Retirer v des candidats (backtracking)
                candidates.remove(v)

            return None

            # Lancer depuis tous les sommets
        result = backtrack([], set(range(n)))

        if result is None:
            return []
        return sorted(result)


    sommets = []
    for a,b in consoles:
        if not sommets.__contains__(a) :
            sommets.append(a)
        if not sommets.__contains__(b) :
            sommets.append(b)


    nbr_de_sommets = len(sommets)
    print(len(sommets))
    print(find_clique_k(nbr_de_sommets, consoles, n))

findTightlyLinkedConsoles(4,[(0,1),(0,4),(2,1),(3,1),(4,2),(2,3),(1,4),(4,3)])