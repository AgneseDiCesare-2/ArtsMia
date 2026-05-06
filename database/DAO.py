from database.DB_connect import DBConnect
from model.arco import Arco
from model.objects import Object


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_nodi():
            conn = DBConnect.get_connection()

            result = []

            cursor = conn.cursor(dictionary=True)
            query = """select *
                        from objects o """
            cursor.execute(query)

            for row in cursor:
                result.append(Object(**row))
            cursor.close()
            conn.close()
            return result

    #NB: MOLTO INTELLIGENTE!
    @staticmethod
    def getEdgePeso(idMap):
        #mi prende già tutte le coppie (una volta grazie al < nella query), e mi restiutisce le coppie di nodi
        #tra cui esiste una connessione e il relativo peso!
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select  eo1.object_id as o1, eo2.object_id as o2, count(*) as peso
                    from exhibition_objects eo1, exhibition_objects eo2
                    where eo1.exhibition_id = eo2.exhibition_id and eo1.object_id < eo2.object_id
                    group by  eo1.object_id, eo2.object_id
                    """
        cursor.execute(query)
        for row in cursor:
            result.append(Arco(idMap[row["o1"]], idMap[row["o2"]], row["peso"])) #restituisce direttamente gli oggetti

        cursor.close()
        conn.close()
        return result

    """@staticmethod
    def get_numOgg_esibizioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = select eo.exhibition_id, count(*) as num_oggetti
                    from exhibition_objects eo 
                    group by eo.exhibition_id 
        cursor.execute(query)

        for row in cursor:
            result.append((row["exhibition_id"], row["num_oggetti"]))
        #(exhibition_id, num_oggetti)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getOggetti_esibizione(id_exh):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = select eo.object_id
                    from exhibition_objects eo 
                    where eo.exhibition_id =%s
        cursor.execute(query, (id_exh, ))

        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result #lista di id_oggetti presenti a quell'esibizione"""