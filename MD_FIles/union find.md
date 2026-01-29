# Union-Find – Disjoint Set Union (DSU)

## 1. Intuition générale

On a un ensemble d’éléments, et on veut répondre efficacement à deux types de questions :

* **Est-ce que deux éléments appartiennent au même groupe ?**
* **Fusionner deux groupes**

L’algorithme **Union-Find** (ou **Disjoint Set Union – DSU**) permet de gérer dynamiquement des **ensembles disjoints**.

Chaque élément appartient à **exactement un ensemble**, et ces ensembles peuvent être fusionnés au fil du temps.

---

## 2. Quand utiliser Union-Find ?

Tu utilises Union-Find lorsque :

* tu dois gérer des **groupes qui fusionnent** ;
* tu dois tester rapidement la **connectivité** entre deux éléments ;
* les opérations sont nombreuses et doivent être très rapides.

Cas typiques :

* détection de cycles dans un graphe,
* algorithme de **Kruskal** (MST),
* regroupement de composantes connexes,
* problèmes de connectivité dynamique.

---

## 3. Idée principale

Chaque ensemble est représenté par un **arbre** :

* chaque nœud pointe vers un **parent**,
* la racine de l’arbre est le **représentant** de l’ensemble.

Deux opérations fondamentales :

1. **find(x)**
   → trouver le représentant (racine) de l’ensemble contenant `x`.

2. **union(x, y)**
   → fusionner les ensembles contenant `x` et `y`.

---

## 4. Optimisations essentielles

Sans optimisation, Union-Find peut devenir lent.

Deux techniques rendent les opérations **quasi constantes** :

### 4.1 Compression de chemin

Lors d’un `find(x)`,
on fait pointer directement `x` vers la racine de son ensemble.

Résultat :

* les arbres deviennent presque plats,
* les futurs `find` sont plus rapides.

---

### 4.2 Union par rang (ou taille)

Lors d’une fusion :

* on accroche l’arbre **le plus petit** sous le plus grand.

Cela limite la hauteur des arbres.

---

## 5. Implémentation Python (DSU optimisé)

```python
class UnionFind:
    def __init__(self, n):
        """
        Initialise n ensembles disjoints : {0}, {1}, ..., {n-1}
        """
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """
        Trouve le représentant de l'ensemble contenant x
        avec compression de chemin.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Fusionne les ensembles contenant x et y.
        Retourne True si la fusion a eu lieu, False sinon.
        """
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False  # déjà dans le même ensemble

        # Union par rang
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        return True
```

---

## 6. Exemple d’utilisation

### Détection de cycle dans un graphe non orienté

```python
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 1)  # crée un cycle
]

uf = UnionFind(4)

cycle = False
for u, v in edges:
    if not uf.union(u, v):
        cycle = True
        break

print(cycle)  # True
```

---

## 7. Union-Find et Kruskal (MST)

Dans l’algorithme de Kruskal :

1. on trie les arêtes par poids croissant,
2. pour chaque arête `(u, v)` :

   * si `find(u) != find(v)` → on l’ajoute au MST,
   * sinon → elle créerait un cycle, on l’ignore.

Union-Find rend cette vérification **ultra rapide**.

---

## 8. Complexité

Avec compression de chemin + union par rang :

* **Temps amorti** par opération :
  **O(α(n))**, où α est la fonction d’Ackermann inverse
  → **pratiquement constant**

* **Mémoire** : O(n)

---

## 9. Points à retenir

* Union-Find gère des **ensembles disjoints dynamiques**.
* Les opérations clés sont `find` et `union`.
* Avec les optimisations, c’est l’une des structures les plus rapides en pratique.
* Indispensable pour :

  * MST (Kruskal),
  * détection de cycles,
  * connectivité dynamique.

---

# Conclusion

Union-Find est une structure simple mais extrêmement puissante.
Dès que tu dois fusionner des groupes ou tester des connexions répétées,
c’est l’outil naturel à utiliser.
