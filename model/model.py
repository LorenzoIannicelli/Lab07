from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()
        self._lista_musei = []  # forse superflua
        self._lista_artefatti = []
        self._lista_artefatti_filtrati = []

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""

        if museo == 'NULL' and epoca == 'NULL' :
            return self._lista_artefatti
        elif museo == 'NULL'  :
            return [artefatto for artefatto in self._lista_artefatti if artefatto.epoca == epoca]
        elif epoca == 'NULL' :
            return [artefatto for artefatto in self._lista_artefatti if artefatto.id_museo == museo]
        else :
            return [artefatto for artefatto in self._lista_artefatti if artefatto.id_museo == museo and artefatto.epoca == epoca]

        '''self._lista_artefatti_filtrati = self._artefatto_dao.read_artefatti_filtrati(museo, epoca)

        return self._lista_artefatti_filtrati'''

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        list_epoche = set()
        self._lista_artefatti = self._artefatto_dao.read_artefatti()
        #print(self._lista_artefatti) \\ NON è vuota
        for artefatto in self._lista_artefatti:
            list_epoche.add(artefatto.epoca)

        return list(sorted(list_epoche))

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        self._lista_musei = self._museo_dao.read_musei()
        return self._lista_musei