
# Binary Search – Recherche binaire & patterns classiques

## 1. Intuition générale

La **recherche binaire** est un algorithme permettant de trouver une valeur ou une position
en **divisant l’espace de recherche par 2 à chaque étape**.

Contrairement à une idée reçue, la recherche binaire ne s’applique **pas uniquement** aux tableaux triés.

On distingue deux grands usages :

1. **Recherche binaire classique sur tableau trié**
2. **Recherche binaire sur l’espace des réponses** (*binary search on answer*)

---

## 2. Quand utiliser la recherche binaire ?

Tu utilises une recherche binaire lorsque :

* l’espace de recherche est **ordonné** (explicitement ou implicitement) ;
* une condition passe de **False → True** (ou l’inverse) de manière monotone ;
* tu veux réduire une complexité linéaire à **O(log n)**.

Cas typiques :

* trouver un élément dans un tableau trié,
* trouver la première position valide,
* minimiser / maximiser une valeur sous contrainte,
* problèmes du type *“minimum X tel que condition(X) est vraie”*.

---

## 3. Recherche binaire classique (tableau trié)

### Problème

Étant donné un tableau trié `arr` et une valeur `target`,
déterminer si `target` est présent et à quelle position.

---

### Implémentation Python

```python
def binary_search(arr, target):
    """
    Recherche target dans un tableau trié.
    Retourne l'indice ou -1 si absent.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

---

## 4. Variantes importantes

### 4.1 Première occurrence (lower bound)

Trouver la **première position** où `arr[i] >= target`.

```python
def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

---

### 4.2 Dernière occurrence (upper bound)

Trouver la **première position** où `arr[i] > target`.

```python
def upper_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left
```

---

## 5. Binary Search sur l’espace des réponses

### Idée clé

On ne cherche pas une valeur dans un tableau,
mais la **meilleure valeur possible** vérifiant une condition.

Propriété essentielle :

> Si `X` est valide, alors tous les `X' > X` (ou `< X`) le sont aussi
> → condition **monotone**

---

### Schéma général

```python
def binary_search_answer(low, high):
    while low < high:
        mid = (low + high) // 2
        if condition(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

---

## 6. Exemple : minimiser une capacité

### Problème

On veut la **capacité minimale** telle que toutes les tâches puissent être traitées.

---

### Condition monotone

```python
def can_process(capacity):
    # retourne True si capacity suffit
    ...
```

---

### Recherche binaire

```python
low, high = 1, max_capacity

while low < high:
    mid = (low + high) // 2
    if can_process(mid):
        high = mid
    else:
        low = mid + 1

answer = low
```

---

## 7. Pièges classiques

* oublier que `right` peut être **exclusif** ou **inclusif** ;
* boucles infinies (`left + 1 < right` mal géré) ;
* condition non monotone → recherche binaire invalide.

Toujours se poser la question :

> **Est-ce que la condition change une seule fois ?**

---

## 8. Complexité

| Type                    | Complexité   |
| ----------------------- | ------------ |
| Recherche binaire       | **O(log n)** |
| Binary search on answer | **O(log R)** |

où `R` est la taille de l’espace de recherche.

---

## 9. Points à retenir

* La recherche binaire est un **pattern**, pas juste un algorithme.
* Elle s’applique dès qu’il existe une **monotonie**.
* Très utilisée pour optimiser des problèmes difficiles.
* Indispensable en algorithmique et en examen.

---

# Conclusion

La recherche binaire est l’un des outils les plus puissants de l’algorithmique.
Dès que tu vois :

* “minimum possible”,
* “première position valide”,
* “est-ce faisable ?”,

pense immédiatement **Binary Search**.
