from algoritmos.ordenacao import Ordenacao
from algoritmos.busca import Busca
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def plotar_complexidade_tempo():
    
    tamanhos = np.linspace(1, 10000, 100)

    bubble_sort = tamanhos ** 2
    selection_sort = tamanhos ** 2
    insertion_sort = tamanhos ** 2
    merge_sort = tamanhos * np.log(tamanhos)
    quick_sort = tamanhos * np.log(tamanhos)

    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, bubble_sort, label="Bubble Sort (O(n^2))")
    plt.plot(tamanhos, selection_sort, label="Selection Sort (O(n^2))")
    plt.plot(tamanhos, insertion_sort, label="Insertion Sort (O(n^2))")
    plt.plot(tamanhos, merge_sort, label="Merge Sort (O(n*log(n)))")
    plt.plot(tamanhos, quick_sort, label="Quick Sort (O(n*log(n)))")
    plt.xlabel('Tamanho da Entrada')
    plt.ylabel('Complexidade Temporal')
    plt.title('Notação Big O dos Algoritmos de Ordenação')
    plt.legend()
    plt.grid(True)
    plt.savefig('complexidade_temporal.png')
    plt.show()

def medir_tempo_execucao(algoritmo, lst, alvo=None):
 
    tempo_inicial = time.time()  
    if alvo is not None:
        algoritmo(lst, alvo)  
    else:
        algoritmo(lst)  
    tempo_final = time.time() 
    return tempo_final - tempo_inicial  


def gerar_dados_teste(tamanho):

    return [random.randint(1, 1000) for _ in range(tamanho)]  
def analisar_desempenho(algoritmos, tamanhos, tipo):

    resultados = {} 

    for nome, algoritmo in algoritmos.items():  
        tempos_execucao = []  
        for tamanho in tamanhos:  
            if tipo == 'Ordenação':
                lst = gerar_dados_teste(tamanho)  
            elif tipo == 'Busca':
                lst = sorted(gerar_dados_teste(tamanho))  
                alvo = random.choice(lst)  
            tempo_decorrido = medir_tempo_execucao(algoritmo, lst, alvo if tipo == 'Busca' else None)  
            tempos_execucao.append(tempo_decorrido)  
        resultados[nome] = tempos_execucao  

    return resultados  


def gerar_grafico(resultados, tamanhos, tipo):

    plt.figure(figsize=(10, 6))  
    for nome, tempos_execucao in resultados.items():
        plt.plot(tamanhos, tempos_execucao, label=nome)  
    plt.xlabel('Tamanho da Lista')  
    plt.ylabel('Tempo de Execução (s)')  
    plt.title(f'Desempenho dos Algoritmos de {tipo}')  
    plt.legend()  
    plt.grid(True)  
    plt.savefig(f'grafico_{tipo.lower()}.png')  
    plt.show()  


def main():

    plotar_complexidade_tempo()

    algoritmos_ordenacao = {
        'Bubble Sort': Ordenacao.bubble_sort,
        'Selection Sort': Ordenacao.selection_sort,
        'Insertion Sort': Ordenacao.insertion_sort,
        'Merge Sort': Ordenacao.mergeSort,
        'Quick Sort': Ordenacao.quicksort
    }

    algoritmos_busca = {
        'Busca Binária': Busca.busca_binaria,
        'Busca Sequencial': Busca.busca_sequencial
    }

    tamanhos_teste = [100, 1000, 10000]  

    resultados_ordenacao = analisar_desempenho(algoritmos_ordenacao, tamanhos_teste, 'Ordenação')  
    gerar_grafico(resultados_ordenacao, tamanhos_teste, 'Ordenação')  

    resultados_busca = analisar_desempenho(algoritmos_busca, tamanhos_teste, 'Busca')  
    gerar_grafico(resultados_busca, tamanhos_teste, 'Busca')  


if __name__ == "__main__":
    main()
    
