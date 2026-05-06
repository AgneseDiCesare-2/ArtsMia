import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        self._idOggetto=None
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        #quando clicco creo il grafo pesato
        self._model.buildGraphPesato()
        self._view.txt_result.controls.append(ft.Text("grafo creato correttamente. "))
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {self._model.get_numnodi()} nodi e {self._model.get_numarchi()} archi. "))
        self._view._page.update()

    def handleCompConnessa(self,e):
        #voglio cercare tutti i nodi che sono raggiungibili dal nodo selezionato (BFV O DFV)
        #in questo caso non mi interessa un cammino minimo --> uso DBV (più veloce)
        output=self._model.componente_connessa(self._idOggetto) #tupla (lista, len(Lista))
        if output==0:
            self._view.txt_result.controls.append(ft.Text("Inserire un id_oggetto valido!"))
            self._view._page.update()
            return
        #altrimenti output è la lista dei nodi (object) connessi:
        self._view.txt_result.controls.append(ft.Text(f"I nodi connessi sono {output[1]}"))
        for nodo in output[0]:
            self._view.txt_result.controls.append(ft.Text(nodo))
            self._view._page.update()


    def get_idOggetto(self):
        id=self._view._txtIdOggetto.value
        if id == "" or id is None:
            self._view.txt_result.controls.append(ft.Text("Inserisci un id_oggetto per continuare! ", color="red"))
            self._view._page.update()
            return
        self._idOggetto=int(id)
        return
