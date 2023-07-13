'''Inicio do programa de pesquisa com Tabela Hash'''
from dados import Dados
class HashSearch:
    '''Classe que implementa a pesquisa na tabela hash'''
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash_function(self, chave):
        '''Função que calcula o índice na tabela hash a partir da chave'''
        # Aqui, está usando a função interna hash do python e
        # aplicando o módulo % pelo tamanho da tabela para obter o índice
        return hash(chave) % self.tamanho

    def hash_search(self, chave):
        '''Função de pesquisa na tabela'''
        index = self.hash_function(chave)
        for i, item in enumerate(self.tabela[index]):
            if item[0] == chave:
                return i
        return -1
# Teste do código
tabela = HashSearch(30)
dados = Dados()
nomes = Dados.nomes
MATRICULAS = []

# Inserção dos dados na tabela
for nome in nomes:
    MATRICULA = dados.geradormatricula()
    tabela.tabela[tabela.hash_function(nome)].append((nome, MATRICULA))
    MATRICULAS.append(MATRICULA)

# Pesquisa na tabela hash
pesquisa = input("\nDigite o nome que você deseja pesquisar: ")
encontrado = tabela.hash_search(pesquisa)
if encontrado != -1:
    achou_nome, achou_matricula = tabela.tabela[tabela.hash_function(pesquisa)][encontrado]
    print("\nNome encontrado!")
    print("Matrícula:", achou_matricula)
else:
    print("Este nome não foi encontrado!")
