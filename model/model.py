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

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        list_artefatti = []

        # SONO BLOCCATO IN QUESTO PUNTO, NON SO DOVE RECUPERARE GLI ARTEFATTI


    @staticmethod
    def get_epoche():
        """Restituisce la lista di tutte le epoche."""
        list_epoche = ArtefattoDAO.read_epoche()
        return list_epoche

    # --- MUSEI ---
    @staticmethod
    def get_musei():
        """ Restituisce la lista di tutti i musei."""
        list_musei = MuseoDAO.read_musei()
        return list_musei