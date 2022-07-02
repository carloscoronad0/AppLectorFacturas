from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Factura:
    sort_index: int = field(init=False, repr=False)
    NIT_Emisor: int
    Numero_Factura: int
    Numero_Autorizacion: int
    Fecha_Emision: str
    Total: int
    Importe_Credito_Fiscal: int
    Codigo_Control: str
    NIT_Comprador: int
    Import_ICE_IEHD_TASAS: int
    Importe_ventas_No_Gravadas: int
    Importe_No_Sujeto_Credito_Fiscal: int
    Bonificaciones_Rebajas: int

    def __post__init__(self):
        object.__setattr__(self, 'sort_index', self.Total)

    def to_csv_format(self):
        return f"{self.NIT_Emisor},{self.Numero_Factura},{self.Numero_Autorizacion},{self.Fecha_Emision},{self.Total},{self.Importe_Credito_Fiscal},{self.Codigo_Control},{self.NIT_Comprador},{self.Import_ICE_IEHD_TASAS},{self.Importe_ventas_No_Gravadas},{self.Importe_No_Sujeto_Credito_Fiscal},{self.Bonificaciones_Rebajas}\n"
