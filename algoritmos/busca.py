class Busca:
    
    @staticmethod
    def busca_binaria(lista, alvo):
        inicio = 0
        fim = len(lista) - 1
        
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if lista[meio] == alvo:
                return meio
            elif lista[meio] < alvo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return -1
    
    @staticmethod
    def busca_sequencial(lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1