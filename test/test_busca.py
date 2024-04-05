import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") 

from algoritmos.busca import Busca

import random

class TestBusca:
    def __init__(self):
        self.lista_ordenada = [3, 5, 7, 9, 27, 34, 63, 88, 89]

    def test_busca_sequencial(self):
        valores = [random.randint(1, 100) for _ in range(5)]
    
        for v in valores:
            resultado = Busca.busca_sequencial(self.lista_ordenada, v)
            if v in self.lista_ordenada:
                esperado = self.lista_ordenada.index(v)
                if resultado == esperado:
                    print(f"Teste de busca sequencial para o valor {v} passou.")
                else:
                    print(f"Teste de busca sequencial para o valor {v} falhou. Índice esperado: {esperado}, Índice real: {resultado}")
            else:
                if resultado == -1:
                    print(f"Teste de busca sequencial para o valor {v} passou.")
                else:
                    print(f"Teste de busca sequencial para o valor {v} falhou. Índice esperado: -1, Índice real: {resultado}")

    def test_busca_binaria(self):
        try:
            assert Busca.busca_binaria(self.lista_ordenada, 34) == 5
            assert Busca.busca_binaria(self.lista_ordenada, 88) == 7
            assert Busca.busca_binaria(self.lista_ordenada, 50) == -1
            print("Teste de busca binária passou.")
        except AssertionError:
            print("Teste de busca binária falhou.")

    def executar_testes(self):
        self.test_busca_sequencial()
        self.test_busca_binaria()
        print("Fim dos testes.")

if __name__ == '__main__':
    test_Busca = TestBusca()
    test_Busca.executar_testes()
