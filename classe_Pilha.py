from array import array

class PilhaCheiaErro(Exception):
    """Erro personalizado para quando a pilha está cheia"""
    pass

class PilhaVaziaErro(Exception):
    """Erro personalizado para quando a pilha está cheia"""
    pass

class Pilha():
    def __init__(self, tamanho_max, tipo='i'):
        """
        Inicializa a pilha com um array do tipo especificado.
        Tipos aceitos:
            'i' -> inteiros (int - parâmetro padrão)
            'u' -> caracteres (string)
        """

        if tipo != 'i' and tipo != 'u':
            raise TypeError("'tipo' deve ser 'i' (inteiros) ou 'u' (caracteres)")
    
        self.__itens = array(tipo)  # Array privado para armazenar os itens
        self.__tipo = tipo
        self.__tamanhoMax = tamanho_max

    def ver_topo(self):
        """Retorna o elemento no topo da pilha sem removê-lo."""
        if self.pilha_esta_vazia():
            return 0
        return self.__itens[-1]
    
    def empilha(self, dado):
        """Adiciona um item ao topo da pilha."""
        try:
            if self.pilha_esta_cheia():
                raise PilhaCheiaErro("A pilha atingiu sua capacidade máxima")
        
            if self.__tipo == 'i' and not isinstance(dado, int):
                raise TypeError(f"O tipo do dado {dado} deve ser int (inteiro)")
            elif self.__tipo == 'u' and not isinstance(dado, str):
                raise TypeError(f"O tipo do dado {dado} deve ser string (caractere)")
            
            self.__itens.append(dado)

        except PilhaCheiaErro as e:
            print("Erro:", e)  # A pilha atingiu sua capacidade máxima


    def desempilha(self):
        """Remove e retorna o item do topo da pilha.
        Levanta uma exceção se a pilha estiver vazia."""

        if len(self.__itens) <= 0:
            raise PilhaVaziaErro("A pilha está vazia!")

        return self.__itens.pop()

    def pilha_esta_vazia(self):
        """Verifica se a pilha está vazia."""
        return self.tamanho() == 0
    
    def pilha_esta_cheia(self):
        """Verifica se a pilha está cheia."""
        return self.tamanho() == self.__tamanhoMax

    def troca(self):
        item_abaixo_ref = self.__itens[-2]

        self.__itens[-2] = self.__itens[-1]
        self.__itens[-1] = item_abaixo_ref


    def tamanho(self):
        """Retorna o número de itens na pilha."""
        return len(self.__itens)



    def __str__(self):
        """Representação em string da pilha (topo no final)."""
        return str(self.__itens)


# Testes
if __name__ == "__main__":
    pilha = Pilha(5)

    pilha.empilha(10)
    pilha.empilha(20)
    pilha.empilha(30)

    print("Pilha:", pilha)  # Saída: [10, 20, 30]
    print("Desempilhado:", pilha.desempilha())  # Saída: 30
    print("Pilha após desempilhar:", pilha)  # Saída: [10, 20]
    print("Tamanho:", pilha.tamanho())  # Saída: 2
    print("Está vazia?", pilha.pilha_esta_vazia())  # Saída: False

