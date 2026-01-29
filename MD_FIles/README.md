# 📚 Algorithmes – Index Complet

Bienvenue dans ta **bibliothèque d’algorithmes**.
Ce dépôt regroupe les **algorithmes fondamentaux** vus en cours et en pratique, organisés par **thématique** et **paradigme algorithmique**.

Chaque fichier `.md` :

* explique **quand utiliser l’algorithme**,
* détaille **l’idée clé**,
* fournit une **implémentation claire**,
* met en avant les **liens avec d’autres algorithmes**.

---

## 🧭 Navigation Rapide

* [Graphes – Fondamentaux](#-graphes--fondamentaux)
* [Graphes – Plus courts chemins](#-graphes--plus-courts-chemins)
* [Graphes – Propriétés & Analyse](#-graphes--propriétés--analyse)
* [Arbres](#-arbres)
* [Greedy](#-greedy)
* [Programmation Dynamique & Optimisation](#-programmation-dynamique--optimisation)
* [Backtracking](#-backtracking)
* [Grilles & Recherche 2D](#-grilles--recherche-2d)
* [Jeux & Exploration d’Espace](#-jeux--exploration-despace)
* [Problèmes Combinatoires / Branch & Bound](#-problèmes-combinatoires--branch--bound)
* [Outils & Patterns transversaux](#-outils--patterns-transversaux)

---

## 🌐 Graphes – Fondamentaux

### 1. [BFS.md](BFS.md)

Parcours en largeur – exploration niveau par niveau.

### 2. [DFS.md](DFS.md)

Parcours en profondeur – exploration, cycles, composantes.

### 3. [Shortest Path – Unweighted Graph.md](Shortest Path – Unweighted Graph.md)

Plus courts chemins dans un graphe non pondéré (BFS).

### 4. [Flood Fill.md](Flood Fill.md)

DFS/BFS appliqué aux grilles – remplissage de zones connexes.

### 5. [Counting Ships.md](Counting Ships.md)

Détection de composantes connexes dans une grille.

---

## 🚦 Graphes – Plus courts chemins

### 1. [Dijkstra.md](Dijkstra.md)

Plus courts chemins avec poids positifs.

### 2. [0-1 BFS.md](0-1 BFS.md)

Plus courts chemins avec poids 0 ou 1 (deque).

### 3. [Bellman-Ford.md](Bellman-Ford.md)

Poids négatifs + détection de cycles négatifs.

### 4. [Floyd-Warshall.md](Floyd-Warshall.md)

Plus courts chemins entre **toutes les paires**.

### 5. [Minimum Effort Path – Dijkstra Minimax.md](Minimum Effort Path – Dijkstra Minimax.md)

Minimisation du maximum d’arête (minimax path).

---

## 🧠 Graphes – Propriétés & Analyse

### 1. [check_if_biparti.md](check_if_biparti.md)

Test de bipartition (coloration 2 couleurs).

### 2. [Cycle Detection.md](Cycle Detection.md)

Détection de cycles (graphes orientés / non orientés).

### 3. [Topological Sort.md](Topological%20Sort.md)

Ordonnancement de dépendances (DAG).

### 4. [Strongly Connected Components.md](Strongly Connected Components.md)

SCC – Kosaraju & Tarjan.

### 5. [Avalanche Chain Reaction.md](Avalanche Chain Reaction.md)

Propagation et reachability dans un graphe dirigé.

---

## 🌲 Arbres

### 1. [Diameter of a tree.md](Diameter of a tree.md)

Calcul du diamètre via double BFS/DFS.

### 2. [MST.md](MST.md)

Arbre couvrant minimal – Prim & Kruskal.

### 3. [Union Find (Disjoint Set Union).md](Union%20Find%20%28Disjoint%20Set%20Union%29.md)

Gestion de composantes disjointes (DSU).

### 4. [Lowest Common Ancestor.md](Lowest Common Ancestor.md)

LCA par binary lifting.

### 5. [Digitec – Livraison au jour même.md](Digitec – Livraison au jour même.md)

Pruning d’arbre + distance maximale autorisée.

---

## ⚡ Greedy

### 1. [Greedy Algorithms.md](Greedy Algorithms.md)

Paradigme glouton – principes et limites.

### 2. [Goose Game.md](Goose Game.md)

Jump Game II – minimisation du nombre de sauts.

---

## 🧮 Programmation Dynamique & Optimisation

### 1. [fibonacci.md](fibonacci.md)

DP, optimisation mémoire, fast doubling.

### 2. [kadane_maxProfit.md](kadane_maxProfit.md)

Algorithme de Kadane – sous-tableau maximal.

---

## 🔍 Backtracking

### 1. [Combinations.md](Combinations.md)

Combinaisons dont la somme atteint un target.

### 2. [MaxUniqueSplit.md](MaxUniqueSplit.md)

Découpage maximal d’une chaîne en sous-chaînes uniques.

---

## 🧱 Grilles & Recherche 2D

### 1. [Flood Fill.md](Flood Fill.md)

DFS/BFS appliqué aux matrices 2D.

---

## 🎮 Jeux & Exploration d’Espace

### 1. [Tic-tac-toe.md](Tic-tac-toe.md)

Exploration complète de l’espace de jeu.

### 2. [Minimax & Alpha-Beta Pruning.md](Minimax & Alpha-Beta Pruning.md)

Décision optimale dans les jeux adversariaux.

---

## 🧠 Problèmes Combinatoires / Branch & Bound

### 1. [Best Organization.md](Best Organization.md)

Répartition optimale de tâches – Branch & Bound.

---

## 🧰 Outils & Patterns transversaux

### 1. [Path Reconstruction.md](Path Reconstruction.md)

Reconstruction d’un chemin optimal (BFS, Dijkstra, etc.).

### 2. [Binary Search – Patterns.md](Binary Search – Patterns.md)

Recherche binaire sur tableaux et espace des réponses.

### 3. [Two Pointers & Sliding Window.md](Two Pointers & Sliding Window.md)

Optimisation linéaire sur tableaux et chaînes.

---

## 📌 Conseils d’utilisation

* Utilise ce README comme **panneau de navigation principal**.
* Identifie d’abord la **nature du problème** :

  * graphe, arbre, grille, jeu, séquence…
* Puis choisis le **paradigme** :

  * BFS / DFS / Greedy / DP / Backtracking.
* Les fichiers sont conçus pour être :

  * relus avant un examen,
  * réutilisés comme templates,
  * comparés entre eux.
