# 🧭 Guide de Décision – Comment choisir le bon algorithme

Ce fichier fournit une **méthode systématique** pour analyser un problème algorithmique
et **choisir rapidement l’approche adaptée**.

Objectif :

> éviter le hasard,
> éviter les mauvais algorithmes,
> et **justifier son choix** en examen ou à l’oral.

---

## 1️⃣ Étape 1 – Identifier la structure du problème

Pose toujours **cette question en premier** :

> **Sur quoi porte le problème ?**

### Cas possibles

| Structure        | Indices                         |
| ---------------- | ------------------------------- |
| Tableau / chaîne | indices, sous-tableaux          |
| Graphe           | sommets, arêtes, connexions     |
| Arbre            | racine, ancêtre, enfants        |
| Grille 2D        | matrice, voisins                |
| Jeu              | tours, adversaire               |
| Combinaisons     | générer toutes les possibilités |

---

## 2️⃣ Étape 2 – Identifier l’objectif

> **Que cherche-t-on exactement ?**

| Objectif       | Mot-clés                   |
| -------------- | -------------------------- |
| Chemin minimal | shortest, minimum distance |
| Atteignabilité | reachable, propagation     |
| Optimisation   | minimum / maximum          |
| Comptage       | combien de                 |
| Décision       | est-ce possible            |
| Génération     | toutes les solutions       |

---

## 3️⃣ Étape 3 – Si c’est un GRAPHE

### 🔹 Chemins les plus courts

| Situation          | Algorithme           |
| ------------------ | -------------------- |
| Graphe non pondéré | **BFS**              |
| Poids ∈ {0,1}      | **0–1 BFS**          |
| Poids positifs     | **Dijkstra**         |
| Poids négatifs     | **Bellman–Ford**     |
| Toutes paires      | **Floyd–Warshall**   |
| Minimiser le max   | **Minimax Dijkstra** |

---

### 🔹 Structure du graphe

| Problème            | Algorithme             |
| ------------------- | ---------------------- |
| Biparti ?           | BFS / DFS + coloration |
| Cycle (orienté)     | DFS (couleurs)         |
| Cycle (non orienté) | DFS / Union-Find       |
| Dépendances         | Topological sort       |
| Composantes SCC     | Kosaraju / Tarjan      |
| MST                 | Kruskal / Prim         |

---

## 4️⃣ Étape 4 – Si c’est un ARBRE

| Problème           | Algorithme |
| ------------------ | ---------- |
| Distance max       | Diamètre   |
| Ancêtre commun     | LCA        |
| Connexion minimale | MST        |
| Recherche          | DFS / BFS  |

Rappel :

> Un arbre = graphe **sans cycle**.

---

## 5️⃣ Étape 5 – Si c’est un TABLEAU / CHAÎNE

### 🔹 Sous-tableaux / sous-chaînes

| Objectif         | Algorithme     |
| ---------------- | -------------- |
| Somme maximale   | Kadane         |
| Fenêtre fixe     | Sliding Window |
| Fenêtre variable | Two Pointers   |
| Unicité          | Set + window   |

---

### 🔹 Recherche

| Cas              | Algorithme              |
| ---------------- | ----------------------- |
| Tableau trié     | Binary Search           |
| Réponse monotone | Binary Search on Answer |

---

## 6️⃣ Étape 6 – Si c’est une GRILLE

> Grille = graphe implicite

| Problème      | Algorithme       |
| ------------- | ---------------- |
| Connexité     | DFS / BFS        |
| Distance      | BFS              |
| Multi-sources | Multi-source BFS |
| Propagation   | BFS              |
| Zones         | Flood Fill       |

---

## 7️⃣ Étape 7 – Si c’est une OPTIMISATION

Pose la question clé :

> **Puis-je faire un choix local sans regret ?**

### Oui → Greedy

### Non → DP ou Backtracking

---

### 🔹 Greedy

Utiliser si :

* un choix local est optimal,
* pas besoin de revenir en arrière.

Exemples :

* Interval Scheduling
* Dijkstra
* Kruskal
* Goose Game

---

### 🔹 Programmation Dynamique

Utiliser si :

* sous-problèmes qui se recouvrent,
* dépendance sur des états précédents.

Indices :

* “maximum”, “minimum”
* dépend de i-1, i-2, …

---

### 🔹 Backtracking / Branch & Bound

Utiliser si :

* générer toutes les solutions,
* contraintes fortes,
* n petit.

Exemples :

* Combinations
* MaxUniqueSplit
* Best Organization

---

## 8️⃣ Étape 8 – Jeux et adversaires

| Situation       | Algorithme           |
| --------------- | -------------------- |
| Jeu à 2 joueurs | Minimax              |
| Trop lent       | Alpha-Beta pruning   |
| Évaluation      | fonction heuristique |

---

## 9️⃣ Étape 9 – Vérifier la complexité

Toujours vérifier :

| Si n ≈ | Autorisé         |
| ------ | ---------------- |
| 10⁵    | O(n), O(n log n) |
| 10⁴    | O(n²) limite     |
| 20     | O(2ⁿ)            |
| 10     | O(n!)            |

---

## 🔁 Résumé express (exam mode)

```
Graphe + distance → BFS / Dijkstra
Arbre + ancêtre → LCA
Sous-tableau → Sliding Window / Kadane
Optimisation → Greedy ou DP
Génération → Backtracking
Adversaire → Minimax
```

---

# Conclusion

Un bon algorithme **ne se devine pas**.
Il se **déduit logiquement** à partir :

1. de la structure,
2. de l’objectif,
3. des contraintes.

Si tu suis ce guide étape par étape,
tu choisis **le bon algorithme presque à coup sûr**.

