from model.model import Model
model=Model()

print("Numero Nodi: ", (model.get_numnodi()))
print("Numero Archi: ", (model.get_numarchi()))
model.BuildGraphPesato()
model.addEdgesPesati()

print("Numero Nodi: ", (model.get_numnodi()))
print("Numero Archi: ", (model.get_numarchi()))


