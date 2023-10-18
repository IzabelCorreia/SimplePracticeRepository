import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Seleciona uma pasta")

lista_de_arquivo = os.listdir(caminho)

locais = {
    "imagens": [".png", ".png"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": [".csv"],
}

for arquivo in lista_de_arquivo:
    nome, estensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if estensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
