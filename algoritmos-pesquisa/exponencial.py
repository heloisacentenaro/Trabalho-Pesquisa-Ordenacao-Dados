'''Código que implementa uma pesquisa Exponencial'''
from dados import Dados
def pesquisabinaria(vetor, low, high, element):
    '''Função que faz uma pesquisa binaria'''
    while low < high:
        posicao = low + (high - low) // 2
        # Encontrou
        if vetor[posicao] == element:
            return posicao
        # Pesquisando no sub array esquerdo
        elif element < vetor[posicao]:
            high = posicao -1
        # Pesquisando no sub array direito
        else:
            low = posicao +1
    # Não encontrou
    return -1

def exponencialsearch(array, tamanho, elemento):
    '''Função que faz a pesquisa exponencial'''
    limite = 1
    while limite < tamanho and array[limite] < elemento:
        limite *= 2
    return pesquisabinaria(array, limite // 2, min(limite, tamanho-1), elemento)
# min: função incorporada que retorna o valor mínimo entre dois ou mais argumentos.

# Teste do código
dados = Dados()
nomes = dados.nomes
MATRICULA = dados.geradormatricula()

pesquisa = input("\n Digite o nome que você deseja pesquisar: ")
local = nomes.index(pesquisa) if pesquisa in nomes else -1

if local != -1:
    print("\nNome encontrado na posição: ", local)
    print("Matrícula:", MATRICULA)
else:
    print("Este nome não foi encontrado!")
