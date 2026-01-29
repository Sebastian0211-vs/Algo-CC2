# Vérifier si un graphe est biparti (2-coloration via BFS)

## Intuition

Un graphe est **biparti** s’il est possible de diviser les sommets en **2 groupes** (A et B) tels que :

- toutes les arêtes vont **d’un groupe à l’autre** (jamais A→A ou B→B),
- autrement dit, on peut colorier chaque sommet en **2 couleurs** (par exemple 0 et 1) de sorte que deux sommets voisins n’aient **jamais la même couleur**.

Dans ton exercice du **tournoi d’hornuss**, chaque sommet représente un professeur et chaque arête représente une paire de profs qui **ne veulent pas jouer ensemble**.  
On cherche à savoir si on peut les séparer en deux équipes de façon à ce que **aucune arête ne soit interne à une équipe** → exactement un test de graphe biparti.

---

## Quand utiliser cet algorithme ?

Tu utilises la 2-coloration / test biparti quand :

- Tu dois savoir si on peut **diviser un ensemble en deux groupes** avec des contraintes de type « ceux-là ne peuvent pas être ensemble ».
- Tu as un graphe non orienté et tu te demandes s’il contient un **cycle impair** (un graphe est biparti ssi il n’a **aucun cycle de longueur impaire**).
- Typiquement :
  - Problèmes de **conflits** (personnes qui se détestent, tâches incompatibles, etc.).
  - Affectation de **deux types de ressources** (par ex. deux couleurs, deux équipes, deux salles).

Dans le labo, cet algo sert directement pour :

- `is_tournament_possible(n, dislikes)`  
  → Construire un graphe des `dislikes` et vérifier s’il est biparti.

---

## Idée de l’algorithme (BFS, 2-coloration)

1. On construit un **graphe non orienté** sous forme de liste d’adjacence :
   - pour chaque paire `(u, v)` dans `dislikes`, on ajoute `v` dans la liste de `u`, et `u` dans la liste de `v`.

2. On garde un tableau `color` de taille `n+1` (si les sommets sont numérotés 1..n) :
   - `color[i] = -1` → non colorié
   - `color[i] = 0` ou `1` → couleur assignée

3. Pour chaque sommet `i` non colorié :
   - On lance un **BFS** depuis `i`,
   - On lui donne une couleur initiale (par exemple `0`),
   - À chaque fois qu’on visite un voisin `v` d’un sommet `u` :
     - s’il n’a pas de couleur (`-1`), on lui donne la couleur opposée `1 - color[u]` et on le met dans la file.
     - s’il a **déjà** une couleur et que `color[v] == color[u]`, alors on a trouvé un conflit → **le graphe n’est pas biparti**.

4. Si on finit tous les BFS sans conflit, le graphe est biparti.

---

## Complexité

- Construction du graphe : `O(n + m)` où `m = len(dislikes)`
- BFS : `O(n + m)` aussi
- Total : **O(n + m)** en temps, **O(n + m)** en mémoire

---

## Implémentation en Python

Ici, on code directement la fonction pour ton exercice Hornuss :

```python
from collections import deque
from typing import List

def is_tournament_possible(n: int, dislikes: List[List[int]]) -> bool:
    """
    Détermine si l'on peut diviser les n personnes en deux équipes
    de façon à ce qu'aucune paire 'dislike' ne soit dans la même équipe.
    
    C'est équivalent à tester si le graphe des dislikes est biparti.
    """
    # 1) Construire le graphe non orienté
    graph = [[] for _ in range(n + 1)]  # on utilise 1..n
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    
    # 2) Tableau de couleurs : -1 = non colorié, 0 ou 1 pour les deux groupes
    color = [-1] * (n + 1)
    
    # 3) On doit penser aux composantes connexes : le graphe peut être non connexe
    for start in range(1, n + 1):
        if color[start] != -1:
            # déjà colorié via une autre composante
            continue
        
        # Si le sommet n'a pas de voisins, il peut aller dans n'importe quelle équipe,
        # donc on peut soit le colorier arbitrairement, soit l'ignorer. On le colorie.
        if not graph[start]:
            color[start] = 0
            continue

        # BFS à partir de 'start'
        queue = deque([start])
        color[start] = 0  # couleur initiale
        
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if color[v] == -1:
                    # pas encore colorié -> on lui donne la couleur opposée
                    color[v] = 1 - color[u]
                    queue.append(v)
                else:
                    # déjà colorié -> on vérifie qu'il n'y a pas de conflit
                    if color[v] == color[u]:
                        # u et v sont dans la même équipe mais se détestent
                        return False
    
    # si on a tout colorié sans conflit, c'est possible
    return True

# =========================
# Quelques tests rapides
# =========================
if __name__ == "__main__":
    # Exemple 1 du labo
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    print(is_tournament_possible(n, dislikes))  # True

    # Exemple 2 du labo
    n = 3
    dislikes = [[1, 2], [1, 3], [2, 3]]
    print(is_tournament_possible(n, dislikes))  # False

    # Cas sans dislikes : toujours possible (tous dans n'importe quelle équipe)
    n = 3
    dislikes = []
    print(is_tournament_possible(n, dislikes))  # True
