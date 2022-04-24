import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url", default="https://ya.ru"
    )
    parser.addoption(
        "--status_code", default=200
    )


@pytest.fixture
def url(request):
    url = request.config.getoption("--url")
    return url


@pytest.fixture
def status(request):
    return int(request.config.getoption("--status_code"))
