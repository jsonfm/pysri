from enum import StrEnum


class AmbienteType(StrEnum):
    PRODUCCION = "PRODUCCION"
    PRUEBAS = "PRUEBAS"
    

class BinaryResponseType(StrEnum):
    SI = "SI"
    NO = "NO"


class DocumentIdentificationType(StrEnum):
    RUC = "04"
    CEDULA = "05"
    PASAPORTE = "06"
    VENTA_A_CONSUMIDOR_FINAL = "07"
    IDENTIFICACION_DEL_EXTERIOR = "08"
    

class DocumentType(StrEnum):
    FACTURA = "01"
    LIQUIDACION_DE_COMPRA_DE_BIENES_Y_PRESTACION_DE_SERVICIOS = "03"
    NOTA_DE_CREDITO = "04"
    NOTA_DE_DEBITO = "05"
    GUIA_DE_REMISION = "06"
    COMPROBANTE_DE_RETENCION = "07"