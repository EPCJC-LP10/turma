# -*- coding: utf-8 -*-

#
# Utilização de uma lista de registos com inserção ordenada (por campo id)
# Não verifica repetição do campo id
# © EPCJC
#

from collections import namedtuple


def inserir(lista):
	id = input("Introduza código ")
	nome = raw_input("Introduza nome: ")
	contato = raw_input("Introduza contato: ")
	
	novo = contatoReg(id, nome, telefone)
	inserir_ordenado(lista, novo)


def inserir_ordenado(lista, registo):
	pos = 0
	for i in range(len(lista)):
		if lista[i].id > registo.id:			
			break
		pos = pos + 1

	
	lista.insert(pos, registo)
	

def visualizar(lista):
	for registo in lista:
		print "      id: ", registo.id
		print "    Nome: ", registo.nome
		print "Telefone: ", registo.telefone	
		print "=" * 50
		print
	print


#
# Exemplo com registos com campos (id, nome, telefone)
#

contatoReg = namedtuple("contatoReg", "id, nome, telefone")

contatos = []
 
# Pedir os dados de cada registo 
#inserir(contatos)
#inserir(contatos)
#inserir(contatos)

rui = contatoReg(4, "Rui", "914123456")
inserir_ordenado(contatos, rui)

eva = contatoReg(1, "Eva", "967098098")
inserir_ordenado(contatos, eva)

ana = contatoReg(6, "Ana", "935456891")
inserir_ordenado(contatos, ana)

visualizar(contatos)
