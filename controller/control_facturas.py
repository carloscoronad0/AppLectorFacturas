import cv2
import numpy as np

from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol
from typing import List
from os.path import isdir
from os.path import splitext
from os.path import join
from os import walk

from model.factura import Factura

ACCEPTED_EXTENSIONS = [".jpg", ".png"]

class ControlFacturas:
    def __init__(self, control_name):
        self.name: str = control_name
        self.control: List[Factura] = []

    def __get_barcodes__(self, item):
        return pyzbar.decode(item, symbols=[ZBarSymbol.QRCODE])

    def add_from_folder(self, path):
        if isdir(path):
            filenames = next(walk(path), (None, None, []))[2]

            # Iterating over the files
            for f in filenames:
                _, ext = splitext(f)

                # If the file is valid (It's an image)
                if ext in ACCEPTED_EXTENSIONS:
                    complete_path = join(path, f)
                    barcodes = self.__get_barcodes__(cv2.imread(complete_path))

                    if len(barcodes) > 0:
                        self.__save_from_barcodes__(barcodes)
                    else:
                        print(f"No barcodes found in {f}")

            # for fac in self.control:
                # print(fac)
        else:
            raise ValueError('Not a valid path')

    def add_from_camera(self):
        camera = cv2.VideoCapture(0)
        show_pic = True

        while show_pic:
            ret, frame = camera.read()
            cv2.imshow('Lector QR', frame)
            barcodes = self.__get_barcodes__(frame)

            if len(barcodes) > 0:
                self.__save_from_barcodes__(barcodes)
                show_pic = False

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()

    def __save_from_barcodes__(self, barcodes):
        for barcode in barcodes:
            barcode_fields = barcode.data.decode('utf-8').split('|')

            # The structure of the QR barcodes "ine" uses has 13 fields
            if len(barcode_fields) == 12:
                ne, nf, na, fe, t, icf, cc, nc, iIIT, ivng, inscf, br = barcode_fields
                self.control.append(Factura(ne, nf, na, fe, t, icf, cc, nc, iIIT, ivng, inscf, br))
            else:
                print(f"El codigo QR en la imagen {path} no es valido, posee menos campos dde los requerdos")

    def write_to_file(self, path):
        document_text = ""
        for fac in self.control:
            document_text += fac.to_csv_format()

        print("To write: ", document_text)

        with open(path, "w") as f:
            f.write(document_text)
            f.close()
