import flet as ft
from UI.view import View
from model.model import Model
from UI.alert import AlertManager

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self._museo_selezionato = None
        self._epoca_selezionata = None

    # POPOLA DROPDOWN
    def crea_opzioni_dd_museo(self, lista_musei):
        options = [ft.dropdown.Option(None, 'Nessun filtro')]
        for museo in lista_musei:
            options.append(
                ft.dropdown.Option(key = museo.id, text = museo.nome)
            )

        return options

    def crea_opzioni_dd_epoche(self, list_epoche) :
        options = [ft.dropdown.Option(None, 'Nessun filtro')]
        for epoca in list_epoche:
            options.append(
                ft.dropdown.Option(key = epoca, text = epoca)
            )

        return options

    # CALLBACKS DROPDOWN
    def handler_dd_museo_change(self, e):
        if self._museo_selezionato is None:
            self._museo_selezionato = self._view._dd_museo.value
        else:
            self.handler_filtra_artefatti(None)

    def handler_dd_epoca_change(self, e):
        if self._epoca_selezionata is None:
            self._epoca_selezionata = self._view._dd_epoca.value
        else:
            self.handler_filtra_artefatti(None)

    # AZIONE: MOSTRA ARTEFATTI

    def handler_filtra_artefatti(self, e):
        if self._museo_selezionato is None or self._epoca_selezionata is None :
            alt = AlertManager(self._view.page)
            alt.show_alert('Selezionare opzioni per il museo e/o epoca.\nÈ possibile selezionare "Nessun filtro".')
        else :
            self._view.listview_artefatti.clean()
            artefatti = self._model.get_artefatti_filtrati(self._museo_selezionato, self._epoca_selezionata)