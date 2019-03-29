
class RepositoryBase(object):

    connection = None

    def __init__(self, connection):
        self.connection = connection

    def create(self, entity):
        pass

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

    def create_table(self):
        pass

    def create_or_update(self, entity):
        if self._entity_is_exist(entity):
            self.update(entity)
        else:
            self.create(entity)

    def _entity_is_exist(self, tag_name):
        pass

