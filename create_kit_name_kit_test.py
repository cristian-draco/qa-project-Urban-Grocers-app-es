import sender_stand_request
import data


# Construye el body del kit reemplazando el nombre
def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body

# Validación positiva: el kit se crea correctamente
def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


# Validación negativa: la solicitud devuelve error 400
def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(
        kit_body,
        sender_stand_request.get_new_user_token()
    )
    assert response.status_code == 400


# 1 carácter permitido
def test_1_numero_permitido_de_caracteres_1():
    kit_body = get_kit_body(data.test_1_kit_name)
    positive_assert(kit_body)


# 511 caracteres permitidos
def test_2_numero_permitido_de_caracteres_511():
    kit_body = get_kit_body(data.test_2_kit_name)
    positive_assert(kit_body)


# Menos caracteres de los permitidos
def test_3_numero_de_caracteres_es_menor_que_la_cantidad_permitida():
    kit_body = get_kit_body(data.test_3_kit_name)
    negative_assert_400(kit_body)


# Más caracteres de los permitidos
def test_4_numero_de_caracteres_es_mayor_que_la_cantidad_permitida():
    kit_body = get_kit_body(data.test_4_kit_name)
    negative_assert_400(kit_body)


# Permite caracteres especiales
def test_5_permite_caracteres_especiales():
    kit_body = get_kit_body(data.test_5_kit_name)
    positive_assert(kit_body)


# Permite espacios
def test_6_permite_espacios():
    kit_body = get_kit_body(data.test_6_kit_name)
    positive_assert(kit_body)


# Permite números
def test_7_permite_numeros():
    kit_body = get_kit_body(data.test_7_kit_name)
    positive_assert(kit_body)


# No se envía el parámetro name
def test_8_parametro_no_pasa_en_la_solicitud():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_400(kit_body)


# Tipo de dato incorrecto para name
def test_9_ha_pasado_un_tipo_de_parametro_diferente():
    kit_body = get_kit_body(data.test_9_kit_name)
    negative_assert_400(kit_body)

# Obtener todos los kits del usuario
def test_get_user_kits():
    auth_token = sender_stand_request.get_new_user_token()

    kit_body = get_kit_body("Kit GET")
    sender_stand_request.post_new_client_kit(kit_body, auth_token)

    response = sender_stand_request.get_kits(auth_token)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# Buscar kit por nombre
def test_search_kit_by_name():
    auth_token = sender_stand_request.get_new_user_token()

    kit_name = "Sabores de París"
    kit_body = get_kit_body(kit_name)
    sender_stand_request.post_new_client_kit(kit_body, auth_token)

    response = sender_stand_request.search_kit_by_name(kit_name)

    assert response.status_code == 200


# Actualizar un kit existente
def test_update_kit_success():
    auth_token = sender_stand_request.get_new_user_token()

    kit_body = get_kit_body("Kit inicial")
    create_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    kit_id = create_response.json()["id"]

    updated_kit_body = {
        "name": "Mi kit modificada",
        "productsList": [
            {"id": 1, "quantity": 2}
        ]
    }

    response = sender_stand_request.put_kit(kit_id, updated_kit_body, auth_token)

    assert response.status_code == 200
    assert response.json()["ok"] is True


# Eliminar un kit
def test_delete_kit_success():
    auth_token = sender_stand_request.get_new_user_token()

    kit_body = get_kit_body("Kit eliminar")
    create_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    kit_id = create_response.json()["id"]

    response = sender_stand_request.delete_kit(kit_id, auth_token)

    assert response.status_code == 200
    assert response.json()["ok"] is True

# Obtener kits sin autorización
def test_get_kits_sin_autorizacion():
    response = sender_stand_request.get_kits_without_auth()
    assert response.status_code == 400 or response.status_code == 401