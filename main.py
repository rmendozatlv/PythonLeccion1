# edad = int(input("Ingrese su edad : "))
# if (edad > 0 and edad <= 10):
#     print("Estas en un edad maravillosa vive la niñes")
# elif (edad > 10 and edad <= 20):
#     print("Esta es la edad de mucho estudio y feliz juventud")
# elif (edad > 20 and edad <= 30):
#     print("Viva el amor y conciencia y dedicacion en el trabajo")
# else:
#     print("Edad no valida")

listado = ("Naranja", "Platano", "Papaya")

print(len(listado))
print(listado[0:2])
for valor in listado:
    print(valor, end=' ')
# listado[0] = "Pera"
list = list(listado)
list[1] = 'Manzana'
listado = tuple(list)
print(listado)

# lista set
listaset = {'HP', 'LENOVO', 'ASUS', 'HUAWEI'}
print(listaset)
print(type(listaset))
listaset.add('SANSUNG')
print(listaset)
listaset.discard('AOC')
