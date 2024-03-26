class Ordenacao:

    @staticmethod
    def insertion_sort(lista):
        for i in range(1, len(lista)):
            chave = lista[i]
            j = i - 1
            while j >= 0 and lista[j] > chave:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = chave
        return lista
    



    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivo = arr[0]
            menores_que_pivo = [x for x in arr[1:] if x <= pivo]
            maiores_que_pivo = [x for x in arr[1:] if x > pivo]
            return self.quicksort(menores_que_pivo) + [pivo] + self.quicksort(maiores_que_pivo)
    


    
    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista
    
    
    
    @staticmethod
    def merge_sort(lista):
    
        if len(lista) <= 1:
            return lista
        
        
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        
        esquerda = merge(esquerda)
        direita = merge(direita)
        
        return merge(esquerda, direita)

def merge(esquerda, direita):
   
    resultado = []
    i = j = 0 
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado
            

                