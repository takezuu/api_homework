import requests
import pytest


def test_status():
    response = requests.get('https://jsonplaceholder.typicode.com/')
    assert response.status_code == 200


def test_num_comments():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/3/comments')
    data = response.json()
    assert len(data) == 5


def test_photo():
    response = requests.get('https://jsonplaceholder.typicode.com/photos/15')
    data = response.json()
    assert data['url'] == "https://via.placeholder.com/600/f9cee5"


@pytest.mark.parametrize('id_', [1, 2, 3, 4])
def test_post(id_):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id_}')
    data = response.json()
    assert data['userId'] == 1


@pytest.mark.parametrize('id_', [130, 131, 132, 133])
def test_todo(id_):
    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{id_}')
    data = response.json()
    assert data['userId'] == 7
