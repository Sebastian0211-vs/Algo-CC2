# ⏱️ Complexity Cheat Sheet – Analyse de complexité (Big-O)

Ce fichier sert de **référence rapide** pour analyser la **complexité temporelle et spatiale**
des algorithmes classiques.

Objectif :

> reconnaître rapidement un **ordre de grandeur**,
> le **justifier**,
> et éviter les erreurs classiques en examen.

---

## 🔹 Rappels essentiels

La notation **Big-O** décrit :

* le **pire cas**,
* le comportement quand `n → ∞`,
* en ignorant les constantes.

Ordre de croissance (du meilleur au pire) :

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

---

## 🔁 Boucles classiques

### Boucle simple

```python
for i in range(n):
    ...
```

➡ **O(n)**

---

### Boucles imbriquées indépendantes

```python
for i in range(n):
    for j in range(n):
        ...
```

➡ **O(n²)**

---

### Boucles dépendantes

```python
for i in range(n):
    for j in range(i):
        ...
```

➡ **O(n²)**
(moyenne ≈ n²/2 → Big-O reste n²)

---

### Boucle logarithmique

```python
i = n
while i > 1:
    i //= 2
```

➡ **O(log n)**

---

## 🔍 Recherche

| Méthode                             | Complexité      |
| ----------------------------------- | --------------- |
| Recherche linéaire                  | O(n)            |
| Recherche binaire                   | O(log n)        |
| Recherche avec hash (`set`, `dict`) | O(1) en moyenne |

---

## 🌐 Graphes

Soit :

* `V` = nombre de sommets
* `E` = nombre d’arêtes

### BFS / DFS

➡ **O(V + E)**

Pourquoi :

* chaque sommet est visité une fois,
* chaque arête est explorée au plus une fois.

---

### Dijkstra (heap)

➡ **O((V + E) log V)**
(souvent noté **O(E log V)**)

---

### Bellman-Ford

➡ **O(V · E)**

---

### Floyd-Warshall

➡ **O(V³)**

---

### Topological Sort

➡ **O(V + E)**

---

## 🌲 Arbres

### Parcours (DFS/BFS)

➡ **O(n)**

---

### Diamètre d’un arbre (double BFS)

➡ **O(n)**

---

### LCA (Binary Lifting)

| Phase         | Complexité |
| ------------- | ---------- |
| Prétraitement | O(n log n) |
| Requête       | O(log n)   |

---

### Union-Find (DSU)

| Opération    | Complexité             |
| ------------ | ---------------------- |
| find / union | **O(α(n))** ≈ constant |

(α = fonction d’Ackermann inverse)

---

## ⚡ Greedy

Souvent dominé par un tri :

➡ **O(n log n)**

Exemples :

* Interval Scheduling
* Kruskal
* Goose Game

---

## 🧮 Programmation Dynamique (DP)

### DP 1D

```python
dp = [0] * n
```

➡ **Temps : O(n)**
➡ **Mémoire : O(n)**

---

### DP 2D

```python
dp = [[0]*m for _ in range(n)]
```

➡ **Temps : O(n·m)**
➡ **Mémoire : O(n·m)**

---

### DP avec états compressés

➡ **O(n · 2ⁿ)**
(utilisé quand `n ≤ 20`)

---

## 🔍 Backtracking

Complexité souvent **exponentielle**.

| Problème                     | Complexité        |
| ---------------------------- | ----------------- |
| Génération de sous-ensembles | O(2ⁿ)             |
| Permutations                 | O(n!)             |
| Combinaisons                 | dépend du pruning |

⚠️ Le **pruning** réduit le temps **en pratique**,
mais pas le pire cas théorique.

---

## 🎮 Jeux & Minimax

### Minimax naïf

➡ **O(bᵈ)**

* `b` = facteur de branchement
* `d` = profondeur

---

### Alpha-Beta Pruning (idéal)

➡ **O(b^(d/2))**

Permet de **doubler la profondeur explorée**.

---

## 🧠 Astuces d’examen

* Un `set` ou `dict` ⇒ souvent **O(1)** attendu
* BFS sur graphe non pondéré ⇒ **O(V + E)** (pas Dijkstra)
* Tri presque toujours ⇒ **O(n log n)**
* DP = **taille du tableau**
* Backtracking = **exponentiel par défaut**

---

## ❌ Erreurs fréquentes

* Dire `O(n)` au lieu de `O(V + E)`
* Oublier le `log n` du heap
* Sous-estimer un backtracking
* Compter des constantes inutiles

---

# Conclusion

Savoir **coder** un algorithme est important.
Savoir **justifier sa complexité** est indispensable.

Ce fichier doit te permettre de :

* reconnaître un schéma,
* annoncer un Big-O crédible,
* et le défendre clairement à l’écrit comme à l’oral.

