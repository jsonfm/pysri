### PySRI

Python + SRI e-invoicing

### Sign XML Invoice and Authorize

```python
from pysri import sign_invoice_and_authorize, AmbienteType

with open("/signature.p12", mode="rb") as file:
    p12 = file.read() # bytes

invoice_xml = """<xml><data>some important data</data></xml>"""
response = sign_invoice_and_authorize(
    p12,
    "password",
    invoice_xml,
    AmbienteType.PRUEBAS,
    validate_input=True
)
```
