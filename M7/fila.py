# -*- coding: utf-8 -*-

#
# Implementação de uma fila recorrendo a lista
# © EPCJC
#

def remover(l):
	return l.pop(0)

def inserir(l, elem):
	l.append(elem)

def inicializar(l):
	del l[:]
	print "Fila Inicializada"

def visualizar(l):
	for elem in l:
		print elem, 
		
	print


#
# Exemplo de Utilização
#

fila = []

#inserir na fila 
inserir(fila, 5)
inserir(fila, 10)
inserir(fila, 20)

visualizar(fila)

#remover da fila
remover(fila)
print "Retirei primeiro elemento da fila"

visualizar(fila)