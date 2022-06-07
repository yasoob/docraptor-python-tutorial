import docraptor
import os

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = os.environ.get("DOCRAPTOR_KEY")
doc_api.api_client.configuration.debug = True

with open("invoice.html", "r") as f:
    invoice_html = f.read()

response = doc_api.create_doc(
    {
        "test": True,
        "document_content": invoice_html,
        "name": "invoice.pdf",
        "document_type": "pdf",
    }
)

with open("invoice.pdf", "wb") as f:
    f.write(response)
