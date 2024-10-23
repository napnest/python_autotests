import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5952314913da8aa3f1646e8d5162d41c'
HEADER = {
    'trainer_token': TOKEN,
    'Content-Type': 'application/json'
                 }
TRAINER_ID = '7722'

# Проверка статус кода
def test_status_code():
    response = requests.get(url = URL + '/trainers')
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [
    ('trainer_id', TRAINER_ID),
])

# Проверка имени тренера
def test_name_trainer(key, value):
    response = requests.get(url = URL + '/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.json()['data'][0][key] == value