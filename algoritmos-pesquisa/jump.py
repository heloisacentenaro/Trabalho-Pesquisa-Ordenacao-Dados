"""Inicio do código de pesquisa com Jump Search"""
import math
from dados import Dados

def jumpsearch(vetor, elemento, intervalo):
    '''Classe do Jump Search''' 
    # Vai procurar o tamanho do salto
    salto = math.sqrt(intervalo)
    # Encontrando o bloco onde está o elemento
    bloco = 0
    while vetor[int(min(salto, intervalo)-1)] < elemento:
        bloco = salto
        salto += math.sqrt(intervalo)
    if bloco >= intervalo:
        return -1
    # Fazendo uma busca linear por x
    while vetor[int(bloco)] < elemento:
        bloco += 1
        # Se chegar próximo bloco ou final do vetor, o elemento não está presente
        if bloco == min(salto, intervalo):
            return -1
    # Se o elemento for encontrado
    if vetor[int(bloco)] == elemento:
        return bloco
    return -1

# Teste do código
dados = Dados()
nomes = Dados.nomes
MATRICULA = dados.geradormatricula()

pesquisa = input("\n Digite o nome que você deseja pesquisar: ")
ordenados = sorted(nomes)
encontrado = jumpsearch(ordenados, pesquisa, len(ordenados))
if encontrado != -1:
    print ("\n Nome encontrado na posição", int(encontrado))
    print(" Número da matrícula:", MATRICULA)
else:
    print ("Este nome não foi encontrado! ")
