import glob, time, codecs, nltk, pickle


# """"""""""""""" Printa um erro caso digite uma opcao que n existe """""""""""""""""""""
def opcao_invalida():
    print("========================================================")
    print("                   opção invalida!")
    print("========================================================")
    time.sleep(2)


# """"""""""""""""""""""" Le um arquivo txt da pasta Docs """""""""""""""""""""""""""""""
def lendo_arquivo(nome_arquivo):
    doc_normal = ''
    filename = 'docs/' + nome_arquivo
    f = codecs.open(filename, 'r', "UTF-8")
    for linha in f:
        # remove espaços em branco no inicio e fim de cada linha lida
        doc_normal += linha.strip()
    f.close()

    # print(docNormal)
    return doc_normal


# """"""""""""""""""""" Le todos os arquivos txt da pasta Docs """""""""""""""""""""""""""
def lendo_arquivos():
    for arq in glob.glob("docs/*.txt"):
        print("[{}]".format(arq))
        doc_temporario = ''

        # Abrir arquivo
        f = codecs.open(arq, "r", "UTF-8")
        linhas = f.readlines()

        for linha in linhas:
            # remove espaços em branco no inicio e fim de cada linha lida
            doc_temporario += linha.strip()
        f.close()

        print(doc_temporario)
        print()


# """"""""""" Cria um novo arquivo se n existir, e se existir da um erro """""""""""""""""
def criando_arquivo(nome_arquivo):
    filename = 'docs/' + nome_arquivo
    f = codecs.open(filename, 'x', "UTF-8")
    f.close()


# """"""""""""""""""" Escreve uma mensagem dentro de certo arquivo """""""""""""""""""""""
def escrevendo_arquivo(nome_arquivo, texto):
    filename = 'docs/' + nome_arquivo
    f = codecs.open(filename, 'w', "UTF-8")
    f.write(texto)
    f.close()


# """"""""""" Remove todas as stopwords que contém no arquivo stopwords.txt """""""""""""""
def remove_stopwords(lista, stopwords):
    nova_lista = []

    for token in lista:
        if token.lower() not in stopwords and token.lower() != '':
            nova_lista.append(token)

    return nova_lista


# """"""""""""""""" Separa numa lista as palavras através dos espaços """""""""""""""""""""
def tokenizacao(doc_inicial):
    return doc_inicial.split(' ')


# """"" Substitui as letra com caracteres especiais por letras sem o caracter  """"""""""""
def substituir_especiais(token):
    for i in range(len(token)):
        if (token[i] == 'á' or token[i] == 'ã' or token[i] == 'â' or token[i] == 'à' or token[i] == 'ä'):
            token = token.replace(token[i], 'a')
        elif (token[i] == 'ç'):
            token = token.replace(token[i], 'c')
        elif (token[i] == 'é' or token[i] == 'ê' or i == 'ë'):
            token = token.replace(token[i], 'e')
        elif (token[i] == 'í' or token[i] == 'ï'):
            token = token.replace(token[i], 'i')
        elif (token[i] == 'ó' or token[i] == 'õ' or token[i] == 'ô' or token[i] == 'ö'):
            token = token.replace(token[i], 'o')
        elif (token[i] == 'ú' or token[i] == 'ü'):
            token = token.replace(token[i], 'u')

    return token


# """""""""""""""""""""""""""""" Remove os numeros """"""""""""""""""""""""""""""""
def remove_numeros(token):
    nova_lista = []
    lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for i in range(len(token)):
        if (token[i] not in lista_numeros):
            nova_lista.append(token[i])

    return nova_lista


# """""""""""""""""""""""" Remove os numeros em extenso """"""""""""""""""""""""""
def remove_numeros_extenso(lista):
    numeros_extenso = []
    nova_lista = []
    nome_arq = 'numeros.txt'

    arq = codecs.open(nome_arq, "r", "UTF-8")
    linhas = arq.readlines()
    for linha in linhas:
        numeros_extenso.append(linha.replace('\n', '').strip().lower())
    arq.close()

    for token in lista:
        if token.lower() not in numeros_extenso and token.lower() != '':
            nova_lista.append(token)

    return nova_lista


# """"""" Retira as pontuações, e faz os metodo de substituir especiais e remover numeros """"""""
def normalizacao(linha):
    token = ''
    nova_lista = []
    pontuacoes = '!()[]{};:\'\"\,<>.?@#%^&*_~ºª'

    linha_final = substituir_especiais(linha)
    linha_final = remove_numeros(linha_final)

    for i in range(len(linha_final)):
        for j in linha_final[i]:
            if (j in pontuacoes):
                continue
            else:
                token += j.lower()
        nova_lista.append(token)
        retorno = "".join(nova_lista)
        token = ''

    return retorno


# """""""""""""""""""""""" Remove as palavras repetidas """"""""""""""""""""""""""
def remove_repetidas(lista):
    conjunto = set(lista)
    return conjunto


# """""""""""" Faz o processo de stemming = deixa a palavra no radical """"""""""""
def stemming(lista):
    stm = []
    stemmer = nltk.stem.RSLPStemmer()
    for i in lista:
        stm.append(stemmer.stem(i))

    return stm


# """""""""""" Faz a indexação da palavra com os doc no dicionario """"""""""""""""
def indexacao(doc, arq, dicio):
    # doc: list | arq: str (nome do arquivo)
    for palavra in doc:
        if palavra in dicio:
            lista_docs = dicio[palavra]
            lista_docs.append(arq)
        else:
            dicio[palavra] = [arq]


# """""""""""""""""""""" Grava o dicionario no dicionario.txt """""""""""""""""""""
def gravar_dic_arquivo(arquivo, dicionario):
    arq = open(arquivo, 'wb')
    pickle.dump(dicionario, arq)
    arq.close()


# """""""""""""""""""""" Le o arquivo dicionario.txt """"""""""""""""""""""""""""""
def ler_dic_arquivo(arquivo):
    arq = open(arquivo, 'rb')
    dicionario = pickle.load(arq)
    arq.close()
    return (dicionario)


# """""""""""""""""""""" abre arquivo stopwords.txt """"""""""""""""""""""""""""""
def abrir_stopwords():
    stopwords = []
    nome_arq = 'stopwords.txt'

    arq = codecs.open(nome_arq, "r", "UTF-8")
    linhas = arq.readlines()
    for linha in linhas:
        linha = substituir_especiais(linha)
        stopwords.append(linha.replace('\n', '').strip().lower())
    arq.close()

    return stopwords


# """""""""""""""""""""" métodos opção 3.x""""""""""""""""""""""""""""""""""""""

def encontrar_termos_union(arquivos_busca, termos_obtidos):
    return termos_obtidos.union(arquivos_busca)


def encontrar_termos_intersect(arquivos_busca, termos_obtidos):
    return termos_obtidos.intersection(arquivos_busca)

