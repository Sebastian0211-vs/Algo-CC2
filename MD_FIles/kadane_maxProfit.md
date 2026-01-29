# Algorithme de Kadane – Maximum Subarray / Maximum Profit

## 1. Intuition générale

L’algorithme de **Kadane** permet de trouver **le sous-tableau contigu ayant la plus grande somme** dans un tableau d’entiers.  
C’est l’un des algorithmes linéaires les plus connus en programmation dynamique.

Dans le cadre du labo (*We’re rich !*), tu reçois une liste `price_history` contenant les **variations journalières** d’un prix.  
L’objectif est de trouver le **profit maximal possible**, c’est-à-dire la somme maximale d’une sous-séquence contiguë de deltas.

Exemple :  
[0, 3, -10, -5, 10] → meilleure période = [-5, 10], profit = 5 + 10 = 10.

Kadane résout ce problème **en O(n)** naturellement.

---

## 2. Quand utiliser Kadane ?

Tu utilises Kadane lorsque :

- tu veux déterminer la **meilleure période continue** pour maximiser une somme ;  
- tu analyses un phénomène composé de **variations** successives (profits, températures, signaux, deltas) ;  
- tu dois répondre à un problème du type :  
  « Trouver la somme maximale d’un sous-tableau contigu ».

Dans ce labo, Kadane s’applique directement à :

- `max_profit(price_history)`

---

## 3. Idée de l’algorithme

On parcourt le tableau en construisant deux valeurs :

1. **current_sum** : la meilleure somme possible **en terminant exactement à l’indice i**  
   - Si `current_sum + x` devient négatif, on repart à 0 (car aucune bonne sous-séquence ne commencerait avec une somme négative).

2. **best_sum** : la plus grande somme rencontrée jusqu’ici.

Règles :

- `current_sum = max(x, current_sum + x)`  
- `best_sum = max(best_sum, current_sum)`

C’est un cas typique de **programmation dynamique** :  
la solution optimale au rang `i` dépend uniquement de la solution optimale au rang `i-1`.

---

## 4. Complexité

- **Temps : O(n)**  
Un seul passage dans le tableau.

- **Mémoire : O(1)**  
On ne stocke que deux variables.

---

## 5. Implémentation Python (version classique de Kadane)

```python
def max_profit(price_history):
    """
    Retourne la somme maximale d'un sous-tableau contigu.
    Implémentation complète de l'algorithme de Kadane.
    """
    current_sum = 0
    best_sum = float('-inf')
    
    for delta in price_history:
        # Étendre ou recommencer
        current_sum = max(delta, current_sum + delta)
        # Mettre à jour le meilleur résultat global
        best_sum = max(best_sum, current_sum)
    
    return best_sum
````

---

## 6. Vérifications

```python
assert max_profit([0, 3, -10, -5, 10]) == 10
assert max_profit([3, 5, -10, 15, -10, 7]) == 15
assert max_profit([-1, -2, -3]) == -1     # marche aussi pour tout négatif
assert max_profit([5, -1, 5]) == 9
```

---

## 7. Pourquoi Kadane est optimal ?

Kadane repose sur une propriété simple :
si la somme courante devient négative, il est **toujours suboptimal** de la conserver, car ajouter cette somme négative au futur réduit nécessairement la possibilité d’obtenir un meilleur résultat.

Cette vision permet de réduire un problème potentiellement quadratique (tous sous-tableaux) à un passage linéaire.

---

# Conclusion

Kadane est l’un des algorithmes fondamentaux en analyse de séquences, à connaître par cœur.
Dans ce labo, il fournit la solution optimale pour déterminer le profit maximal à partir d'une série de variations de prix.

