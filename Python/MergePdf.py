import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista_de_arquivos = os.listdir("nome_pasta")
lista_de_arquivos.sort()

for arquivo in lista_de_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivo/{arquivo}")

merger.write("Arquivo_Final.pdf")
