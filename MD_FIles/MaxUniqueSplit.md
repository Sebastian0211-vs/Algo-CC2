
# Maximum Unique Split – Backtracking avec ensemble de substrings

## 1. Intuition générale

On reçoit une chaîne `s` et on veut la découper en **plusieurs sous-chaînes contiguës**, de telle sorte que :

- toutes les sous-chaînes obtenues soient **uniques** (aucun doublon),
- le **nombre de sous-chaînes** soit maximal.

Exemples (du labo) :

- `s = "ababccc"`  
  Une découpe possible maximale : `"a", "b", "ab", "c", "cc"` → 5 morceaux  
  → `find_maximum_split("ababccc") == 5`

- `s = "aba"`  
  Une découpe maximale : `"a", "ab"` → 2 morceaux

- `s = "aa"`  
  On ne peut pas faire `"a", "a"` (doublon),  
  donc seule `"aa"` est valide → 1 morceau.

Ce n’est pas un problème de DP classique, mais un bon cas pour du **backtracking + pruning**.

---

## 2. Quand utiliser cet algorithme ?

On utilise ce schéma quand :

- on découpe une chaîne en **segments contigus** ;
- on impose une contrainte de **unicité** des segments ;
- on cherche un **maximum** (ici, du nombre de morceaux possibles).

Ce pattern de backtracking se retrouve souvent dans des problèmes où :

- on explore toutes les partitions possibles,
- on garde un set des choix déjà utilisés,
- on maximise un certain critère (taille, nombre, etc.).

Dans le labo, on l’utilise pour :

- `find_maximum_split(s)`

---

## 3. Idée principale (Backtracking)

On parcourt la chaîne de gauche à droite, en essayant toutes les possibilités de découpe :

À chaque position `i`, on essaie toutes les sous-chaînes `s[i:j]` possibles (avec `j > i`) :

1. Si `s[i:j]` n’a pas encore été utilisée :
   - on l’ajoute à un ensemble `used`,
   - on continue récursivement depuis `j`,
   - on met à jour la meilleure réponse globale.

2. À la fin (si on est au bout de la chaîne),  
   on regarde combien de morceaux on a utilisés (`len(used)` ou un compteur).

On garde une variable globale (ou passée par référence) `best` qui suit le **maximum** atteint.

---

## 4. Optimisations (branch & bound simple)

On peut faire un *pruning* (ébranchage) basique :

- Il reste `remaining = len(s) - index` caractères.
- Même si on faisait **chaque caractère en morceau individuel**, on ne pourrait pas obtenir plus que `current_count + remaining`.

Si `current_count + remaining <= best`,  
on peut **arrêter** la branche : elle ne battra jamais le meilleur.

C’est un exemple de **Branch and Bound** appliqué au backtracking.

---

## 5. Complexité

- Dans le pire cas, le nombre de partitions possibles est **exponentiel**.
- Mais avec :
  - l’ensemble `used` qui bloque les doublons,
  - le pruning,
  
la solution est suffisamment efficace pour les tailles de chaînes du labo.

---

## 6. Implémentation Python (Backtracking + set + pruning)

```python
def find_maximum_split(s: str) -> int:
    """
    Retourne le nombre maximum de sous-chaînes uniques
    dans lesquelles on peut découper s.
    """
    n = len(s)
    used = set()
    best = 0

    def backtrack(index: int, count: int):
        nonlocal best

        # Pruning : même en faisant un caractère par morceau,
        # peut-on battre le meilleur ?
        remaining = n - index
        if count + remaining <= best:
            return

        # Si on a consommé toute la chaîne, mettre à jour le maximum
        if index == n:
            best = max(best, count)
            return

        # Essayer toutes les sous-chaînes s[index:j]
        for j in range(index + 1, n + 1):
            substr = s[index:j]
            if substr in used:
                continue  # déjà utilisée, on saute

            # Choisir cette sous-chaîne
            used.add(substr)
            backtrack(j, count + 1)
            # Backtrack
            used.remove(substr)

    backtrack(0, 0)
    return best
````

---

## 7. Tests du labo

```python
assert find_maximum_split("ababccc") == 5  # ex : "a","b","ab","c","cc"
assert find_maximum_split("aba") == 2      # ex : "a","ab"
assert find_maximum_split("aa") == 1       # ex : "aa"
```

---

## 8. Points importants à retenir

* On découpe `s` avec un **backtracking** classique sur les indices.
* On garde les sous-chaînes déjà utilisées dans un **set** pour garantir l’unicité.
* On maximise le nombre de morceaux obtenus.
* On ajoute un pruning simple pour éviter les branches clairement perdantes.

---

# Conclusion

Ce problème illustre très bien :

* la logique de **backtracking** (choix → récursion → retour en arrière),
* l’usage d’un **ensemble** pour gérer des contraintes de type “unique”,
* un premier exemple de **Branch and Bound** pour accélérer la recherche.


