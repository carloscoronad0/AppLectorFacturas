from os.path import exists

class Documento:
    def __init__(self, path):
        self.path = path
        self.file_created = exists(path)

    def write_to_document(self):
        if self.file_created:
