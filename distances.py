#! /usr/bin/env python
# encoding: utf-8

# Constant
IFTY = 100

def min(a, b):
    return a if a < b else b


def min3(a, b, c):
    return min(min(a, b), c)


# Compute editing distance on strings a and b
def edit_dist(a, b):
    assert (a > 0 and b > 0)
    d = 0
    matrix = [[IFTY for i in range(len(a)+1)] for i in range(len(b) + 1)]
    matrix[0] = [i for i in range(len(a)+1)]
    for i in xrange(len(b)+1):
        matrix[i][0] = i
# i -1 ci sono perchè prendiamo della lista la fetta 1..n, e non 0..n-1 (come invece sono gli indici dei caratteri della stringa)
    for i in range(len(b)+1)[1:]:
        for j in range(len(a)+1)[1:]:
            d = 0 if a[j-1] == b[i-1] else 1
            matrix[i][j] = min3( matrix[i-1][j]+1,
                 matrix[i][j-1]+1,
                 matrix[i-1][j-1] + d
            )

    # print matrix
    return matrix[len(b)][len(a)]

def pm(matrix, h, w):
    for i in range(h):
        print i
        print("{}".format(matrix[i]))

if __name__ == "__main__":
    # Testing levenshtein distance
    print("edit_dist '{}' '{}' = '{}'\n".format("prova", "prova", edit("prova", "prova")))
    print("edit_dist '{}' '{}' = '{}'\n".format("prova", "proda", edit("prova", "proda")))
    print("edit_dist '{}' '{}' = '{}'\n".format("prova", "proa", edit("prova", "proa")))
    print("edit_dist '{}' '{}' = '{}'\n".format("prova", "prov", edit("prova", "prov")))
    print("edit_dist '{}' '{}' = '{}'\n".format("prova", "y", edit("prova", "y")))
    print("edit_dist '{}' '{}' = '{}'\n".format("prova", "orova", edit("prova", "orova")))
    print("edit_dist '{}' '{}' = '{}'\n".format("rova", "prova", edit("rova", "prova")))
    print("edit_dist '{}' '{}' = '{}'\n".format("prova", "rova", edit("prova", "rova")))
    print("edit_dist '{}' '{}' = '{}'\n".format("prova", "provaaa", edit("prova", "provaaa")))



