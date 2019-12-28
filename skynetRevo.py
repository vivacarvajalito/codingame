import sys
import math
from collections import deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def main():
    #creamos grafos
    g = Graph()
    # n: the total number of nodes in the level, including the gateways
    # l: the number of links
    # e: the number of exit gateways
    n, l, e = [int(i) for i in input().split()]
    print("n={}, l={}, e={}".format(n,l,e), file=sys.stderr)
    for i in range(l):
        # n1: N1 and N2 defines a link between these nodes
        n1, n2 = [int(j) for j in input().split()]
        g.addLink(n1,n2)
        print("n1={},n2={}".format(n1,n2), file=sys.stderr)
    for i in range(e):
        ei = int(input())  # the index of a gateway node
        print("e1={}".format(ei), file=sys.stderr)
        g.addGate(ei)
    
    #imprimir todo los graph
    #g.show_edges()
    # game loop
    while True:
        si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
        print("si={}".format(si), file=sys.stderr)
        g.print(si)
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)


        # Example: 0 1 are the indices of the nodes you wish to sever the link between
        #print("0 1")

class Graph:
    graph_dict = {}
    gateways = []

    def addLink(self, node, neighbour):
        self.node = str(node)
        self.neighbour = str(neighbour)
        if self.node not in self.graph_dict:
            self.graph_dict[self.node] = [self.neighbour]
        else:
            self.graph_dict[self.node].append(self.neighbour)
        
        if self.neighbour not in self.graph_dict:
            self.graph_dict[self.neighbour] = [self.node]
        else:
            self.graph_dict[self.neighbour].append(self.node)
    
    def deleteLink(self, node, neighbour):
        self.node = str(node)
        self.neighbour = str(neighbour)
        if self.node in self.graph_dict:
            try:
                self.graph_dict[self.node].remove(self.neighbour)
                self.graph_dict[self.neighbour].remove(self.node)
            except ValueError:
                print('No se encuentra el valor {} en el nodo {}'.format(self.neighbour, self.node), file=sys.stderr)
    
    def addGate(self, gateway):
        self.gateways.append(str(gateway))
    

    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("({},{})".format(node,neighbour), file=sys.stderr)
    
    def search(self, start, goal):
        start = str(start)
        goal = str(goal)
        explored = []
        queue = [[start]]
        
        if(start == goal):
            print("El inicio {} es el mismo que la salida {}".format(start, goal))
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in explored:
                neighbours = self.graph_dict[node]
                
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)
                    if(neighbour == goal):
                        return new_path
                explored.append(node)
        
        return "No conseguimos un camino para este objetivo"
        
    def print(self, start):
        start = str(start)
        result = []
        for goal in self.gateways:
            result.append(self.search(start,goal))
        for res in result:
            print("Estos son los resultados: {}".format(res), file=sys.stderr)
        result.sort(key=len)
        if(len(result) > 0 ):
            res = result[0]
            self.deleteLink(res[0], res[1])
            print("{} {}".format(res[0],res[1]))

def test():
    g = Graph()
    g.addLink(1,2)
    g.addLink(1,0)
    g.show_edges()
    print(g.search(1,2))     


if __name__ == "__main__":
    main()