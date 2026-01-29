# Flood Fill – Remplissage de zone (DFS/BFS)

## 1. Intuition générale

Le *Flood Fill* est un algorithme classique de traitement d’images et de grilles.  
Il consiste à **remplacer la valeur d’une zone connexe** (pixels adjacents) par une nouvelle valeur, en partant d’un pixel source.

C’est exactement le comportement de l’outil “seau de peinture” (Paint Bucket Tool) dans Photoshop.

Dans le labo, tu reçois :
- une image M×N (grid),
- une position `(sr, sc)`,
- une **nouvelle couleur**,
et tu dois renvoyer l’image après remplissage.

---

## 2. Quand utiliser Flood Fill ?

On utilise Flood Fill lorsque :
- on veut **modifier une zone entière connectée** dans une grille (images, labos, cartes, etc.) ;
- on doit identifier ou redessiner un **groupe de cellules adjacentes** partageant la même valeur d'origine ;
- on travaille avec des problèmes de type **remplissage, segmentation, îlots, zones**.

Dans le labo Searching Space, il sert pour :

- `fill(image, sr, sc, color)`

---

## 3. Idée principale

1. On observe la **couleur d’origine** à la position `(sr, sc)`.  
2. À partir de cette cellule, on visite **toutes les cellules adjacentes** (haut, bas, gauche, droite)  
   ayant **exactement la même couleur d’origine**.  
3. À chaque cellule visitée, on remplace la couleur par la couleur cible.  
4. On continue jusqu’à ce qu’il n’y ait plus de cellule valide à explorer.

L'algorithme peut s’implémenter soit par **DFS**, soit par **BFS**.  
Les deux donnent le même résultat.

---

## 4. Complexité

- **Temps : O(M × N)**  
  Dans le pire cas, on visite toutes les cellules une seule fois.

- **Mémoire :**
  - DFS récursif → O(M × N) dans le pire cas à cause de la pile d’appel  
  - BFS ou DFS itératif → O(M × N) pour la file/pile

---

## 5. Implémentation Python (DFS itératif, sûre et propre)

```python
def fill(image, sr, sc, color):
    """
    Flood Fill sur une image (grille) en utilisant une DFS itérative.
    Modifie toutes les cellules connectées à (sr, sc) et ayant la même couleur initiale.
    """
    m, n = len(image), len(image[0])
    original = image[sr][sc]

    # Si la couleur est déjà identique, rien à faire
    if original == color:
        return image

    stack = [(sr, sc)]
    image[sr][sc] = color

    while stack:
        r, c = stack.pop()

        # Quatre directions : up, down, left, right
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            # Vérifier les bornes et la couleur d'origine
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original:
                image[nr][nc] = color
                stack.append((nr, nc))

    return image
````

---

## 6. Version BFS (optionnelle)

```python
from collections import deque

def fill_bfs(image, sr, sc, color):
    m, n = len(image), len(image[0])
    original = image[sr][sc]

    if original == color:
        return image

    queue = deque([(sr, sc)])
    image[sr][sc] = color

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == original:
                image[nr][nc] = color
                queue.append((nr, nc))

    return image
```

---

## 7. Tests du labo

```python
image = [[1,1,1],[1,1,0],[1,0,1]]
sr, sc = 1, 1
color = 2

res = fill(image, sr, sc, color)
assert res == [[2,2,2],[2,2,0],[2,0,1]]
```

---

# Conclusion

Flood Fill est un cas d’école pour BFS/DFS sur une grille.
Il sert autant pour du traitement d'images que pour des problèmes d’îlots, de connexité ou de marquage de zones.
