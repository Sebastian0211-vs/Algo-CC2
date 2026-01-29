from typing import List, Tuple

"""
Author : Sebastian Morsch


Sachant que des "obstacles" peuvent s'alterner dépend si une minute est paire ou impaire il est nécessaire de garder en
mémoire un compteur de mouvant afin d'y pouvoir détecter ces changements.

ma première intuition pour cette algorithme serait de partir sur un algorithme type Remplissage de zone (DFS/BFS), comme
si le personnage principale s'étalait sur les cases disponibles jusqu'à l'arrivée. 
de là prendre un chemin optimisée sachant la possibilité de pouvoir rester sur place pour attendre un mouvement des obsatcles 
paires et impaires



"""
def solve_level(
    level: List[List[str]], start: Tuple[int, int], dest: Tuple[int, int]
) -> List[Tuple[int, int]]:

    return []
