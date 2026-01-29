

# **Clique Detection — Recherche de cliques dans un graphe**

La **détection de cliques** consiste à identifier des sous-ensembles de sommets d’un graphe tels que **chaque paire de sommets est directement connectée**.

Une clique représente un groupe **totalement interconnecté**.

---

## 1. **Définition**

Soit un graphe non orienté `G = (V, E)`.

Une **clique de taille k** est un ensemble de sommets `{v₁, v₂, …, vₖ}` tel que :

```
∀ i ≠ j : (vᵢ, vⱼ) ∈ E
```

Autrement dit :

> tous les sommets de la clique sont voisins deux à deux.

Exemples :

* une clique de taille 2 = une arête
* une clique de taille 3 = un triangle
* une clique de taille n = sous-graphe complet

---

## 2. **Types de problèmes de clique**

Il existe plusieurs variantes classiques :

| Problème                      | Question                                    |
| ----------------------------- | ------------------------------------------- |
| Clique d’existence            | Existe-t-il une clique de taille k ?        |
| Clique maximale               | Quelle est la plus grande clique possible ? |
| Clique maximale par inclusion | Une clique qu’on ne peut plus agrandir      |
| Comptage de cliques           | Combien de cliques de taille k existent ?   |

⚠️ Ces problèmes sont **NP-complets / NP-durs** en général.

---

## 3. **Quand utiliser cet algorithme ?**

On utilise la détection de cliques lorsque :

* on cherche un **groupe entièrement connecté**,
* on analyse des réseaux sociaux, de communication, ou de compatibilité,
* le graphe est **petit ou moyennement dense**,
* on accepte une **complexité exponentielle**.

Dans un contexte de labo / examen :

> On attend une **recherche par backtracking avec pruning**.

---

## 4. **Pourquoi BFS / DFS ne suffisent pas ?**

BFS et DFS permettent :

* d’explorer la connectivité,
* de trouver des composantes,
* de vérifier l’atteignabilité.

Mais une clique impose une contrainte **globale** :

> chaque nouveau sommet doit être connecté à **tous les sommets déjà choisis**.

👉 Il faut donc :

* tester des **combinaisons de sommets**,
* vérifier une condition sur **toutes les paires**,
* utiliser du **backtracking**.

---

## 5. **Idée principale (Backtracking)**

On construit progressivement une clique :

1. On maintient :

   * `current` : clique en cours de construction,
   * `candidates` : sommets encore possibles.
2. À chaque étape :

   * on choisit un sommet `v` dans `candidates`,
   * on l’ajoute à `current`,
   * on met à jour `candidates` :

     ```
     candidats = candidats ∩ voisins(v)
     ```
3. Si `len(current) == k` → clique trouvée.
4. Sinon, on continue récursivement.
5. On revient en arrière (backtracking).

---

## 6. **Pruning (indispensable)**

Sans pruning, la recherche est beaucoup trop lente.

### Pruning principal

Si :

```
len(current) + len(candidates) < k
```

alors :

> même en prenant tous les candidats, on ne peut pas atteindre k
> → on coupe la branche.

Ce simple test est **crucial**.

---

## 7. **Complexité**

* Dans le pire cas : **exponentielle**
* Le problème de clique est **NP-complet**
* Le pruning permet de résoudre des graphes de taille raisonnable

👉 C’est normal et attendu.

---

## 8. **Implémentation Python — Clique de taille k**

```python
def exists_clique_k(n, edges, k):
    """
    Détermine s'il existe une clique de taille k dans un graphe non orienté.
    
    n     : nombre de sommets (0..n-1)
    edges : liste d'arêtes [u, v]
    k     : taille recherchée
    """
    # -------------------------
    # Construire la liste d'adjacence
    # -------------------------
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # -------------------------
    # Backtracking
    # -------------------------
    def backtrack(current, candidates):
        # Si on a atteint la taille k
        if len(current) == k:
            return True

        # Pruning : impossible d'atteindre k
        if len(current) + len(candidates) < k:
            return False

        for v in list(candidates):
            # Nouveaux candidats = voisins communs
            new_candidates = candidates.intersection(adj[v])

            if backtrack(current + [v], new_candidates):
                return True

            # Retirer v des candidats (backtracking)
            candidates.remove(v)

        return False

    # Tous les sommets sont candidats au départ
    return backtrack([], set(range(n)))


def find_clique_k(n, edges, k):
    """
    Retourne une clique de taille k sous forme de liste triée,
    ou [] si aucune clique de cette taille n'existe.
    """

    # -------------------------
    # Construire la liste d'adjacence
    # -------------------------
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # -------------------------
    # Backtracking
    # -------------------------
    def backtrack(current, candidates):
        # Cas succès : clique complète
        if len(current) == k:
            return current.copy()

        # Pruning : impossible d'atteindre k
        if len(current) + len(candidates) < k:
            return None

        for v in list(candidates):
            # Nouveaux candidats = voisins communs
            new_candidates = candidates.intersection(adj[v])

            res = backtrack(current + [v], new_candidates)
            if res is not None:
                return res  # on propage la solution trouvée

            # Backtracking
            candidates.remove(v)

        return None

    # Lancer depuis tous les sommets
    result = backtrack([], set(range(n)))

    if result is None:
        return []
    return sorted(result)

```

---

## 9. **Exemple**

```python
n = 5
edges = [
    [0, 1], [0, 2], [1, 2],   # triangle (clique 3)
    [2, 3], [3, 4]
]

assert exists_clique_k(n, edges, 3) is True
assert exists_clique_k(n, edges, 4) is False
```

---

## 10. **Lien avec d’autres algorithmes**

La détection de cliques est liée à :

* **Backtracking**
* **Branch & Bound**
* **Exploration combinatoire**
* **Graphes denses**
* **Problèmes NP-complets**

Elle apparaît souvent **là où BFS/DFS échouent**.

---

## **Résumé**

* Une clique est un sous-graphe **entièrement connecté**.
* La détection de cliques est **NP-complète**.
* On utilise du **backtracking avec pruning**.
* BFS/DFS ne suffisent pas.
* Le test `|current| + |candidates| < k` est essentiel.
* Très classique en examen pour tester :

  * raisonnement,
  * complexité,
  * choix de l’algorithme.
