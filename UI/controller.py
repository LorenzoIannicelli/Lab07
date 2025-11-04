import flet as ft
from UI.view import View
from model.model import Model

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
    def handler_dd_museo_change(self, e):
        if self._museo_selezionato is None :
            self._museo_selezionato = self._view._dd_museo.value

    def handler_dd_epoca_change(self, e):
        if self._epoca_selezionata is None :
            self._epoca_selezionata = self._view._dd_epoca.value

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
