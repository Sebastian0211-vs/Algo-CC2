from typing import List, Tuple

"""
Author : Sebastian Morsch


ici on cherche à compter le nombre de feuilles existantes dans le graphe et de faire un rapport avec le nombre de
feuilles marqué comme "sortie"


on enregistre deux listes a et b, respectivement une liste de source et une liste de destinations

on identifie les feuilles comme étant toute les destinations (list_b) qui ne sont pas une source elle-même

de là, le nombre de sorties nous est donnée et nous connaissons le total de feuilles existante. 
On effectue un rapport entre les deux pour obtenir la probabilité.
"""

def get_proba(labyrinth: List[Tuple[int, int]], start: int, exits: List[int]) -> float:
    list_a = []
    list_b = []
    i =0
    while i<len(labyrinth):
        a, b = labyrinth[i]
        if not list_a.__contains__(a):
            list_a.append(a)
        if not list_b.__contains__(b):
            list_b.append(b)

        i+=1
    for a in list_a:
        if list_b.__contains__(a):
            list_b.remove(a)
    print(list_b)

    return len(exits)/len(list_b)


labyrinth = [(1, 2), (1, 3), (1, 4), (3, 5), (4, 6), (4, 7)]
print(get_proba(labyrinth, 1,
            [6, 5]))