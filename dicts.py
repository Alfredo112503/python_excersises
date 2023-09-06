# Dado dos diccionarios 1 de productos y el 2 de categoría,
# conocer un 3 que permita tener el nombre del producto y el nombre de su categoría ejemplo.

products = {
    'ids':{
        '1': {
            'nombre': 'mouse',
            'precio': 50,
            'id_cat': '1'
        },
        '2': {
            'nombre': 'libreta',
            'precio': 10,
            'id_cat': '2'
        },
        '3': {
            'nombre': 'lapices big',
            'precio': 3,
            'id_cat': '2'
        }
    }
}

categories = {
    'ids': {
        '1': {
            'nombre': 'tecnologia'
        },
        '2': {
            'nombre': 'escolares'
        }
    }
}

result = {
    'id': '',
    'nombre': '',
    'precio': 0,
    'nombre_cat': ''
}


while True: 
    product_id = input("Ingrese el id del producto: ")

    if product_id in products['ids']:
        break

    print("Ingrese un id válido.")

values = []
cat_id = products['ids'][product_id]['id_cat']

# Agregamos el vector.
values.append(product_id)
values.append(products['ids'][product_id]['nombre'])
values.append(products['ids'][product_id]['precio'])
values.append(categories['ids'][cat_id]['nombre'])

ref = 0
for key in result:
    
    result.update({key:values[ref]})
    ref += 1

# Mostrar
print()
for k,v in result.items():

    print(f"{k} : {v}")





