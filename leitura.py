import re

def categorias():
    f = open("train.txt","r",encoding='utf-8')
    txt = f.read()
    categorias = []
    numero = []
    aux = []
    count = 1
    div = re.split(r'B',txt)
    for c in div:
        e = re.search(r'^-([A-Z_]{2,})',c)
        if(e):
            categorias.append(e.group(1))   

    categorias.sort()
    nome = categorias[0]
    length = len(categorias)
    i = 1
    while(i < length):
        if(categorias[i] == nome):
            count = count + 1 
        else:
            par = (nome,count)
            numero.append(par)
            nome = categorias[i]
            count = 1
        i+=1  
    par = (nome,count)
    numero.append(par)     
    return numero


def conteudo():
    f = open("train.txt","r",encoding='utf-8')
    txt = f.read()
    c = []
    div = re.split(r'B',txt)
    for texto in div:
        cont = re.findall(r'[^O]\t(.+)',texto) 
        inf = ' '.join(cont)
        nome = re.search(r'[A-Z_]{2,}',texto)
        if(nome):
            parAux = (nome.group(),inf)
            c.append(parAux)
    return c
          


def htmlConteudo(categoria ,conteudo):
    final = "html/" + categoria + ".html"
    f = open(final,"w",encoding='utf-8')
    f.write(f'''<!DOCTYPE html>
    <html>
        <head>
    <title>{categoria}</title>
        <meta charset="UTF-8"/>
    </head>
    <body>
        <h1>{categoria}</h1>
        <h2><a href= ../projetoWEB.html>
        <blockquote>Informação</blockquote>
        </a></h2>
        <ul>''')
    for (cat,text) in conteudo:
        if(cat == categoria):
            f.write(f'<li>{text}</li>')
    f.write(f'''  </ul></body>
    </html>''')
    return final


def html(categoria,conteudo):
    f = open("projetoWEB.html","w",encoding='utf-8')
    f.write("""<!DOCTYPE html>
    <html>
        <head>
    <title>Train</title>
        <meta charset="UTF-8"/>
    </head>
    <body>
        <h1>Trabalho 1</h1>
        <h2>Abril de 2021</h2>
        <h3>Autoras</h3>
        <ul>
            <li>A89525: Maria Quintas Barros</li>
            <li>A89535: Maria Beatriz Araújo Lacerda</li>
            <li>A89536: Ana Teresa Gião Gomes</li>
        </ul>
        <h3>Categorias:</h3>""")
    i = len(categoria)
    for (a,b) in categoria:
        ficheiro = htmlConteudo(str(a),conteudo)
        f.write(f'''<p> {str(a)} ({b}) </p> 
        <a href= {ficheiro}>
        <blockquote>Informação</blockquote>
        </a>''')
    f.write(f'''  </body>
</html>''')


        


