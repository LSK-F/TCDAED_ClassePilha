from array import array
from classe_Pilha import PilhaCheiaErro, PilhaVaziaErro, Pilha

class Torre_de_Hanoi:
    def __init__(self, discos):
        self.__discos = discos
        self.__passos = 0
        self.torres = {
            'A': Pilha(discos, 'i'),
            'B': Pilha(discos, 'i'),
            'C': Pilha(discos, 'i')
        }
        self.haste_A()
        self.visualizar()

    def haste_A(self):
        """Empilha os discos na haste A (do maior para o menor)."""
        for disco in range(self.__discos, 0, -1):
            self.torres['A'].empilha(disco)
    
    def mover_disco(self, origem: str, final: str):
        """
        Move um disco entre hastes.
        
        origem: Haste de origem ('A', 'B', 'C')
        final: Haste de destino ('A', 'B', 'C')
        """
        haste_origem = self.torres[origem]
        haste_final = self.torres[final]

        if haste_origem.pilha_esta_vazia():
            raise PilhaVaziaErro(f"Haste {origem} vazia")
        
        if haste_final.pilha_esta_cheia():
            raise PilhaCheiaErro(f"Haste {final} cheia")
        
        if (not haste_final.pilha_esta_vazia() and
            haste_origem._Pilha__itens[-1] > haste_final._Pilha__itens[-1]):
            raise ValueError('Disco maior não pode ficar em cima do menor')
        
        disco = haste_origem.desempilha()
        haste_final.empilha(disco)
        self.__passos += 1

        print(f"\nPosição {self.__passos} passos")
        self.visualizar()

    def visualizar(self):
        """Mostra a representação visual simplificada das torres"""
        # Obtém os discos de cada torre (em ordem do topo para a base)
        torre_A = self.obter_discos('A')
        torre_B = self.obter_discos('B')
        torre_C = self.obter_discos('C')
        
        # Formata a saída conforme a imagem
        print(f"[ {' '.join(map(str, torre_A))} ] < pino inicial")
        print(f"[ {' '.join(map(str, torre_B))} ] < pino intermediário")
        print(f"[ {' '.join(map(str, torre_C))} ] < pino destino")
        print()

    def obter_discos(self, torre):
        """Retorna os discos de uma torre em ordem do topo para a base"""
        discos = []
        temp_pilha = Pilha(self.__discos, 'i')
        original_pilha = self.torres[torre]
        
        # Desempilha tudo para obter a ordem correta
        while not original_pilha.pilha_esta_vazia():
            discos.append(original_pilha.desempilha())
            temp_pilha.empilha(discos[-1])
        
        # Reempilha para manter a estrutura original
        while not temp_pilha.pilha_esta_vazia():
            original_pilha.empilha(temp_pilha.desempilha())
        
        # Inverte para mostrar do topo para base
        return discos[::-1]

    def resolver(self, n: int = None, origem: str = 'A', final: str = 'C', auxiliar: str = 'B'):
        """Resolve o jogo da Torre de Hanoi recursivamente"""
        if n is None:
            n = self.__discos

        if n == 1:
            self.mover_disco(origem, final)
        else:
            self.resolver(n-1, origem, auxiliar, final)
            self.mover_disco(origem, final)
            self.resolver(n-1, auxiliar, final, origem)

# Exemplo de uso
if __name__ == "__main__":
    jogo = Torre_de_Hanoi(3)
    
    print("Posição Inicial: 0 passos")
    jogo.visualizar()

    jogo.resolver()

    print("\nEstado final:")
    jogo.visualizar()