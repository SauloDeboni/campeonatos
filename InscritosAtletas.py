from reportlab.platypus import SimpleDocTemplate, PageBreak, Spacer, Paragraph
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.units import cm
from datetime import datetime
import pytz
from functions.data import GetFileClubs, GetAthletes
from functions.pages import FirstPageAtletas, LaterPages


timezone = pytz.timezone("America/Sao_Paulo")
data = datetime.now(timezone).strftime("%Y-%m-%d")

def Atletas(path):
    """
    Gera o arquivo com a lista de atletas por clube
    """
    nome_arquivo = f"Lista-Atletas-{data}.pdf"
    template = SimpleDocTemplate(nome_arquivo,
                                 leftMargin=1.5*cm,
                                 rightMargin=1.5*cm)

    lista, tabela_atletas = GetFileClubs(path)

    h1 = PS(name = 'Heading1', fontName ="Helvetica-Bold", fontSize = 16, leading = 28)

    Story = [Spacer(1,2*cm)]

    for clube in lista:
        tabela, p4 = GetAthletes(clube, tabela_atletas)

        Story.append(Paragraph(clube, h1))
        Story.append(tabela)
        Story.append(Spacer(1,0.5*cm))
        Story.append(p4)
        Story.append(PageBreak())

    template.build(Story, onFirstPage=FirstPageAtletas, onLaterPages=LaterPages)

    print()
    print(f"Seu arquivo {nome_arquivo} foi gerado com sucesso!")

if __name__ == "__main__":
    Atletas(path=input("Qual o path do arquivo? "))
