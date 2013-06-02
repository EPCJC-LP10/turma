# -*- coding: utf-8 -*-

#
# Implementação de uma pilha recorrendo a lista
# © EPCJC
#

def pop(p):
	return p.pop()

def push(p, elem):
	p.append(elem)

def ver_topo(p):
	if len(p) == 0:
		print "Pilha vazia"
		return
		
	print p[-1]		
		

def inicializar(p):
	del p[:]
	print "Pilha Inicializada"


#
# Exemplo de Utilização
#

pilha = []

#inserir na pilha 
push(pilha, 5)
push(pilha, 10)

#retirar da pilha
pop(pilha)