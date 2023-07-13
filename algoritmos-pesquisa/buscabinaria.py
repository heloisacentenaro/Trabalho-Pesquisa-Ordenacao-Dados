'''Implementação do algoritmo de pesquisa - Árvore de Busca Binária'''
from dados import Dados

class Arvore:
    ''' Construtor para criar um nó'''
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None

def arvorebinaria(root, valor):
    '''Função para pesquisar na árvore'''
    # Caso base: a raiz é nula ou está presente na raiz (root = raiz)
    if root is None or root.valor == valor:
        return root
    # O valor é maior que o valor da raiz
    if root.valor < valor:
        return arvorebinaria(root.right, valor)
    # O valor é menor que o valor da raiz
    return arvorebinaria(root.left, valor)

# Teste do código
dados = Dados()
nomes = Dados.nomes
MATRICULA = dados.geradormatricula()

pesquisa = input("\n Digite o nome que você deseja pesquisar: ")
ordenados = sorted(nomes)
raiz = Arvore(ordenados[0])
for nome in ordenados[1:]:
    node = Arvore(nome)
    current = raiz
    while True:
        if nome < current.valor:
            if current.left is None:
                current.left = node
                break
            else:
                current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            else:
                current = current.right

encontrado = arvorebinaria(raiz, pesquisa)

if encontrado is not None:
    print("\nNome encontrado na posição", ordenados.index(encontrado.valor))
    print("Número da matrícula:", MATRICULA)
else:
    print("Este nome não foi encontrado!")
