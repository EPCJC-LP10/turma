# -*- coding: utf-8 -*-

import menu
import produtos
import util


# nome dos ficheiros
fxProdutos = "fxProdutos.dat"

def ler_ficheiros():
	# adicionar todos ficheiros a ler
	produtos.listaArtigos = util.ler_ficheiro(fxProdutos)


def escrever_ficheiros():
	# adicionar todos ficheiros a guardar
	util.escrever_ficheiro(fxProdutos, produtos.listaArtigos)



# Bloco Principal

ler_ficheiros()

terminar = False
while not terminar:
    op = menu.principal()

    if op == '1':
        produtos.gerir()
    elif op == '2':
        pass    #por fazer
    elif op == '0':
        terminar = True


escrever_ficheiros()
