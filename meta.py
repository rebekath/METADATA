import PyPDF2
import openpyxl
from docx import Document
pdf = open ("7 Tampoco pido tanto megan maxwell.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
meta = reader.metadata
print(meta)

import openpyxl

def extract_xlsx_metadata(file_path):
    wb = openpyxl.load_workbook(file_path)
    metadata = {}
    metadata['properties'] = wb.properties
    return metadata

metadata = extract_xlsx_metadata("CALIFICACIONES TERCER PERIODO.xlsx")
print(metadata)

def extract_docx_metadata(file_path):
    doc = Document(file_path)
    metadata = {
        "Title": doc.core_properties.title,
        "Author": doc.core_properties.author,
        "Subject": doc.core_properties.subject,
        "Keywords": doc.core_properties.keywords,
        "Comments": doc.core_properties.comments,
        "Last Modified By": doc.core_properties.last_modified_by,
        "Revision": doc.core_properties.revision,
        "Created": doc.core_properties.created,
        "Modified": doc.core_properties.modified
    }
    return metadata

def main():
    docx_file = "prog.docx"
    metadata = extract_docx_metadata(docx_file)

    print("Metadatos del archivo:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()