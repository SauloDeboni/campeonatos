from reportlab.platypus import SimpleDocTemplate, PageBreak, Spacer, Paragraph
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.units import cm
from datetime import datetime
import pytz
from functions.data import GetFileRaces, GetRaces
from functions.pages import FirstPageProvas, LaterPages


timezone = pytz.timezone("America/Sao_Paulo")
data = datetime.now(timezone).strftime("%Y-%m-%d")

def Provas(path):
    """
    Gera o arquivo com a lista de atletas por clube
    """
    tabela_provas, lista_provas_order, lista_provas, dia_provas = GetFileRaces(path)

    nome_arquivo = f"Lista-Provas-{dia_provas}-{data}.pdf"
    template = SimpleDocTemplate(nome_arquivo,
                                 leftMargin=1.5*cm,
                                 rightMargin=1.5*cm)

    h1 = PS(name = 'Heading1', fontName ="Helvetica-Bold", fontSize = 16, leading = 28)

    Story = [Spacer(1,2*cm)]

    for prova in lista_provas:
        tabela, p3, nome_prova = GetRaces(prova, lista_provas_order, lista_provas)

        Story.append(Paragraph(nome_prova, h1))
        Story.append(tabela)
        Story.append(Spacer(1,0.5*cm))
        Story.append(p3)
        Story.append(PageBreak())

    template.build(Story, onFirstPage=FirstPageProvas, onLaterPages=LaterPages)

    print()
    print(f"Seu arquivo {nome_arquivo} foi gerado com sucesso!")

if __name__ == "__main__":
    Provas(path=input("Qual o path do arquivo? "))
