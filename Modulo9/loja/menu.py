# -*- coding: utf-8 -*-

def principal():
    print
    print " **** MENU ****** "
    print
    print "   1. Gestão de Produtos"
    print "   2. ...... (não implementado)"
    print
    print "   0. Sair"
    print

    op = raw_input("Opção: ")
    return op


def produtos():
    print
    print " *** Menu Produtos **** "
    print
    print("1: Inserir novo artigo")
    print("2: Pesquisar por um artigo")
    print("3: Modificar quantidade em stock de um artigo")
    print("4: Apresentar dados de todos os artigos");
    print "5. Eliminar artigo\n"
    print("0: menu anterior\n");

    op = raw_input("Opção: ")
    return op



if __name__ == "__main__":
    print "Este programa não deve ser executado diretamente"
