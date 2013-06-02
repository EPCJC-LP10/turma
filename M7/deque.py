# -*- coding: utf-8 -*-

#
# Implementação de uma fila recorrendo a deque (mais eficiente)
# © EPCJC
#

from collections import deque

def remover(q):
	return q.popleft()

def inserir(q, elem):
	q.append(elem)

def inicializar(l):
	q.clear()
	print "Fila Inicializada"

def visualizar(q):
	for elem in q:
		print elem, 
		
	print


#
# Exemplo de Utilização
#

fila = deque()

#inserir na fila 
inserir(fila, "Rui")
inserir(fila, "Eva")
inserir(fila, "Ana")

visualizar(fila)

#remover da fila
remover(fila)
print "Retirei primeiro elemento da fila"

visualizar(fila)