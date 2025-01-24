def  maior(coleção):
    maior_item = coleção [0]
    for item  in coleção:
        if item > maior_item:
           maior_item = item
    return maior_item
def menor(coleção):
    menor_item = coleção [0]
    for item in coleção:
        if item < menor_item:
            menor_item =item
    return menor_item
print(menor((1,2,3,4,5,6,7,8,1256,27)))