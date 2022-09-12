import pandas as pd
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors

# UPLOAD DE ARQUIVOS PARA DATAFRAME

def GetFileClubs(path):
    """
    Upload do Arquivo com as Inscrições de Atletas
    """
    arquivo = path
    tabela_atletas = pd.read_excel(arquivo,
                                   sheet_name="ATLETAS",
                                   converters={"SIR":str})

    # Gerando a lista de CLUBES
    lista_clubes_order = tabela_atletas.sort_values(by=["CLUBE"])
    lista_clubes = lista_clubes_order["CLUBE"].unique().tolist()

    return lista_clubes, tabela_atletas

#----------------------------------------------------------------------

def GetFileRaces(path):
    """
    Upload do Arquivo com as Inscrições de Provas
    """
    arquivo = path
    dia_provas = str(input("Escolha SABADO ou DOMINGO: "))

    tabela_provas = pd.read_excel(arquivo,
                                  sheet_name=dia_provas,
                                  converters={"HORARIO":str})

    # Gerando a lista de PROVAS
    lista_provas_order = tabela_provas.sort_values(by=["NRO"])
    lista_provas = lista_provas_order["PROVA"].unique().tolist()

    return tabela_provas, lista_provas_order, lista_provas, dia_provas

# GERAÇÃO DAS TABELAS DE INSCRITOS

def GetAthletes(clube, tabela_atletas):
    """
    Gera a Lista de Atletas Inscritos por Clube
    """
    clube_inscritos = tabela_atletas.loc[tabela_atletas["CLUBE"] == clube, ("SIR","NOME","ATESTADO","CATEGORIA")].sort_values(by=["NOME"])
    clube_inscritos_lista = clube_inscritos.values.tolist()

    total_inscritos = f"<para>Total de atletas inscritos: {len(clube_inscritos_lista)}</para>"

    # Cabeçalho da Tabela
    p0 = Paragraph("<para align=center><b>SIR</b></para>")
    p1 = Paragraph("<b>NOME DO ATLETA</b>")
    p2 = Paragraph("<para align=center><b>ATESTADO</b></para>")
    p3 = Paragraph("<para align=center><b>CATEGORIA</b></para>")
    p4 = Paragraph(total_inscritos)

    content_table = [[p0, p1, p2, p3]]
    content_table.extend(clube_inscritos_lista)

    data_table_inscritos = content_table

    tabela = Table(data_table_inscritos, rowHeights=20)
    tabela.setStyle(TableStyle([
                          ('LINEBELOW',(0,0),(-1,-1),0.5,colors.grey),
                          ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                          ('ALIGN',(0,0),(0,-1),'CENTRE'),
                          ('ALIGN',(2,0),(2,-1),'CENTRE'),
                          ('ALIGN',(3,0),(3,-1),'CENTRE'),
                          ('FONT',(0,0),(-1,-1), "Helvetica"),
                          ('FONTSIZE', (0,0),(-1,-1), 10),
                          ('BACKGROUND',(0,0),(3,0), colors.lightgrey)
                          ]))

    return tabela, p4

#----------------------------------------------------------------------

def GetRaces(prova, lista_provas_order, lista_provas):
    """
    Gera a Lista de Atletas Inscritos por Prova
    """
    horario_prova = lista_provas_order.loc[lista_provas_order["PROVA"] == prova, ("HORARIO")].tolist()
    horario_prova_simples = horario_prova[0]

    nome_prova = "{0}. {1} – Prova {2}".format (lista_provas.index(prova)+1, horario_prova_simples[:-3], prova)

    lista_clubes = lista_provas_order.loc[lista_provas_order["PROVA"] == prova, ("CLUBE","NOME","EMPRESTIMO")].sort_values(by=["CLUBE", "NOME"])
    lista_clubes_prova = lista_clubes.values.tolist()

    # Cálculo da Quantidade de Barcos
    if ("2x" in nome_prova) or ("2-" in nome_prova):
        qtd_barcos = int(len(lista_clubes_prova)/2)
    elif ("4x" in nome_prova) or ("4-" in nome_prova):
        qtd_barcos = int(len(lista_clubes_prova)/4)
    elif "4+" in nome_prova:
        qtd_barcos = int(len(lista_clubes_prova)/5)
    elif "8+" in nome_prova:
        qtd_barcos = int(len(lista_clubes_prova)/9)
    else:
        qtd_barcos = len(lista_clubes_prova)

    # Cabeçalho da Tabela
    p0 = Paragraph("<para align=center><b>CLUBE</b></para>")
    p1 = Paragraph("<b>NOME DO ATLETA</b>")
    p2 = Paragraph("<para align=center><b>EMPRÉSTIMO</b></para>")
    p3 = Paragraph(F"<para spaceBefore=8>Total de barcos inscritos: {qtd_barcos}</para>")

    content_table = [[p0, p1, p2]]
    content_table.extend(lista_clubes_prova)

    data_table_inscritos = content_table

    tabela=Table(data_table_inscritos, rowHeights=20)
    tabela.setStyle(TableStyle([
                          ('LINEBELOW',(0,0),(-1,-1),0.5,colors.grey),
                          ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                          ('ALIGN',(0,0),(0,-1),'CENTRE'),
                          ('ALIGN',(2,0),(2,-1),'CENTRE'),
                          ('ALIGN',(3,0),(3,-1),'CENTRE'),
                          ('FONT',(0,0),(-1,-1), "Helvetica"),
                          ('FONTSIZE', (0,0),(-1,-1), 10),
                          ('BACKGROUND',(0,0),(3,0), colors.lightgrey)
                          ]))

    return tabela, p3, nome_prova
