import flet as ft
from UI.alert import AlertManager
from database.museo_DAO import MuseoDAO
from model.model import Model

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self._controllercontroller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self._controller = controller

    def update(self):
        self.page.update()

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
                ft.dropdown.Option(key = epoca.id, text = epoca.id)
            )

        return options

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        list_musei = Model.get_musei()
        self._dd_museo = ft.Dropdown(label = 'Museo',
                                     options = self.crea_opzioni_dd_museo(list_musei),
                                     width = 200,
                                     hint_text = 'Seleziona il museo',
                                     on_change = self._controller.handler_dd_museo_change)

        list_epoche = Model.get_epoche()
        self._dd_epoca = ft.Dropdown(label = 'Epoca',
                                     options = self.crea_opzioni_dd_epoche(list_epoche),
                                     width=200,
                                     hint_text="Seleziona l'epoca",
                                     on_change=self._controller.handler_dd_epoca_change)

        # Sezione 3: Artefatti
        # TODO

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            ft.Row(controls = [self._dd_museo, self._dd_epoca],
                   alignment = ft.MainAxisAlignment.CENTER),
            ft.Divider()

            # Sezione 3: Artefatti
            # TODO
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
