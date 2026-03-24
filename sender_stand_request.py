import configuration
import requests
import data

# Función para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Función para obtener el token del nuevo usuario
def get_new_user_token():
    user_body = data.user_body.copy()
    user_response = post_new_user(user_body)

    # Líneas de depuración
    print("Código de estado:", user_response.status_code)
    print("Respuesta completa:", user_response.json())

    return user_response.json()['authToken']

# Función para crear un nuevo kit de usuario
def post_new_client_kit(kit_body, auth_token):
    url = configuration.URL_SERVICE + configuration.KITS_PATH
    headers = {"Authorization": f"Bearer {auth_token}",
               "Content-Type": "application/json"
    }

    print(f"URL completa: {url}")
    print(f"Headers: {headers}")
    print(f"Kit body: {kit_body}")

    response = requests.post(url, json=kit_body, headers=headers)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")

    return response

# Función para obtener todos los kits del usuario
def get_kits(auth_token):
    url = configuration.URL_SERVICE + configuration.KITS_PATH
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    print(f"GET URL: {url}")
    print(f"Headers: {headers}")

    response = requests.get(url, headers=headers)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")

    return response


# Función para obtener kits sin autorización (prueba negativa)
def get_kits_without_auth():
    url = configuration.URL_SERVICE + configuration.KITS_PATH

    print(f"GET URL (sin auth): {url}")

    response = requests.get(url)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")

    return response


# Función para buscar un kit por nombre
def search_kit_by_name(name):
    url = configuration.URL_SERVICE + configuration.SEARCH_KITS_PATH
    params = {"name": name}

    print(f"SEARCH URL: {url}")
    print(f"Params: {params}")

    response = requests.get(url, params=params)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")

    return response


# Función para actualizar un kit existente
def put_kit(kit_id, body, auth_token):
    url = f"{configuration.URL_SERVICE}{configuration.KITS_PATH}/{kit_id}"
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

    print(f"PUT URL: {url}")
    print(f"Headers: {headers}")
    print(f"Body: {body}")

    response = requests.put(url, json=body, headers=headers)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")

    return response


# Función para eliminar un kit
def delete_kit(kit_id, auth_token):
    url = f"{configuration.URL_SERVICE}{configuration.KITS_PATH}/{kit_id}"
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    print(f"DELETE URL: {url}")
    print(f"Headers: {headers}")

    response = requests.delete(url, headers=headers)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")

    return response