from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
import pytesseract
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx import Document

# Definir rutas para Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class PDFshield:
    def __init__(self, ogfile, protectedfile, password):
        self.ogfile = ogfile
        self.protectedfile = protectedfile
        self.password = password

    def save_as_txt(self, text, filename):
        """Guardar el texto extraído como archivo .txt"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)

    def save_as_pdf(self, text, filename):
        """Guardar el texto extraído como archivo PDF"""
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        text_object = c.beginText(40, height - 40)
        text_object.setFont("Helvetica", 10)
        text_object.setTextOrigin(40, height - 40)
        text_object.textLines(text)
        c.drawText(text_object)
        c.showPage()
        c.save()

    def save_as_docx(self, text, filename):
        """Guardar el texto extraído como archivo .docx"""
        doc = Document()
        doc.add_paragraph(text)
        doc.save(filename)

    def save_as_html(self, text, filename):
        """Guardar el texto extraído como archivo HTML"""
        html_content = f"<html><head><title>Extracted Text</title></head><body><pre>{text}</pre></body></html>"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

    def protectPDF_extractText(self, save_formats):
        """Función principal para extraer el texto del PDF y generar los formatos seleccionados"""
        text_output = ""
        # Convertir un PDF a una lista de imágenes
        pages = convert_from_path(self.ogfile, poppler_path=r'poppler-24.07.0\Library\bin')
        protectedPDF = PdfWriter()

        # Extraer texto de cada página
        for pagesnumber, image in enumerate(pages):
            extractedtxt = pytesseract.image_to_string(image)
            print("Text from page {}:".format(pagesnumber+1))
            print(extractedtxt)
            
            # Agregar texto extraído a la variable text_output
            text_output += f"Page {pagesnumber+1}:\n{extractedtxt}\n\n"

            bytesimage = BytesIO()
            image.save(bytesimage, format="PDF")
            bytesimage.seek(0)
            image_asPDF = PdfReader(bytesimage)
            protectedPDF.add_page(image_asPDF.pages[0])

        # Guardar el archivo protegido
        protectedPDF.encrypt(self.password)
        with open(self.protectedfile, "wb") as protectedfile:
            protectedPDF.write(protectedfile)

        # Generar los archivos según la elección del usuario
        if 'txt' in save_formats:
            self.save_as_txt(text_output, "extracted_text.txt")
        if 'pdf' in save_formats:
            self.save_as_pdf(text_output, "extracted_text.pdf")
        if 'docx' in save_formats:
            self.save_as_docx(text_output, "extracted_text.docx")
        if 'html' in save_formats:
            self.save_as_html(text_output, "extracted_text.html")

# Función para elegir los formatos
def choose_formats():
    print("Elige los formatos en los que deseas guardar el informe:")
    print("1. .txt")
    print("2. .pdf")
    print("3. .docx")
    print("4. .html")
    print("Escribe el número de las opciones separadas por coma (ejemplo: 1,3,4):")
    
    user_input = input()
    selected_formats = []
    
    # Procesar las opciones seleccionadas
    if '1' in user_input:
        selected_formats.append('txt')
    if '2' in user_input:
        selected_formats.append('pdf')
    if '3' in user_input:
        selected_formats.append('docx')
    if '4' in user_input:
        selected_formats.append('html')

    return selected_formats

# Ejemplo de uso
if __name__ == "__main__":
    # Archivos de entrada y salida
    ogfile = "quijote.pdf"
    protectedfile = "protected_file.pdf"
    password = "luvaacan"

    # Crear instancia de PDFshield
    shield = PDFshield(ogfile, protectedfile, password)

    # Elegir los formatos de salida
    save_formats = choose_formats()

    # Ejecutar la extracción de texto y la creación de los informes
    shield.protectPDF_extractText(save_formats)
