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
    def selection_sort(arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr



    @staticmethod
    def bubble_sort(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista
    
    
    @staticmethod
    def mergeSort(arr):
        aux = [0] * len(arr)
        Ordenacao.mergesort(arr, aux, 0, len(arr) - 1)
        return arr

    @staticmethod
    def merge(arr, aux, left, mid, right):
        
        for k in range(left, right + 1):
            aux[k] = arr[k]

        i = left
        j = mid + 1

        for k in range(left, right + 1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > right:
                arr[k] = aux[i]
                i += 1
            elif aux[j] < aux[i]:
                arr[k] = aux[j]
                j += 1
            else:
                arr[k] = aux[i]
                i += 1

    @staticmethod
    def mergesort(arr, aux, left, right):
        if right <= left:
            return
        
        mid = (left + right) // 2

        #
        Ordenacao.mergesort(arr, aux, left, mid)

       
        Ordenacao.mergesort(arr, aux, mid + 1, right)


        Ordenacao.merge(arr, aux, left, mid, right)

                    