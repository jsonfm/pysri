#
from typing import Any, Union

#
from src.schemas.common import AmbienteType
from src.schemas.invoice import Invoice
from src.lib.xadessri import sign_xml
from src.utils.xml import dict_to_xml


def sign_invoice_and_authorize(
    p12_file: Union[bytes], 
    password: Union[bytes, str], 
    invoice: Union[dict[str, Any], str, Invoice], 
    environ: AmbienteType = AmbienteType.PRUEBAS,
    validate_input: bool = False,
):
    if isinstance(invoice, dict):
        xml_string = dict_to_xml(invoice)
    
    # xml_invoice = invoice.xml()
    signed = sign_xml(p12_file, password, xml_string)
    return signed