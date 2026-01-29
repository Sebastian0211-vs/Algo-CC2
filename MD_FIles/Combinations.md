
# Combinations – Trouver toutes les décompositions d’un total (Backtracking)

## 1. Intuition générale

On reçoit :
- une liste de contenants (par exemple des éprouvettes graduées),
- un **target** représentant la quantité exacte à obtenir.

On doit retourner **toutes les combinaisons possibles** de contenants dont la somme est égale au target.

Exemple du labo :

```python
containers = [2, 3, 6, 7]
target = 7
res = [[2, 2, 3], [7]]
````

Il s’agit d’un problème classique de **backtracking avec somme**.

---

## 2. Quand utiliser cet algorithme ?

On utilise ce type d’algorithme lorsque :

* on doit générer **toutes** les combinaisons possibles qui satisfont une contrainte numérique ;
* l’ordre des éléments **n’a pas d’importance** (une combinaison `[2,3,2]` est la même que `[2,2,3]`) ;
* on veut éviter les doublons en explorant les possibilités **dans un ordre croissant**.

Dans ton labo, il s’applique à :

* `combinations(containers, target)`

---

## 3. Idée principale (Backtracking)

1. Trier les contenants (permet d’éviter les doublons et de garder les combinaisons ordonnées).
2. Explorer récursivement :

   * à chaque étape, on peut choisir d’utiliser un contenant donné **autant de fois que l’on veut**,
   * tant que la somme ne dépasse pas le target.
3. Si on atteint exactement le target → on ajoute la combinaison actuelle à la solution.
4. Si la somme dépasse → on arrête immédiatement la branche.

**Important :**
Contrairement à un backtracking classique, l’indice `i` n’avance pas forcément :

* On peut réutiliser plusieurs fois `containers[i]`,
* Mais pour éviter les doublons, on ne revient **jamais** aux éléments précédents.

---

## 4. Complexité

* La complexité est **exponentielle** dans le pire cas (génération de toutes les combinaisons).
* Le backtracking avec tri et ordre croissant limite largement les doublons.

---

## 5. Implémentation Python (Backtracking propre)

```python
def combinations(containers, target):
    """
    Retourne toutes les combinaisons de 'containers' dont la somme vaut 'target'.
    Basé sur un backtracking avec répétitions autorisées.
    """
    containers = sorted(containers)
    result = []
    current = []

    def backtrack(start_index, remaining):
        # Si on a atteint exactement le target
        if remaining == 0:
            result.append(current.copy())
            return

        # Si la somme dépasse, on coupe la branche
        if remaining < 0:
            return

        # Explorer tous les choix possibles à partir de start_index
        for i in range(start_index, len(containers)):
            value = containers[i]

            # Si le contenant dépasse le besoin restant, inutile d'aller plus loin
            if value > remaining:
                break

            # Choisir ce contenant
            current.append(value)
            # Rester sur i pour pouvoir réutiliser le même contenant
            backtrack(i, remaining - value)
            # Backtrack
            current.pop()

    backtrack(0, target)
    return result
```

---

## 6. Tests du labo

```python
containers = [2, 3, 6, 7]
target = 7
assert combinations(containers, target) == [[2, 2, 3], [7]]

containers = [2, 3, 5]
target = 8
assert combinations(containers, target) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
```

---

## 7. Pourquoi le backtracking est correct ici ?

* On essaye systématiquement toutes les possibilités mais :

  * **dans un ordre trié**,
  * **sans jamais revenir en arrière sur les indices**,
  * ce qui garantit **absence de doublons**.
* Chaque branche ne génère qu'une seule combinaison potentielle.
* Le test `value > remaining` coupe énormément de branches dès que possible.

Ce problème représente un cas standard de **recherche exhaustive intelligemment structurée**, un fondamental des compétitions d’algo.

---

# Conclusion

Le problème des combinaisons pour atteindre un total cible est un exemple clair de backtracking à choix multiples avec répétitions autorisées.
L’implémentation est élégante, efficace, et grâce au tri initial + backtracking contrôlé, elle produit toutes les solutions sans doublons.

