from os.path import isfile
from os.path import isdir
from os.path import split
from os import makedirs

from model.documento import AccionesDocumento
from controller.control_facturas import ControlFacturas

class ControladorDocumento:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.filepath, self.filename = split(path_to_file)

    def write_to_file(self, doc_action: AccionesDocumento, fac_control: ControlFacturas):
        # The AccionesDocumento layer exists due to the fact that any of the "w", "a", "x" actions
        # will create the file if it doesn't exists. AccionesDocumento allows the app to add 
        # some functionality by putting constraints over the actions the user selects to use

        if doc_action == AccionesDocumento.CrearYEscribirDocumento:
            # If the path does not exist, create it
            if not isdir(self.filepath):
                makedirs(self.filepath)
            # The file will be created using this action
            action = "w"

        elif doc_action == AccionesDocumento.SobreEscribirDocumento:
            # If the file does not exist, raise an error
            if not isfile(self.path_to_file):
                raise ValueError("No se puede agregar elementos a un archivo inexistente")
            # To overwrite the file content
            action = "w"

        elif doc_action == AccionesDocumento.AgregarADocumento:
            # If the file does not exist, raise an error
            if not isfile(self.path_to_file):
                raise ValueError("No se puede agregar elementos a un archivo inexistente")
            # To append to the content of the file
            action = "a"

        document_text = '\n'.join(set([aux.to_csv_format() for aux in fac_control.control]))
        self.__write_elements__(action. document_text)
                
    def __write_elements__(self, action: str, text: str):
        with open(self.path_to_file, action) as f:
            f.write(text)
            f.close()
