
from reportlab.pdfgen import canvas
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import cm
from datetime import datetime
import pytz


# Tamanho Página ReportLab A4
largura = defaultPageSize[0]
altura = defaultPageSize[1]

# Data de Atualização do Arquivo
timezone = pytz.timezone("America/Sao_Paulo")
data = datetime.now(timezone).strftime("%d/%m/%Y %H:%M")

# Input com Nome do Evento
nome_evento = str(input("Nome do evento: "))

# TEMPLATES

def FirstPageAtletas(canvas, template):
    """
    Template da Primeira Página de Atletas
    """
    canvas.saveState()

    canvas.setFont("Helvetica", 10)
    canvas.drawString(1.7*cm, 28.2*cm, nome_evento)
    canvas.drawRightString(largura-1.7*cm, 28.2*cm, "Atualizado em " + str(data))
    canvas.line(1.7*cm,28*cm,largura-1.7*cm,28*cm)

    canvas.setFont("Helvetica-Bold", 24)
    canvas.drawCentredString(largura/2, 26.5*cm, "Lista de Inscritos por Clube")

    canvas.restoreState()

#----------------------------------------------------------------------

def FirstPageProvas(canvas, template):
    """
    Template da Primeira Página de Provas
    """
    canvas.saveState()

    canvas.setFont("Helvetica", 10)
    canvas.drawString(1.7*cm, 28.2*cm, nome_evento)
    canvas.drawRightString(largura-1.7*cm, 28.2*cm, "Atualizado em " + str(data))
    canvas.line(1.7*cm,28*cm,largura-1.7*cm,28*cm)

    canvas.setFont("Helvetica-Bold", 24)
    canvas.drawCentredString(largura/2, 26.5*cm, "Lista de Inscritos por Prova")

    canvas.restoreState()

#----------------------------------------------------------------------

def LaterPages(canvas, template):
    """
    Template das Páginas Seguintes
    """
    canvas.saveState()

    canvas.setFont("Helvetica", 10)
    canvas.drawString(1.7*cm, 28.2*cm, nome_evento)
    canvas.drawRightString(largura-1.7*cm, 28.2*cm, "Atualizado em " + str(data))
    canvas.line(1.7*cm,28*cm,largura-1.7*cm,28*cm)

    canvas.restoreState()
