import requests


def test_url_status(base_url, status_code):
    response = requests.get(url=base_url)
    assert response.status_code == status_code
    #  pytest --url=https://google.com --status_code=200
    #  pytest --status_code=404 --url=https://httpbin.org/status/404
