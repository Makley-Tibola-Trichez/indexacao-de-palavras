import glob, os, time, codecs, sys

stopwords = []
nome_arq = 'stopwords.txt'

arq = codecs.open(nome_arq, "r", "UTF-8")
linhas = arq.readlines()
for linha in linhas:    
    stopwords.append(linha.replace('\n', '').strip().lower())
arq.close()

def opcaoInvalida():
    print("========================================================")
    print("                   opção invalida!")
    print("========================================================")
    time.sleep(2)

def lendoarquivo(nomeArquivo):
    docNormal = ''
    filename = 'docs/' + nomeArquivo
    f = codecs.open(filename, 'r', "UTF-8")
    for linha in f:
        # remove espaços em branco no inicio e fim de cada linha lida
        docNormal += linha.strip()
    f.close()

    # print(docNormal)
    return docNormal
    

def lendoarquivos():
    for arq in glob.glob("docs/*.txt"):
        print("[{}]".format(arq))
        docTemporario = ''
    
        # Abrir arquivo
        f = codecs.open(arq, "r", "UTF-8")
        linhas = f.readlines()

        for linha in linhas:
            # remove espaços em branco no inicio e fim de cada linha lida
            docTemporario += linha.strip()
        f.close()

        print(docTemporario)
        print()

def criandoarquivo(nomeArquivo):
    filename = 'docs/' + nomeArquivo
    f = codecs.open(filename, 'x', "UTF-8")
    f.close()

def escrevendoarquivo(nomeArquivo, texto):
    filename = 'docs/' + nomeArquivo
    f = codecs.open(filename, 'w', "UTF-8")
    f.write(texto)
    f.close()

def remove_stopwords(lista):
    nova_lista = []

    for token in lista:
        if token.lower() not in stopwords:
            nova_lista.append(token)

    return nova_lista

def tokenizacao(doc_inicial):
    return doc_inicial.split(' ')

def substituir_especiais(token):
        
    for i in range(len(token)):
        if (token[i] == 'á' or token[i] == 'ã' or token[i] == 'â' or token[i] == 'à' or token[i] == 'ä'):
            token = token.replace(token[i], 'a')
            print("a")
        elif (token[i] == 'ç'):
            token = token.replace(token[i], 'c')
            print("c")
        elif (token[i] == 'é' or token[i] == 'ê' or i == 'ë'):
            token = token.replace(token[i], 'e')
            print("e")
        elif (token[i] == 'í' or token[i] == 'ï'):
            token = token.replace(token[i], 'i')
            print("i")
        elif (token[i] == 'ó' or token[i] == 'õ' or token[i] == 'ô' or token[i] == 'ö'):
            token = token.replace(token[i], 'o')
            print("o")
        elif (token[i] == 'ú' or token[i] == 'ü'):
            token = token.replace(token[i], 'u')
            print("u")

    return token

def normalizacao(lista):
    token = ''
    nova_lista = []
    pontuacoes = '!()[]{};:\'\"\,<>.?@#%^&*_~'
    
    for i in range(len(lista)):
        for j in lista[i]:
            if (j in pontuacoes):
                continue
            else:
                # substituir_especiais(j)
                token += j.lower()
        nova_lista.append(token)
        token = ''
        
    return nova_lista
    

"""
docTemporario = ''
arq = "Docs/doc1.txt"
f = codecs.open(arq, "r", "UTF-8")
linhas = f.readlines()

for linha in linhas:
        # remove espaços em branco no inicio e fim de cada linha lida
        docTemporario += linha.replace('\r\n',' ')
f.close()

docTemporario = tokenizacao(docTemporario)
docTemporario = remove_stopwords(docTemporario)
# docTemporario = normalizacao(docTemporario)

print(docTemporario)

docTemporario = normalizacao(docTemporario)

print(docTemporario)

# print(docTemporario)
# print(normalizacao(tokenizacao(lendoarquivo(docTemporario))))
"""

# ! primeiro  tokenizacao           ok
# ! segundo   remove_stopwords      ok
# ! terceiro  normalizacao          ok
# ! quarto    substituir_especiais 
# ! quinto    indexacao

carac = 'Com a vitória sobre o Uruguai, o Brasil chegou a 12 pontos e lidera as Eliminatórias da Copa do Mundo FIFA Catar 2022. Arthur vê a Seleção em boa situação na busca por uma vaga na Copa do Mundo, mas sabe que cada partida deve apresentar ainda mais dificuldade. "Nosso objetivo é esse (conquistar a classificação). Estamos trabalhando forte em busca do nosso objetivo. Sempre temos algo a melhorar. A gente não entrou pensando que estamos invictos, pois cada jogo é diferente e difícil. Estamos em um bom caminho, confiamos na comissão técnica e eles confiam na gente. Agora é seguir trabalhando e buscando essa classificação para o Mundial", concluiu.'


# # substitui
# ca = (carac.replace(carac[9], 'o'))
# # volta a não estar substituido
# print(carac)


print(substituir_especiais(carac))