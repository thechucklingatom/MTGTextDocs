from docx import *

def createDocumentTest():
    document = newdocument()
    body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]
    body.append('Test text')
    savedocx(document, None, None, None, None, None, 'Test.docx')
