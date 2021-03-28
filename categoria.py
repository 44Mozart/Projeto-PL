import re

f = open("train.txt", "r",encoding='utf-8')

categorias = []
conteudo = []
count = 0
final = []

linha = f.read()
div = re.split(r'\n\n',linha)
for conj in div:
    e = re.search(r'(B\-.+)(\nI\-.+)*',conj)
    if(e):
        nome = re.findall(r'B\-(.+)\t.+',e.group(1))
        if(nome):
            for i in nome:
                categorias.append(i)
    if(e):
        soCate = re.split(r'B',e.group())
        for texto in soCate:
            cont = re.findall(r'\t(.+)',texto) 
            inf = ' '.join(cont)
            nome = re.search(r'[A-Z]{2,}',texto)
            if(nome):
                parAux = (nome.group(),inf)
                conteudo.append(parAux)

# Neste momento já temos a informação todo!
         
categorias.sort()
nome = categorias[1]

for cat in categorias:
    if(cat == nome):
        count = count + 1
    else:
        par = (nome,count)
        final.append(par)
        nome = cat







    