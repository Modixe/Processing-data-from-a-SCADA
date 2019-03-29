from DataAccessLayer.Repositories.db.RepositoryBase import RepositoryBase
from Models.Configuration import Configuration


class TagValueRepository(RepositoryBase):

    config = Configuration()
    config.load()

    def create(self, entity):
        cursor = self.connection.cursor()

        query = "INSERT INTO {0} (tag_id, value, value_quality, value_timestamp) VALUES ({1}, {2}, {3}, '{4}')" \
                .format(self.config.table_name, entity.tag_id, entity.value,
                        entity.quality, entity.timestamp.strftime("%d-%m-%Y %H:%M:%S"))

        cursor.execute(query)

        self.connection.commit()
        cursor.close()

    def update(self, entity):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE {0} "
                       "SET value={1}, value_quality={2} "
                       "WHERE tag_id={3} and value_timestamp='{4}';"
                       .format(self.config.table_name, entity.value, entity.quality, entity.tag_id,
                               entity.timestamp.strftime("%d-%m-%Y %H:%M:%S"), ))

        self.connection.commit()
        cursor.close()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "CREATE TABLE if not exists {0} (value_id BIGSERIAL, tag_id bigint not null,"
            "value text, value_quality text, value_timestamp timestamp without time zone,"
            "PRIMARY KEY (value_id, tag_id),"
            "FOREIGN KEY (tag_id) REFERENCES tags (tag_id))"
            .format(self.config.table_name))
        self.connection.commit()

        try:
            cursor.execute(
                "CREATE INDEX fki_{0}_tag_id_fkey \
                    ON public.\"{0}\" USING btree \
                    (tag_id) \
                    TABLESPACE pg_default;"
                .format(self.config.table_name))
            self.connection.commit()

        except Exception:
            cursor.execute("ROLLBACK")
            self.connection.commit()

        try:
            cursor.execute(
                "CREATE INDEX {0}_value_timestamp_index \
                    ON public.\"{0}\" USING btree \
                    (value_timestamp) \
                    TABLESPACE pg_default;"
                .format(self.config.table_name))
            self.connection.commit()

        except Exception:
            cursor.execute("ROLLBACK")
            self.connection.commit()

        cursor.close()

    def _entity_is_exist(self, tag_value):
        query = "SELECT value_id FROM {0} " \
                   "WHERE tag_id={1} and value_timestamp='{2}';" \
                   .format(self.config.table_name, tag_value.tag_id,
                           tag_value.timestamp.strftime("%d-%m-%Y %H:%M:%S"))

        cursor = self.connection.cursor()
        cursor.execute(query)

        # retrieve the records from the database
        records = cursor.fetchall()
        cursor.close()

        for _ in records:
            return True

        return False
