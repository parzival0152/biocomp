from itertools import chain, combinations
from pprint import pprint


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# if we have an existing connected sub graph of size n-1, for each node in the sub graph we can create 3 more sub graphs for size n
# choosing a vertex i we can add the edge "i n" the edge "n i" and both of them.
# for each choice of 2 vertecies i,j we can create 9 more graphs, 3 for i and 3 for j
graphbank = {
    2: [[(1,2)],[(1,2),(2,1)]]
}


def subgraph(n):
    if n in graphbank.keys():
        return graphbank[n]
    nminus1 = graphbank[n-1]
    PS = list(powerset(range(1,n)))[1:]
    nlist = []
    for s in PS:
        hold = nminus1.copy()
        for i in s:
            h = []
            for g in hold:
                print(type(h))
                # h.append(g.append((i,n)))
                # h.append(g.append((n,i)))
                # h.append(g.extend(((i,n),(n,i))))
            hold = h
        nlist.extend(hold)
    graphbank[n] = nlist
    return graphbank[n]


if __name__ == "__main__":
    pprint(subgraph(3))
    