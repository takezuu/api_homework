import requests
import pytest


def test_status():
    response = requests.get('https://api.openbrewerydb.org/')
    assert response.status_code == 200


def test_state_ohio():
    response = requests.get('https://api.openbrewerydb.org/breweries?by_state=ohio')
    data = response.json()
    for i in data:
        assert i['state'] == 'Ohio'


@pytest.mark.parametrize('num', [20, 30, 40, 50])
def test_num_of_breweries(num):
    response = requests.get(f'https://api.openbrewerydb.org/breweries?per_page={num}')
    data = response.json()
    assert (len(data)) == num


@pytest.mark.parametrize('name', ['Brewers Tasting Room', 'Cage Brewing', 'Green Bench Brewing Co'])
def test_city(name):
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_name={name}')
    data = response.json()
    for i in data:
        assert i['city'] == 'Saint Petersburg'


@pytest.mark.parametrize('postal_code', [13006, 13127, 13005])
def test_country(postal_code):
    response = requests.get(f'https://api.openbrewerydb.org/breweries?by_postal={postal_code}')
    data = response.json()
    for i in data:
        assert i['country'] == 'France'
