'''Random: utilizado para gerar números pseudo-aleatórios'''
import random

class Dados:
    '''Vai receber a matrícula e o nome a ser pesquisado'''
    nomes = [
        "Alice",
        "Alana",
        "Benjamin",
        "Bianca",
        "Carol",
        "Daniel",
        "Daiane"
        "Eduarda",
        "Evandro",
        "Felipe",
        "Fernanda",
        "Gabriela",
        "Gustavo",
        "Henrique",
        "Helena",
        "Isabela",
        "Isadora",
        "Ismael",
        "Joaquim",
        "Jaqueline",
        "Laura",
        "Lucas",
        "Mateus",
        "Natalia",
        "Olivia",
        "Pedro",
        "Patrique", 
        "Patricia",
        "Rosana",
        "Raissa"]
    def geradornome(self):
        '''Retorna um nome de uma posição aleatória do vetor de nomes'''
        posicao = random.randint(0, len(self.nomes)-1)
        # Dá um valor a menos na posição porque aqui diminui 1
        return self.nomes[posicao]

    def geradormatricula(self):
        '''Retorna um número de matrícula no formato XXXX, onde X é um dígito aleatório'''
        matricula = ""
        for _ in range(7):
            matricula += str(random.randint(0, 9))
            # random.randint(0, 9) gera um número inteiro aleatório entre 0 e 9.
            # Em seguida, converte o inteiro para string.
        return matricula

    def geradoraluno(self, aluno):
        '''Retorna as informações do aluno, contendo matrícula e nome'''
        aluno = {}
        aluno["Matricula"] = self.geradormatricula()
        aluno["Nome"] = self.geradornome()
        return aluno
