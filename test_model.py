from model.model import Model
model=Model()

print("Numero Nodi: ", (model.get_numnodi()))
print("Numero Archi: ", (model.get_numarchi()))
model.buildGraphPesato()

print("Numero Nodi: ", (model.get_numnodi()))
print("Numero Archi: ", (model.get_numarchi()))

connessi=model.componente_connessa(1224)
print("Numero Nodi: ", connessi[1])


