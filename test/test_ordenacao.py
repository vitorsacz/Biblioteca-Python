import os
import sys
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../") 

from algoritmos.ordenacao import Ordenacao


class TesteOrdenacao:
    def __init__(self):
        pass

    def teste_bubble_sort(self, arr):
        arr_ordenado = sorted(arr)
        try:
            assert Ordenacao.bubble_sort(arr.copy()) == arr_ordenado
            print("O teste do Bubble Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Bubble Sort falhou.")

    def teste_selection_sort(self, arr):
        arr_ordenado = sorted(arr)
        try:
            assert Ordenacao.selection_sort(arr.copy()) == arr_ordenado
            print("O teste do Selection Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Selection Sort falhou.")
            return

    def teste_insertion_sort(self, arr):
        arr_ordenado = sorted(arr)
        try:
            assert Ordenacao.insertion_sort(arr.copy()) == arr_ordenado
            print("O teste do Insertion Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Insertion Sort falhou.")
            return

    def teste_merge_sort(self, arr):
        arr_ordenado = sorted(arr)
        try:
            Ordenacao.mergeSort(arr)
            assert arr == arr_ordenado
            print("O teste do Merge Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Merge Sort falhou.")
            return

    def teste_quick_sort(self, arr):
        arr_ordenado = sorted(arr)
        try:
            Ordenacao.quick_sort(arr)
            assert arr == arr_ordenado
            print("O teste do Quick Sort foi bem-sucedido.")
        except AssertionError:
            print("O teste do Quick Sort falhou.")
            return

    def executar_testes(self):
        casos_teste = [
            ([3, 7, 33, 59, 71], "vetor ordenado crescente"),
            ([71, 7, 3, 9, 7], "vetor não ordenado"),
            ([71, 59, 33, 7, 3], "vetor ordenado descrescente"),
            ([], "Vetor vazio"),
            ([42], "Vetor com um único elemento"),
            ([3, 7, 3, 9, 7], "Vetor com elementos repetidos"),
            ([-5, -3, -9, -1], "Vetor com elementos negativos"),
            ([random.randint(0, 100) for _ in range(100)], "Lista de 100 números aleatórios")
        ]

        for arr, desc in casos_teste:
            print(f"Testando {desc}: {arr}")
            self.teste_bubble_sort(arr)
            self.teste_selection_sort(arr)
            self.teste_insertion_sort(arr)
            self.teste_merge_sort(arr)
            self.teste_quick_sort(arr)
            print()

        print("Fim dos testes.")

if __name__ == '__main__':
    testes = TesteOrdenacao()
    testes.executar_testes()
