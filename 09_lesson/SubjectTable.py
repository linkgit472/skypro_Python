from sqlalchemy import create_engine, text


class SubjectTable:
    __scripts = {
        "select all": text("SELECT * FROM subject"),
        "select by id": text("SELECT * FROM subject "
                             "WHERE subject_id = :id"),
        "insert": text("INSERT INTO subject(\"subject_title\") "
                       "VALUES (:title)"),
        "update title": text("UPDATE subject SET subject_title = :title "
                             "WHERE subject_id = :id"),
        "get max id": text("SELECT MAX(subject_id) FROM subject"),
        "delete_by_id": text("DELETE FROM subject "
                             "WHERE subject_id = :id_to_delete")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_all_subject(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select all"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def get_subject_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select by id"],
                              {"id": id})
        rows = result.mappings().first()
        conn.close()
        return rows

    def add_subject(self, title):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert"],
                     {"title": title})
        conn.commit()
        conn.close()

    def change_subject_title(self, new_title, max_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update title"],
                     {"title": new_title, "id": max_id})
        conn.commit()
        conn.close()

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get max id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def delete(self, id):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete_by_id"],
            {"id_to_delete": id}
        )
        conn.commit()
        conn.close()

    def create_random_subject(self):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert"], {"title": "QA"})
        conn.commit()

        id = conn.execute(self.__scripts["get max id"]).scalar()
        conn.close()
        return id
