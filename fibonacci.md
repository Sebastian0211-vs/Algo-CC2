# Fibonacci – Approches efficaces (DP, mémoïsation, fast doubling)

## 1. Contexte du problème

La suite de Fibonacci est définie par :
- F(0) = 0  
- F(1) = 1  
- F(n) = F(n-1) + F(n-2)

Bien que simple, cette suite met rapidement en évidence les limites des approches naïves, notamment la version récursive pure, qui explose en complexité.

Ce document présente **les méthodes efficaces recommandées**, leur logique et un exemple d’implémentation en Python.

---

## 2. Quand utiliser Fibonacci ?

Ces techniques sont utiles lorsque :
- tu veux calculer F(n) pour **n potentiellement très grand** (jusqu’à n ≈ 10⁵ ou plus)  
- tu dois comparer différentes **approches de programmation dynamique**  
- tu analyses l’impact des optimisations sur des **recursions linéaires**

Pour le labo, la méthode demandée doit être **efficace** et capable de renvoyer F(119) instantanément.

---

## 3. Trois approches efficaces

### 3.1 Programmation dynamique (tabulation)
**Idée :**  
On construit un tableau `dp` en partant de F(0) et F(1), puis on remplit jusqu’à F(n).

**Avantages :**
- Très lisible  
- Complexité optimale pour une suite linéaire

**Complexité :**
- Temps : O(n)  
- Mémoire : O(n)

---

### Implémentation (tabulation)

```python
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]
````

---

### 3.2 Optimisation mémoire (deux variables)

**Idée :**
Pour F(n), on n’a besoin que des deux valeurs précédentes → inutile de stocker tout le tableau.

**Complexité :**

* Temps : O(n)
* Mémoire : O(1)

---

### Implémentation (mémoire O(1))

```python
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    
    a, b = 0, 1  # F(0), F(1)
    
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
```

---

### 3.3 Fast Doubling (méthode optimale, O(log n))

**Idée :**
Utilise des identités mathématiques pour calculer F(n) en divisant n par 2 :

* F(2k)   = F(k) * [2*F(k+1) − F(k)]
* F(2k+1) = F(k+1)² + F(k)²

On calcule simultanément F(n) et F(n+1).
Cette méthode est la plus rapide et la plus robuste pour de très grands n.

**Complexité :**

* Temps : O(log n)
* Mémoire : O(log n) (profondeur récursive)

---

### Implémentation (fast doubling)

```python
def fibonacci(n: int) -> int:
    def fib_fast(k):
        # Retourne (F(k), F(k+1))
        if k == 0:
            return (0, 1)
        
        f_k, f_k1 = fib_fast(k // 2)
        
        # Formules du fast doubling
        c = f_k * (2 * f_k1 - f_k)          # F(2k)
        d = f_k * f_k + f_k1 * f_k1         # F(2k + 1)
        
        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)
    
    return fib_fast(n)[0]
```

---

## 4. Quelle méthode choisir ?

| Méthode              | Temps        | Mémoire  | Avantage principal         |
| -------------------- | ------------ | -------- | -------------------------- |
| Tabulation DP        | O(n)         | O(n)     | Simple à comprendre        |
| Optimisation mémoire | O(n)         | O(1)     | Rapide, très propre        |
| Fast Doubling        | **O(log n)** | O(log n) | Ultra rapide pour grands n |

Pour ton labo :
→ **méthode O(1) ou fast doubling** recommandée pour F(119) ou plus.

---

## 5. Tests rapides

```python
assert fibonacci(0) == 0
assert fibonacci(7) == 13
assert fibonacci(10) == 55
assert fibonacci(119) == 3311648143516982017180081
```

---

# Conclusion

Le fast doubling est la version la plus performante, mais la version itérative O(1) est largement suffisante pour la majorité des cas. Toutes sont bien plus adaptées que la version récursive naïve (O(2ⁿ)).


