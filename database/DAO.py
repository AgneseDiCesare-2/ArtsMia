from database.DB_connect import DBConnect
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

    @staticmethod
    def get_numOgg_esibizioni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select eo.exhibition_id, count(*) as num_oggetti
                    from exhibition_objects eo 
                    group by eo.exhibition_id """
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
        query = """select eo.object_id
                    from exhibition_objects eo 
                    where eo.exhibition_id =%s"""
        cursor.execute(query, (id_exh, ))

        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result #lista di id_oggetti presenti a quell'esibizione