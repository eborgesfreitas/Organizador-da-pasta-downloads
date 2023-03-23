import os

cwb = os.getcwd()

folder_list = []

for i in os.listdir(cwb):
    if os.path.isdir(i):
        folder_list.append(i)

for folder in folder_list:
    caminho = os.path.join(cwb,folder)

    files = os.listdir(caminho)
    for file in files:
        caminho_final = os.path.join(caminho, file)
        destino = os.path.join(cwb, file)
        os.replace(caminho_final, destino)
    os.rmdir(caminho)
    

