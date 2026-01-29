# Two Pointers & Sliding Window – Parcours optimisé de tableaux et chaînes

## 1. Intuition générale

De nombreux problèmes sur :

* tableaux,
* chaînes de caractères,

peuvent être résolus sans boucles imbriquées coûteuses.

L’idée clé :

> utiliser **deux indices** qui se déplacent de manière coordonnée
> pour parcourir les données en **temps linéaire**.

Deux patterns principaux :

1. **Two Pointers**
2. **Sliding Window**

---

## 2. Quand utiliser ces patterns ?

Tu utilises Two Pointers / Sliding Window lorsque :

* les données sont **ordonnées** ou parcourables séquentiellement ;
* tu cherches un **segment continu** (sous-tableau / sous-chaîne) ;
* tu veux réduire une complexité **O(n²)** à **O(n)**.

Cas typiques :

* sous-tableaux avec somme ou contrainte,
* fenêtres de taille variable,
* chaînes avec fréquences de caractères,
* problèmes “longest / shortest subarray”.

---

## 3. Two Pointers (tableaux ordonnés)

### Idée

On place deux pointeurs :

* un à gauche,
* un à droite,

et on les déplace selon une condition.

---

### Exemple : paire avec somme donnée

```python
def two_sum_sorted(arr, target):
    """
    arr est trié.
    Retourne True s'il existe deux éléments
    dont la somme vaut target.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return True
        elif s < target:
            left += 1
        else:
            right -= 1

    return False
```

---

## 4. Sliding Window (fenêtre glissante)

### Idée

On maintient une **fenêtre continue** `[left, right]`
qui respecte une contrainte.

On étend `right` pour inclure de nouveaux éléments,
et on déplace `left` pour **réparer** la fenêtre si nécessaire.

---

## 5. Fenêtre glissante à taille fixe

### Exemple : somme maximale d’une fenêtre de taille `k`

```python
def max_sum_window(arr, k):
    """
    Retourne la somme maximale d'une sous-fenêtre de taille k.
    """
    window_sum = sum(arr[:k])
    best = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        best = max(best, window_sum)

    return best
```

---

## 6. Fenêtre glissante à taille variable

### Exemple : plus longue sous-chaîne sans répétition

```python
def longest_unique_substring(s):
    """
    Retourne la longueur de la plus longue sous-chaîne
    sans caractères répétés.
    """
    seen = set()
    left = 0
    best = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        best = max(best, right - left + 1)

    return best
```

---

## 7. Invariant clé

Toujours maintenir un **invariant** :

> la fenêtre actuelle satisfait la contrainte du problème

C’est cet invariant qui garantit :

* la correction,
* la complexité linéaire.

---

## 8. Complexité

| Pattern        | Complexité |
| -------------- | ---------- |
| Two Pointers   | **O(n)**   |
| Sliding Window | **O(n)**   |

Chaque élément entre et sort de la fenêtre **au plus une fois**.

---

## 9. Pièges classiques

* oublier de mettre à jour l’invariant ;
* déplacer les deux pointeurs sans logique ;
* confondre fenêtre fixe et variable ;
* utiliser des boucles imbriquées inutiles.

---

## 10. Points à retenir

* Two Pointers et Sliding Window sont des **patterns**, pas des algorithmes isolés.
* Ils permettent de passer de **quadratique à linéaire**.
* Indispensables pour les problèmes sur tableaux et chaînes.

---

# Conclusion

Dès que tu vois :

* “sous-tableau”,
* “sous-chaîne”,
* “segment continu”,

pense immédiatement **Two Pointers / Sliding Window**.

C’est l’un des patterns les plus rentables à connaître.

