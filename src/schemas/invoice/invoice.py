from src.schemas.common import BinaryResponseType, DocumentIdentificationType
from typing import Optional
from pydantic import BaseModel, Field


class InvoiceInfo(BaseModel):
    fechaEmision: str = Field(...)
    dirEstablecimiento: str = Field(...)
    contribuyenteEspecial: Optional[str]
    obligadoContabilidad: BinaryResponseType
    tipoIdentificacionComprador: DocumentIdentificationType
    guiaRemision: str