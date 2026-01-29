
# Best Organization – Répartition de tâches (Branch & Bound pour minimiser le temps total)

## 1. Intuition générale

On reçoit :
- une liste `tasks` où chaque élément est la **durée** d’une tâche,
- un entier `n_workers` indiquant le **nombre de travailleurs** disponibles.

Chaque travailleur peut exécuter plusieurs tâches, **les unes après les autres**.  
Le temps total nécessaire pour terminer toutes les tâches est :

> le **temps de travail maximal** parmi tous les travailleurs  
> (aussi appelé *makespan*).

Objectif :

> Répartir les tâches entre les `n_workers` de façon à **minimiser ce temps maximal**.

Exemples du labo :

```python
tasks = [3, 2, 2]
n_workers = 3
res = 3     # chaque worker prend une tâche

tasks = [1, 2, 4, 7, 8]
n_workers = 2
res = 11    # meilleure répartition possible
````

C’est un problème classique de **partition / scheduling** difficile (NP-dur),
mais on peut le résoudre proprement avec **Branch & Bound** pour des tailles raisonnables.

---

## 2. Quand utiliser cette approche ?

On utilise ce schéma lorsque :

* on veut répartir des **jobs/tâches** sur des **ressources identiques** (machines, travailleurs),
* la durée totale de chaque ressource est la somme des tâches qui lui sont assignées,
* on veut **minimiser la durée du plus chargé** (makespan).

Exemples typiques :

* planification de tâches sur des CPU,
* répartition de commandes entre livreurs,
* équilibrage de charge.

Dans le labo, cela correspond à :

* `best_organization(tasks, n_workers)`

---

## 3. Idée principale (Branch & Bound)

On cherche une **affectation des tâches aux workers**.

### Représentation

* On garde un tableau `loads` de taille `n_workers` :
  `loads[i]` = temps total de travail du worker `i`.

### Stratégie

1. **Trier les tâches dans l’ordre décroissant** (les plus longues en premier).
   Cela permet un meilleur pruning (on fixe vite un bon upper bound).

2. On explore récursivement :

   * à l’étape `idx`, on affecte la tâche `tasks[idx]` à l’un des `n_workers`.
   * on met à jour `loads[worker] += tasks[idx]`.
   * on calcule le **temps maximal courant** = `max(loads)`.

3. On maintient un `best` (meilleur temps maximal trouvé jusqu’ici).

4. **Pruning (Bound) :**

   * Si le temps maximal courant est déjà ≥ `best`, cette branche ne peut pas faire mieux → on coupe.
   * Si on a affecté toutes les tâches, on met à jour `best`.

5. **Symétries** :

   * Si deux workers ont actuellement la même charge, les affectations symétriques sont équivalentes → on peut éviter des branches en doublon.

---

## 4. Complexité

* Le problème est **exponentiel** dans le pire cas.
* Mais :

  * tri des tâches en décroissant,
  * pruning agressif (bound),
  * gestion des symétries,

le rendent très efficace pour des instances de labo.

---

## 5. Implémentation Python (Branch & Bound)

```python
def best_organization(tasks, n_workers):
    """
    Répartit les tâches entre n_workers pour minimiser le temps de travail maximal.
    Retourne ce temps minimal (makespan).
    """
    # Trier les tâches décroissant pour améliorer le pruning
    tasks = sorted(tasks, reverse=True)
    loads = [0] * n_workers
    best = sum(tasks)  # upper bound trivial : tout chez un seul worker

    def backtrack(idx):
        nonlocal best

        # Si toutes les tâches ont été assignées
        if idx == len(tasks):
            current_max = max(loads)
            best = min(best, current_max)
            return

        task = tasks[idx]

        # Pour éviter des branches symétriques, on se souvient des charges déjà essayées
        seen_loads = set()

        for i in range(n_workers):
            # Symétrie : si un worker a déjà été essayé avec cette charge, on peut ignorer
            if loads[i] in seen_loads:
                continue
            seen_loads.add(loads[i])

            # Assigner la tâche au worker i
            loads[i] += task
            current_max = max(loads)

            # Pruning : si on dépasse déjà le meilleur trouvé, on coupe
            if current_max < best:
                backtrack(idx + 1)

            # Backtrack
            loads[i] -= task

            # Optimisation : si ce worker n'avait rien et qu'on vient de lui enlever la tâche,
            # cela signifie que les autres workers libres se comporteront pareil → on peut arrêter.
            if loads[i] == 0:
                break

    backtrack(0)
    return best
```

---

## 6. Tests du labo

```python
tasks = [3, 2, 2]
n_workers = 3
res = best_organization(tasks, n_workers)
assert res == 3

tasks = [1, 2, 4, 7, 8]
n_workers = 2
res = best_organization(tasks, n_workers)
assert res == 11
```

---

## 7. Points importants à retenir

* On travaille avec un tableau `loads` = charges des workers.
* On assigne les tâches **une par une**, en choisissant un worker à chaque étape.
* On utilise :

  * tri décroissant des tâches,
  * pruning sur le `max(loads)` vs `best`,
  * élimination des symétries via `seen_loads`.

Ce problème est un très bon exemple de **Branch & Bound** appliqué à un problème NP-dur de manière efficace pour des instances réalistes.

---

# Conclusion

`best_organization` illustre une stratégie puissante :

* modéliser les affectations comme un arbre de recherche,
* et couper toutes les branches qui ne peuvent pas battre la meilleure solution courante.

Ce pattern est très utile à connaître pour une large classe de problèmes d'optimisation combinatoire.

