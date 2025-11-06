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
    def get_lista_musei(self):
        return self._model.get_musei()

    def get_lista_epoche(self):
        return self._model.get_epoche()

    def crea_opzioni_dd_museo(self):
        lista_musei = self.get_lista_musei()
        options = [ft.dropdown.Option('Nessun filtro', 'Nessun filtro')]
        for museo in lista_musei:
            options.append(
                ft.dropdown.Option(key = museo.id, text = museo.nome)
            )

        return options

    def crea_opzioni_dd_epoche(self) :
        list_epoche = self.get_lista_epoche()
        options = [ft.dropdown.Option('Nessun filtro', 'Nessun filtro')]
        for epoca in list_epoche:
            options.append(
                ft.dropdown.Option(key = epoca, text = epoca)
            )

        return options

    # CALLBACKS DROPDOWN
    def handler_dd_museo_change(self, e):
        self._museo_selezionato = self._view._dd_museo.value

        print('museo cambiato', self._museo_selezionato)

    def handler_dd_epoca_change(self, e):
        self._epoca_selezionata = self._view._dd_epoca.value

        #print('epoca cambiata', self._epoca_selezionata)

    # AZIONE: MOSTRA ARTEFATTI

    def handler_filtra_artefatti(self, e):
        if self._museo_selezionato is None or self._epoca_selezionata is None :
            alt = AlertManager(self._view.page)
            alt.show_alert('Selezionare opzioni per il museo e/o epoca.\nÈ possibile selezionare "Nessun filtro".')
        else :
            self._view.listview_artefatti.clean()
            #print(self._museo_selezionato)
            artefatti = self._model.get_artefatti_filtrati(self._museo_selezionato, self._epoca_selezionata)
            #print(artefatti) \\ stringa vuota solo se seleziono un museo
            for artefatto in artefatti:
                self._view.listview_artefatti.controls.append(ft.Text(f'{artefatto}'))
            self._view.update()