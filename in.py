import os

cwb = os.getcwd()
full_list = os.listdir(cwb)

#percorrendo arquivos da pasta
files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]
types = list(set([i.split('.')[-1] for i in files_list]))


#criando as pastas
for file_type in types:
    if file_type not in os.listdir():
        os.mkdir(file_type)


for file in files_list:
    origem = os.path.join(cwb, file)
    destino = os.path.join(cwb, file.split('.')[-1], file)
    os.replace(origem, destino)

