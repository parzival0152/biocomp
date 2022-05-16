from sys import argv
from itertools import chain, combinations
from networkx import DiGraph,is_isomorphic
# networkx is a python library for graphs and it is used here to check if two directed graphs are isomorphic

# powerset generator function taken from pythons native itertools lib examples
# the power set is needed to model the different choices of nodes from (n-1) to connect to the nth node
def powerset(iterable:list[any]):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


graphbank = { # used for memoization to reduce back calls to lower n
    1: [[(1, 1)]],
    2: [[(1, 2)], [(1, 2), (2, 1)]]
}


def subgraph(n:int) -> list[list[tuple[int,int]]]:
    if n not in graphbank.keys(): # if we dont have the answer stored, compute it then store it
        nminus1 = subgraph(n-1) # get the n-1 size graphs
        PS = list(powerset(range(1, n)))[1:] # generate a powerset for the nodes of the n-1 graphs and ignore the empty set (the first set)
        nlist = [] # create new buffer list
        for s in PS: # for each set in the powerset
            hold = nminus1.copy() # create a copy of the n-1 graphs as to not mess with other sets
            for i in s: # for each node in the current set
                h = [] # create temporary buffer
                for g in hold: # for each graph in the list
                    h.append(g+[(i, n)]) # add a graph with i -> n
                    h.append(g+[(n, i)]) # add a graph with n -> i
                    h.append(g+[(i, n), (n, i)]) # add a graph with both i -> n and n -> i
                hold = h # update the held list with the buffer
            nlist.extend(hold) # add all the graphs that were created under this set to the comprehensive list
        graphbank[n] = purgeisomorphism(nlist) # remove all isomorphic graphs then store the answer
    return graphbank[n] # in the end serve the stored answer

def purgeisomorphism(graphlist:list[list[tuple[int,int]]]) -> list[list[tuple[int,int]]]:
    # this purging algorithem works with the sieve method of choosing the first graph and adding it to a "safe" buffer
    # then on each pass we remove from the list all the graphs that are isomorphic to the chosen graph
    # repeat till the list we were given is empty then we can be sure that the list of "safe" graphs are all non isomorphic to one another
    safe = []
    while graphlist:
        gtest = graphlist.pop(0)
        safe.append(gtest)
        graphlist = [g for g in graphlist if not is_isomorphic(DiGraph(gtest),DiGraph(g))]
    return safe


if __name__ == "__main__":
    n = int(argv[1])
    subgraphs = subgraph(n)
    print(f"n = {n}")
    print(f"count = {len(subgraphs)}")
    for i,graph in enumerate(subgraphs):
        print(f"#{i+1}")
        for t,f in graph:
            print(t,f)
