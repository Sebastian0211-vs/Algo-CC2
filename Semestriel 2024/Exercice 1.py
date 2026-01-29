"""
J'utilise une hash table pour réduire le lookup de la valeur opposé de O(n) à O(1),
ce qui donne un algorithm O(n) au lieu d'un naif O(n**2)
"""

def countKey(pieces: list[int]) -> int:
    s = set(pieces)
    count = 0
    for x in s:
        if x > 0 and -x in s:
            count += 1
    return count


print(countKey([-3, 4, 2, 8, 9, 1, -3, -8, -4, 2, 8, 2, -8, 1, 3]))