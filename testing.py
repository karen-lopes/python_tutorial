lista = [1,2,1,1,2,3]


for index, i in enumerate(lista):
    for element in lista:
        if element == i:
            print(element, index)