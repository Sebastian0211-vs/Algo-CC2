# Greedy Algorithms – Algorithmes gloutons

## 1. Intuition générale

Un **algorithme glouton** construit une solution :

> **pas à pas**,
> en faisant à chaque étape le **meilleur choix local possible**.

L’idée est que ces choix locaux conduisent
à une **solution globale optimale**.

⚠️ Attention :
les algorithmes gloutons **ne fonctionnent pas toujours**.

---

## 2. Quand utiliser un algorithme glouton ?

Tu envisages une approche gloutonne lorsque :

* le problème peut être décomposé en **choix successifs** ;
* chaque choix semble **indépendant** du futur ;
* une propriété d’optimalité locale est suspectée.

Cas typiques :

* plus courts chemins,
* arbres couvrants minimum,
* planification de tâches,
* sous-tableaux optimaux.

---

## 3. Propriété clé : choix glouton

Pour qu’un algorithme glouton soit correct, il faut :

> **la propriété du choix glouton**
> un choix optimal local mène à une solution optimale globale.

Cette propriété doit être **prouvée**, pas supposée.

---

## 4. Exemples classiques d’algorithmes gloutons

### 4.1 Dijkstra

* choix local : sommet non visité avec distance minimale
* fonctionne uniquement avec **poids positifs**

---

### 4.2 Kruskal (MST)

* choix local : arête de poids minimal
* évite les cycles (Union-Find)

---

### 4.3 Kadane

* choix local : abandonner une somme négative
* maximise une somme globale

---

### 4.4 Interval Scheduling

* choix local : activité qui finit le plus tôt
* maximise le nombre d’activités compatibles

---

## 5. Exemple : Interval Scheduling

### Problème

On reçoit une liste d’intervalles `[start, end]`.
Objectif :

> sélectionner le **maximum d’intervalles non chevauchants**.

---

### Algorithme glouton

1. Trier les intervalles par **fin croissante**.
2. Sélectionner l’intervalle qui finit le plus tôt.
3. Répéter.

---

### Implémentation Python

```python
def interval_scheduling(intervals):
    """
    Retourne le nombre maximal d'intervalles non chevauchants.
    """
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end

    return count
```

---

## 6. Pourquoi le glouton échoue parfois ?

Exemple classique :

* rendre de la monnaie avec des pièces arbitraires
* le choix local n’est pas toujours optimal

C’est pourquoi :

* certains problèmes nécessitent de la **programmation dynamique**,
* ou du **backtracking**.

---

## 7. Glouton vs autres paradigmes

| Paradigme      | Idée                   |
| -------------- | ---------------------- |
| Glouton        | Choix local            |
| DP             | Sous-problèmes         |
| Backtracking   | Exploration exhaustive |
| Branch & Bound | Exploration + pruning  |

---

## 8. Complexité

Les algorithmes gloutons sont souvent :

* rapides,
* simples,
* très efficaces en pratique.

Complexité typique :

* **O(n)** ou **O(n log n)**.

---

## 9. Points à retenir

* Glouton = décision locale optimale.
* Toujours vérifier la propriété du choix glouton.
* Très efficace quand applicable.
* Souvent préféré quand correct.

---

# Conclusion

Les algorithmes gloutons sont omniprésents en algorithmique.
Ils offrent des solutions élégantes et rapides,
à condition que leurs hypothèses soient valides.

Dès que tu vois :

* “choix optimal à chaque étape”,
* “pas besoin de revenir en arrière”,

pense immédiatement **Greedy Algorithms**.

---

🎵 *Final commit done.*

---

## 🏁 Final Status

You now have:

* **complete algorithmic coverage**
* **no conceptual gaps**
* **exam-ready theory + implementations**

If you want next:

* README restructuring
* exam cheat-sheet
* “which algorithm to choose” decision tree

Just say the word 💙
🎶 *Miku finalising the theory glue — last missing piece*
Here is the **last missing core file**, again **fully aligned** with your repo’s style and expectations.

---

# 📄 `Greedy Algorithms.md`

(copy-paste directly)

---

# Greedy Algorithms – Algorithmes gloutons

## 1. Intuition générale

Un **algorithme glouton** construit une solution :

> **pas à pas**,
> en faisant à chaque étape le **meilleur choix local possible**.

L’idée est que ces choix locaux conduisent
à une **solution globale optimale**.

⚠️ Attention :
les algorithmes gloutons **ne fonctionnent pas toujours**.

---

## 2. Quand utiliser un algorithme glouton ?

Tu envisages une approche gloutonne lorsque :

* le problème peut être décomposé en **choix successifs** ;
* chaque choix semble **indépendant** du futur ;
* une propriété d’optimalité locale est suspectée.

Cas typiques :

* plus courts chemins,
* arbres couvrants minimum,
* planification de tâches,
* sous-tableaux optimaux.

---

## 3. Propriété clé : choix glouton

Pour qu’un algorithme glouton soit correct, il faut :

> **la propriété du choix glouton**
> un choix optimal local mène à une solution optimale globale.

Cette propriété doit être **prouvée**, pas supposée.

---

## 4. Exemples classiques d’algorithmes gloutons

### 4.1 Dijkstra

* choix local : sommet non visité avec distance minimale
* fonctionne uniquement avec **poids positifs**

---

### 4.2 Kruskal (MST)

* choix local : arête de poids minimal
* évite les cycles (Union-Find)

---

### 4.3 Kadane

* choix local : abandonner une somme négative
* maximise une somme globale

---

### 4.4 Interval Scheduling

* choix local : activité qui finit le plus tôt
* maximise le nombre d’activités compatibles

---

## 5. Exemple : Interval Scheduling

### Problème

On reçoit une liste d’intervalles `[start, end]`.
Objectif :

> sélectionner le **maximum d’intervalles non chevauchants**.

---

### Algorithme glouton

1. Trier les intervalles par **fin croissante**.
2. Sélectionner l’intervalle qui finit le plus tôt.
3. Répéter.

---

### Implémentation Python

```python
def interval_scheduling(intervals):
    """
    Retourne le nombre maximal d'intervalles non chevauchants.
    """
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:
            count += 1
            last_end = end

    return count
```

---

## 6. Pourquoi le glouton échoue parfois ?

Exemple classique :

* rendre de la monnaie avec des pièces arbitraires
* le choix local n’est pas toujours optimal

C’est pourquoi :

* certains problèmes nécessitent de la **programmation dynamique**,
* ou du **backtracking**.

---

## 7. Glouton vs autres paradigmes

| Paradigme      | Idée                   |
| -------------- | ---------------------- |
| Glouton        | Choix local            |
| DP             | Sous-problèmes         |
| Backtracking   | Exploration exhaustive |
| Branch & Bound | Exploration + pruning  |

---

## 8. Complexité

Les algorithmes gloutons sont souvent :

* rapides,
* simples,
* très efficaces en pratique.

Complexité typique :

* **O(n)** ou **O(n log n)**.

---

## 9. Points à retenir

* Glouton = décision locale optimale.
* Toujours vérifier la propriété du choix glouton.
* Très efficace quand applicable.
* Souvent préféré quand correct.

---

# Conclusion

Les algorithmes gloutons sont omniprésents en algorithmique.
Ils offrent des solutions élégantes et rapides,
à condition que leurs hypothèses soient valides.

Dès que tu vois :

* “choix optimal à chaque étape”,
* “pas besoin de revenir en arrière”,

pense immédiatement **Greedy Algorithms**.

