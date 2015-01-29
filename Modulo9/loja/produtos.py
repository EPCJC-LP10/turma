# -*- coding: utf-8 -*-


#
# Os elementos da lista são mantidos ordenados (por código de artigo)
# © EPCJC
#


from collections import namedtuple
import menu

Artigo = namedtuple("Artigo", "codigo, nome, stock")

listaArtigos = []



def encontra_artigo(codigo, apresentar=False):
    ''' Procura por código já existente.

        Pesquisa por um código de artigo nos artigos
        já inseridos. Se encontra o código, devolve o valor -1;
        em caso contrário, devolve a posicão onde vai ser inserido
        o novo registo

    '''

    posicao = -1
    encontrou = False

    for i in range(len(listaArtigos)):
        registo = listaArtigos[i]
        if registo.codigo == codigo:
            encontrou = True
            if apresentar == True:
                print("Código Artigo     Nome                Quantidade em stock")
                print("%7d           %-20s%11d") % (registo.codigo, registo.nome, registo.stock)

            break

        if registo.codigo > codigo:
            posicao = i
            break

    if encontrou:
        posicao = -1

    if not encontrou and posicao == -1:     # adicionar (append) à lista
        posicao = len(listaArtigos)

    #print posicao
    return posicao


def posicao_artigo(codigo):
    ''' Encontra a posicao onde se encontra um artigo.

        Pesquisa por um código de artigo nos artigos
        já inseridos. Se NÃO encontra o código, devolve o valor -1;
        caso contrário, devolve a posicão do artigo dentro da lista

    '''


    for posicao in range(len(listaArtigos)):
        registo = listaArtigos[posicao]
        if registo.codigo == codigo:
            return posicao


    return -1   # não encontrou




def inserir():
    codigo = input("Introduza código do artigo: ")
    posicao = encontra_artigo(codigo)
    if posicao == -1:
        print("Código já existente.\n")
        return

    # ler os restantes dados do registo
    nome = raw_input("Introduza nome do artigo: ")
    stock = input("Introduza quantidade em stock inicial: ")


    # Criar o novo registo
    novo_registo = Artigo(codigo, nome, stock)

    # Adicionar o registo à lista na posição correta (manter a lista ordenada)
    listaArtigos.insert(posicao, novo_registo)



def listar_todos():
	print("Código Artigo     Nome                Quantidade em stock")
	for registo in listaArtigos:
		print("%7d           %-20s%11d") % (registo.codigo, registo.nome, registo.stock)



def pesquisar():
    codigo = input("Introduza código do artigo: ")
    posicao = encontra_artigo(codigo, apresentar=True)
    if posicao != -1:
        print "Artigo inexistente."


def alterar_stock():
    codigo = input("Introduza codigo do artigo: ")
    posicao = posicao_artigo(codigo)
    if posicao >= 0:
        alteracao = input("Introduza alteração de stock: ")
        listaArtigos[posicao] = listaArtigos[posicao]._replace(stock = alteracao)
    else:
        print("Artigo inexistente.")

def eliminar():
    codigo = input("Introduza codigo do artigo: ")
    posicao = posicao_artigo(codigo)
    if posicao >= 0:
        confirma = raw_input("Tem a certeza? (s/n) ")
        if confirma in ['s', 'S']:
            listaArtigos.pop(posicao)
    else:
        print("Artigo inexistente.")

def gerir():

    terminar = False

    while not terminar:
        op = menu.produtos()

        if op == '1':
            inserir()
        elif op == '2':
            pesquisar()
        elif op == '3':
            alterar_stock()
        elif op == '4':
            listar_todos()
        elif op == '5':
            eliminar()
        elif op == '0':
            terminar = True
        else:
    		print("Opção inválida\n");
