def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[-1]
    menores = [x for x in lista[:-1] if x < pivo]
    maiores_ou_iguais = [x for x in lista[:-1] if x >= pivo]
    return (quick_sort(menores) + [pivo] + quick_sort(maiores_ou_iguais))