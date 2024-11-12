import math

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.subir(len(self.heap) - 1)
        print(self.heap)
   
    def remove(self):
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.descer(0, len(self.heap) - 1)  
            print(f"Nova heap após remoção: {self.heap}")
        elif len(self.heap) == 1:
            removed_element = self.heap.pop(0)
            print(f"Elemento removido: {removed_element}")
        else:
            print("A heap está vazia, nada para remover.")

    def change_priority(self, index, new_priority):
        if index < 0 or index >= len(self.heap):
            print(f"Índice {index} inválido.")
            return
        
        old_priority = self.heap[index]
        self.heap[index] = new_priority

        print(f"Alterando a prioridade do índice {index} de {old_priority} para {new_priority}")

        if new_priority > old_priority:
            self.subir(index)
        else:
            self.descer(index, len(self.heap) - 1)

        print(f"Heap atualizada: {self.heap}")
        self.display_heap()

    def get_high_priority(self):
        return print(f"Alta prioridade: {self.heap[0]}")

    def arranjar(self, n):
        for i in range(n // 2, -1, -1):
            self.descer(i, n - 1)

    def heap_sort(self):
        n = len(self.heap)
        self.arranjar(n)

        for m in range(n - 1, 0, -1):
            self.heap[0], self.heap[m] = self.heap[m], self.heap[0]
            self.descer(0, m - 1)

        print("Heap ordenada:", self.heap)
        self.display_heap()

    def subir(self, i):
        j = (i - 1) // 2
        if j >= 0:
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
                self.subir(j)


    def descer(self, i, n):
        esquerda = 2 * i + 1
        direita = 2 * i + 2
        maior = i

        if esquerda <= n and self.heap[esquerda] > self.heap[maior]:
            maior = esquerda

        if direita <= n and self.heap[direita] > self.heap[maior]:
            maior = direita

        if maior != i:
            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            self.descer(maior, n)

    def display_heap(self):
        currentSize = len(self.heap)
        if currentSize == 0:
            print("A heap está vazia.")
            return

        depth = math.ceil(math.log2(currentSize + 1))

        print("==================================")

        index = 0
        for level in range(depth):
            level_count = 2 ** level

            leading_space = " " * (2 ** (depth - level) - 1)
            between_space = " " * (2 ** (depth - level + 1) - 1)

            line = leading_space
            line += between_space.join(
                f"{self.heap[index + i]:2}"
                for i in range(level_count)
                if index + i < currentSize
            )

            print(line)

            index += level_count

        print("==================================\n")
