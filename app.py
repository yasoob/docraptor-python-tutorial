import docraptor
import os

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = os.environ.get("DOCRAPTOR_KEY")

with open("invoice.html", "r") as f:
    invoice_html = f.read()

try:
    response = doc_api.create_doc(
        {
            "test": True,
            "document_content": invoice_html,
            "name": "invoice.pdf",
            "document_type": "pdf",
        }
    )

    with open("invoice.pdf", "w+b") as f:
        binary_formatted_response = bytearray(response)
        f.write(binary_formatted_response)
        f.close()

except docraptor.rest.ApiException as error:
    print(error.status)
    print(error.reason)
    print(error.body)
