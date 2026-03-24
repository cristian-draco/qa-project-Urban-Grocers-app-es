headers ={
    "Content-Type": "application/json",
}

# Datos para crear un usuario
user_body = {
    "firstName": "Ana",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop",
    "email": "ana@example.com",
    "comment": "Tengo 23 años"
}

# Body base para crear un kit
kit_body = {
    "name": "Mi kit",
}

# Datos para pruebas de validación del nombre del kit
test_1_kit_name = "a"
test_2_kit_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
test_3_kit_name = ""
test_4_kit_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
test_5_kit_name = "№%@\","
test_6_kit_name = " A Aaa "
test_7_kit_name = "123"
test_9_kit_name = 123


# Body para actualizar un kit
update_kit_body = {
    "name": "Mi kit modificada",
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        }
    ]
}

# Body para agregar productos a un kit
products_list_body = {
    "productsList": [
        {
            "id": 1,
            "quantity": 1
        },
        {
            "id": 2,
            "quantity": 2
        }
    ]
}

# Nombre para búsqueda de kit
search_kit_name = "Sabores de París"