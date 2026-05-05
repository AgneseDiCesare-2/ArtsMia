import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodi=DAO.get_nodi()
        #creo un idMap per mappare gli oggetti
        self.idMap={}
        for nodo in self._nodi:
            self.idMap[nodo.object_id]=nodo
        self._grafo=nx.Graph() #grafo semplice, pesato e non orientato

    def BuildGraphPesato(self):
        self._grafo.clear()
        self._grafo.add_nodes_from(self._nodi)
        self.addEdgesPesati()

    def addEdgesPesati(self):
        self._grafo.clear_edges()
        alledges = DAO.get_numOgg_esibizioni()

        for esibizione in alledges:
            if esibizione[1]>1: #se c'è più di un oggetto, li elenco
                id_oggetti_presenti=DAO.getOggetti_esibizione(esibizione[0]) #lista di id_oggetto
                #aggiungo un arco tra tutti gli id!
                for i in range(len(id_oggetti_presenti)):
                    u=self.idMap[id_oggetti_presenti[i]] #PRIMO OGGETTO
                    for j in range(i+1, len(id_oggetti_presenti)):
                        v=self.idMap[id_oggetti_presenti[j]]
                        if self._grafo.has_edge(u, v):
                            #se ciè già l'arco, incremento il peso
                            self._grafo[u][v]["weight"] += 1
                        #altrimenti aggiungo l'arco
                        else:
                            self._grafo.add_edge(u, v, weight=1)

    def get_numnodi(self):
        return len(self._grafo.nodes)

    def get_numarchi(self):
        return len(self._grafo.edges)