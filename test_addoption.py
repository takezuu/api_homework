import requests


def test_url_action(url, status):
    response = requests.get(url)
    assert response.status_code == status
