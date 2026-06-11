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
    return np.sqrt(np.sum(X ** 2))


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
    return new, norme(M.dot(new))


Partie1 = np.array([
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

e = 10 ** (-10)

Q = stochastique(Partie1.T)

r, val = puissance_iterée(Q, e)

print("r =")
print(r)
print("\nQr =")
print(Q.dot(r))
print("\nValeur propre = ", val)
print("\nMarge d'erreur =", norme(r - Q.dot(r)))
print("\nVu que la marge d'erreur est tres petite on peut dire que r est approximativement solution de r = Qr")