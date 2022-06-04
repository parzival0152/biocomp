from sys import argv
from networkx import DiGraph,is_isomorphic
import networkx as nx
from generate_subgraphs import subgraph,powerset

def motif_count(g:DiGraph,motif:DiGraph) -> int:
    count = 0
    edges = g.edges
    for edgeset in powerset(edges):
        count += is_isomorphic(DiGraph(edgeset),motif)
    return count
        
def motif_count_generator(n:int, edgelist:list[tuple[int,int]]) -> list[int]:
    G = DiGraph(edgelist) # turn the given edge list to a DiGraph
    assert n<=4,"N is too large and we will be here all day" # we know the code wont wrap up in a timly manner if n>4 so we assert it here 
    subgraphs = subgraph(n) # generate all the subgraphs from question 1
    return [(motif_count(G,DiGraph(g)),g) for g in subgraphs] # return a list with the count of the accorances of isomorphisms
    


if __name__ == "__main__":
    filename = argv[1] # get file path from argument
    n = 1
    edges = []
    with open(filename,'r') as f: # open the file in read mode
        lines = f.readlines()
        n = int(lines.pop(0).strip()) # the first line is N
        edges = [line.strip().split(" ") for line in lines]
        edges = [(int(a),int(b)) for a,b in edges] # parse the given form of edges to a list of tuples
    for i,(count,motif) in enumerate(motif_count_generator(n,edges)): # run the count generator on the given data
        print(f"#{i+1}")
        print(f"count = {count}") # format and output the data in the format that was asked
        for t,f in motif:
            print(t,f)