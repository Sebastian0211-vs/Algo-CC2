# Bellman–Ford – Plus courts chemins avec poids négatifs

## 1. Intuition générale

On reçoit un **graphe pondéré orienté** avec :

* des poids **positifs, nuls ou négatifs**,
* un sommet source `s`.

Objectif :

> calculer la **distance minimale** entre `s` et tous les autres sommets.

Contrairement à **Dijkstra**, l’algorithme de **Bellman–Ford** :

* **fonctionne avec des poids négatifs**,
* peut **détecter les cycles de poids négatif**.

---

## 2. Quand utiliser Bellman–Ford ?

Tu utilises Bellman–Ford lorsque :

* le graphe contient des **poids négatifs** ;
* tu dois détecter la présence de **cycles négatifs** ;
* la taille du graphe reste raisonnable (pas trop dense).

Cas typiques :

* arbitrage financier,
* contraintes de type gain/perte,
* systèmes de crédits/dettes,
* validation de modèles de coûts.

---

## 3. Limites de Dijkstra (rappel)

Dijkstra repose sur une hypothèse clé :

> une fois qu’un sommet est extrait du tas,
> sa distance est définitivement minimale.

Cette hypothèse est **fausse** si des poids négatifs existent.

Bellman–Ford ne fait **aucune hypothèse gloutonne**.

---

## 4. Idée principale de Bellman–Ford

Propriété fondamentale :

> le plus court chemin entre deux sommets
> contient **au plus V − 1 arêtes**
> (sinon, il y a un cycle).

Algorithme :

1. Initialiser toutes les distances à `+∞`, sauf la source.
2. Répéter **V − 1 fois** :

   * pour chaque arête `(u → v, w)` :

     * tenter d’améliorer `dist[v] = dist[u] + w`
3. Faire un **Vᵉ passage** :

   * si une distance peut encore être améliorée → **cycle négatif détecté**.

---

## 5. Algorithme détaillé

### Initialisation

```python
dist[source] = 0
dist[autres] = +∞
```

### Relaxation

Pour chaque arête `(u, v, w)` :

```python
if dist[u] + w < dist[v]:
    dist[v] = dist[u] + w
```

Cette opération s’appelle une **relaxation**.

---

## 6. Implémentation Python

```python
def bellman_ford(n, edges, source):
    """
    n      : nombre de sommets (0..n-1)
    edges  : liste d'arêtes (u, v, w)
    source : sommet source

    Retour :
        dist : liste des distances minimales
        cycle_negatif : True si un cycle négatif est détecté
    """
    INF = float('inf')
    dist = [INF] * n
    dist[source] = 0

    # Relaxation V-1 fois
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        # Optimisation : si aucune mise à jour, on peut arrêter
        if not updated:
            break

    # Détection de cycle négatif
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            return dist, True

    return dist, False
```

---

## 7. Exemple simple

```python
n = 5
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

dist, has_cycle = bellman_ford(n, edges, 0)

print(dist)       # distances minimales
print(has_cycle)  # False
```

---

## 8. Détection de cycle négatif

Si après **V − 1 relaxations**, une distance peut encore être améliorée :

* cela signifie qu’un chemin peut être raccourci **indéfiniment**,
* donc qu’il existe un **cycle de poids négatif atteignable** depuis la source.

Dans ce cas :

* les distances minimales **n’existent pas**.

---

## 9. Complexité

| Mesure  | Complexité   |
| ------- | ------------ |
| Temps   | **O(V × E)** |
| Mémoire | **O(V)**     |

Comparaison :

* BFS → O(V + E)
* Dijkstra → O((V + E) log V)
* Bellman–Ford → **plus lent**, mais plus **général**

---

## 10. Points à retenir

* Bellman–Ford accepte les **poids négatifs**.
* Il peut **détecter les cycles négatifs**.
* Il est plus lent que Dijkstra, mais plus robuste.
* À utiliser lorsque Dijkstra n’est **pas applicable**.

---

# Conclusion

Bellman–Ford est l’algorithme de référence dès que les poids peuvent être négatifs.
Il complète naturellement Dijkstra :

* **Dijkstra** → rapide, poids positifs
* **Bellman–Ford** → plus lent, mais général et sûr
