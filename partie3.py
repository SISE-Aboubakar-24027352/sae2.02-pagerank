import numpy as np

def somme_col(M):
    return np.sum(M, axis=0)

def stochastique(M):
    new = np.zeros((M.shape[0], M.shape[0]), dtype=float)
    s = somme_col(M)
    for i in range(len(M)):
        for j in range(len(M[i])):
            if s[j] != 0:
                new[i][j] = M[i][j] / s[j]
            else:
                new[i][j] = 0
    return new

def norme(X):
    return np.sqrt(np.sum(X**2))


def puissance_iterée(M, e):
    old = np.random.randint(0, 10, M.shape[0])
    tmp = old.dot(M)
    new = tmp / norme(tmp)
    i = 0
    while norme(new - old) > e:
        i += 1
        if i == 10000:
            return new, norme(M.dot(new))
        old = new
        tmp = M.dot(old)
        new = tmp / norme(tmp)
    return new, norme(M.dot(new)), i

def transition(M, a) :
    N = len(M)
    P = np.zeros((N, N), dtype=float)
    s = somme_col(M)
    for i in range(N) :
        for j in range(N) :
            if s[j] == 0 :
                P[i][j] = 1/N
            else :
                P[i][j] = a * M[i][j] + (1- a) / N
    return P

# 3.2A - Ajout de Hubs seulement
webAvecHub = np.array([
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Page 1 [Hub] -> {2, 3, 4, 5, 6}
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1],  # Page 10 [Hub] -> {6, 9, 11, 12, 13, 14}
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
])

e = 10**(-10)
a = 0.85
Q = stochastique(webAvecHub.T)
P = transition(Q, a)

print("Influence du critère d'arrêt sur Hub seulement")
r, val, i= puissance_iterée(P, e)

print("\nPrécision =", e)
print("\nMarge d'erreur :", norme(r - P.dot(r)))
print("\nNombre d'iteration :", i)
print("\n")
for page in range(len(r)):
    print(f"Page {page+1:<3}: {r[page]:.4f}")

print("\n--------------------------------------------------")

# 3.2B - Ajout d'Autorité seulement
webAvecAutorite = np.array([
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Page 6 [Autorité] -> {8}
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Page 14 [Autorité] -> {}
])

e = 10**(-10)
a = 0.85
Q = stochastique(webAvecAutorite.T)
P = transition(Q, a)

print("Influence du critère d'arrêt sur Authorite seulement")
r, val, i= puissance_iterée(P, e)

print("\nPrécision =", e)
print("\nMarge d'erreur :", norme(r - P.dot(r)))
print("\nNombre d'iteration :", i)
print("\n")
for page in range(len(r)):
    print(f"Page {page+1:<3}: {r[page]:.4f}")

print("\n---------------------------------------------------")

# 3.2C - Ajout des Hubs et des Autorités
webAvecHubAutorite = np.array([
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 1 [Autorité] -> {2, 6}
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],  # Page 6 [Hub] -> {1, 7, 8, 9, 10}
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 8 [Autorité] -> {}
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0]  # Page 14 [Hub] -> {10, 11, 13}
])


e = 10**(-10)
a = 0.85
Q = stochastique(webAvecHubAutorite.T)
P = transition(Q, a)

print("Influence du critère d'arrêt sur Hub et Authorite")
r, val, i= puissance_iterée(P, e)

print("\nPrécision =", e)
print("\nMarge d'erreur :", norme(r - P.dot(r)))
print("\nNombre d'iteration :", i)
print("\n")
for page in range(len(r)):
    print(f"Page {page+1:<3}: {r[page]:.4f}")

print("\n---------------------------------------------------")

webPageXScoreBoost = np.array([
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 2 -> Page 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 3 -> Page 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 4 -> Page 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 5 -> Page 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # Page 6 -> Page 1, 10
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 7 -> Page 1
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 8 -> Page 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # Page 9 -> Page 10, 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Page 10 > Page 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # Page 11 -> Page 10, 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # Page 12 -> Page 10, 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # Page 13 -> Page 10, 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]   # Page 14 -> Page 10, 1
])

e = 10**(-10)
a = 0.85
Q = stochastique(webPageXScoreBoost.T)
P = transition(Q, a)
r, val, i= puissance_iterée(P, e)

print("Influence de la manipulation des liens pour booster une page")

print("\nPrécision =", e)
print("\nMarge d'rreur :", norme(r - P.dot(r)))
print("\nNombre d'iteration :", i)
print("\n")
for page in range(len(r)):
    print(f"Page {page+1:<3}: {r[page]:.4f}")

print("\n---------------------------------------------------")

web = np.array([
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
], dtype=float)

e = 10**(-10)
Q = stochastique(web.T)



for a in [0.1, 0.3, 0.6, 0.99]:
    P = transition(Q, a)
    r, val, i= puissance_iterée(P, e)
    print("\n----------------------------------------------------------------------")
    print("Calcul avec alpha = ", a)
    print("\nNombre d'itération :", i)
    print("\n")
    for page in range(len(r)):
        print(f"Page {page+1:<3}: {r[page]:.4f}")

#print("\nOn peut voir que plus α est élevée plus les pages trés pointé monopolise le score.")