from itertools import chain, combinations
from networkx import Graph,faster_could_be_isomorphic
from sys import argv


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


graphbank = {
    2: [[(1, 2)], [(1, 2), (2, 1)]]
}


def subgraph(n):
    if n in graphbank.keys():
        return graphbank[n]
    nminus1 = subgraph(n-1)
    PS = list(powerset(range(1, n)))[1:]
    nlist = []
    for s in PS:
        hold = nminus1.copy()
        for i in s:
            h = []
            for g in hold:
                # print(type(h))
                h.append(g+[(i, n)])
                h.append(g+[(n, i)])
                h.append(g+[(i, n), (n, i)])
            hold = h
        nlist.extend(hold)
    graphbank[n] = nlist
    return graphbank[n]

def purgeisomorphism(graphlist):
    safe = []
    while graphlist:
        gtest = graphlist.pop()
        safe.append(gtest)
        graphlist = [g for g in graphlist if not faster_could_be_isomorphic(Graph(gtest),Graph(g))]


if __name__ == "__main__":
    n = int(argv[1])
    print(len(subgraph(n)))
