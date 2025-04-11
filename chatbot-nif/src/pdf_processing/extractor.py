import pdfplumber
import logging

def extract_text_from_pdf(pdf_path):
    """
    Extrae todo el texto de un archivo PDF.
    """
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                logging.info(f"Procesando página {page_num + 1}")
                page_text = page.extract_text(x_tolerance=3, y_tolerance=3)
                if page_text:
                    # Elimina encabezados y pies de página
                    lines = page_text.splitlines()
                    content = [line for line in lines if len(line) > 5]  # Filtra líneas muy cortas
                    text += "\n".join(content) + "\n\n"  # Agrega doble salto para separación de párrafos
    except Exception as e:
        logging.error(f"Error al leer el PDF: {e}")
    return text