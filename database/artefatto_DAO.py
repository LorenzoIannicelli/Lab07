from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    @staticmethod
    def read_epoche():
        results = set()
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            print("No database connected")
            return None
        else :
            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM artefatto"
            cursor.execute(query)

            for row in cursor :
                artefatto = Artefatto(row['id'], row['nome'], row['tipologia'], row['epoca'], row['id_museo'])
                results.add(artefatto.epoca)

        results = list(results)
        cursor.close()
        cnx.close()

        return results