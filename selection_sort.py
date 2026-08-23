#Porque o Bubble sort otimizado quebra de dentro do loop caso a lista já esteja organizada, contudo o selection sort não. O selection Sort continua dentro do loop fazendo comparações, então seu ômega continua sendo O(n^2)
def selection_sort(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(n - 1):
        indice_menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista [j] < lista[indice_menor]:
                indice_menor = j
        if indice_menor != i:
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
            trocas += 1
    print(f"comparações: {str(comparacoes)}")
    print(f"trocas={str(trocas)}")
    return lista