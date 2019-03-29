from DataAccessLayer.Repositories.db.RepositoryBase import RepositoryBase


class TagRepository(RepositoryBase):

    def create(self, entity):

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO tags (tag_name, tag_description) VALUES (%s, %s)"
                       "RETURNING tag_id", (entity.name, entity.description))

        self.connection.commit()

        records = cursor.fetchall()
        entity.id = records[0][0]
        cursor.close()

    def update(self, entity):

        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE public.tags \
                SET tag_description=%s \
                WHERE tag_name=%s \
                RETURNING tag_id", (entity.description, entity.name,))

        self.connection.commit()
        records = cursor.fetchall()
        entity.id = records[0][0]

        cursor.close()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "CREATE TABLE if not exists tags (tag_id BIGSERIAL PRIMARY KEY, tag_name text, tag_description text);")

        self.connection.commit()

        try:
            cursor.execute(
                "CREATE UNIQUE INDEX if not exists tags_tag_description_index \
                        ON public.tags USING btree \
                        (tag_name COLLATE pg_catalog.\"default\") \
                        TABLESPACE pg_default;")
            self.connection.commit()

        except Exception:
            cursor.execute("ROLLBACK")
            self.connection.commit()

        cursor.close()

    def _entity_is_exist(self, tag):
        cursor = self.connection.cursor()
        cursor.execute("SELECT tag_id FROM tags \
                        WHERE tag_name=%s;", (tag.name,))

        # retrieve the records from the database
        records = cursor.fetchall()
        cursor.close()

        for _ in records:
            return True

        return False
