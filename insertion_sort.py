#O Insertion Sort é o mais indicado entre os algoritmos quadráticos devido à sua natureza adaptativa, o que permite que sua complexidade caia para O(n) em listas já ordenadas ou quase ordenadas. O Insertion sort é sempre O(n^2) e o Bubble sort otimizado só é O(n) em listas totalmente ordenadas (não quase)
def insertion_sort(lista):
    n = len(lista)
    deslocamentos = 0
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0  and lista[j] > chave:
            lista[j + 1] = lista[j]
            deslocamentos += 1
            j -= 1
        lista[j + 1] = chave
    print(f"deslocamentos={str(deslocamentos)}")
    return lista