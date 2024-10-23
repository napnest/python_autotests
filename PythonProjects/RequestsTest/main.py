import requests
from faker import Faker

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5952314913da8aa3f1646e8d5162d41c'
HEADER = {'Content-Type': 'application/json'}

# Создание рандомного имени
fake = Faker()
random_name = fake.name()

# ID покемона
pokemon_id_delete = '107486'
pokemon_id_add_pokeball = '107486'
pokemon_id_change_name = '107486'

# Хэдеры создания покемона
HEADER = {
    'trainer_token': '5952314913da8aa3f1646e8d5162d41c',
    'Content-Type': 'application/json'
                 }
# Тело создания покемона
body_create = {
    'name': random_name,
    'photo_id': -1
}

# Тело удаления покемона
body_delete = {
    'pokemon_id': pokemon_id_delete
}

# Тело поймать в покебол
body_add_pokeball = {
    'pokemon_id': pokemon_id_add_pokeball
}

# Тело изменения имени покемона
body_change_name = {
    'pokemon_id': pokemon_id_change_name,
    'name': random_name,
}

# Создание покемона
response_create = requests.post(url = URL + '/pokemons', headers = HEADER, json = body_create)
pokemon_id = response_create.json()['id']
print(response_create.status_code)
print(response_create.text)

# Изменение имени покемона
response_change_name = requests.patch(url = URL + '/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.status_code)
print(response_change_name.text)

# Поймать покемона в покебол
response_add_pokeball = requests.post(url = URL + '/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.status_code)
print(response_add_pokeball.text)

# Удаление покемона
response_delete = requests.post(url = URL + '/pokemons/knockout', headers = HEADER, json = body_delete)
print(response_delete.status_code)
print(response_delete.text)




