import requests
import pytest


def test_status():
    response = requests.get('https://dog.ceo/api/breeds/list/all')
    assert response.status_code == 200


def test_random_pictures_1():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    assert (type(data['message'])) == str


def test_random_pictures_3():
    response = requests.get('https://dog.ceo/api/breeds/image/random/3')
    data = response.json()
    assert (len(data['message'])) == 3


@pytest.mark.parametrize('breed', ['bulldog', 'hound', 'retriever'])
def test_images_by_breed(breed):
    response = requests.get('https://dog.ceo/api/breed/hound/images')
    data = response.json()
    assert (len(data['message'])) == 1000


@pytest.mark.parametrize('breed', ['bulldog', 'hound', 'retriever'])
def test_random_images_3_by_breed(breed):
    response = requests.get('https://dog.ceo/api/breeds/image/random/3')
    data = response.json()
    assert (len(data['message'])) == 3
