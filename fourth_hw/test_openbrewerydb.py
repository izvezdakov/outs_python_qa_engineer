import pytest
import requests
from allpairspy import AllPairs

from fourth_hw.data_models import Brewer


@pytest.mark.parametrize('brewtype', ["micro",
                                      "nano",
                                      "regional",
                                      "brewpub",
                                      "large",
                                      "planning",
                                      "bar",
                                      "contract",
                                      "proprietor",
                                      "closed"])
def test_by_type(brewtype):
    url = f'https://api.openbrewerydb.org/breweries?by_type={brewtype}'
    response = requests.get(url=url)
    assert response.status_code == 200
    for brew in response.json():
        parsed_response = Brewer.validate(brew)
        assert parsed_response.brewery_type == brewtype


@pytest.mark.parametrize(('num', 'expected'),
                         [(0, 1),
                          (1, 1),
                          (2, 2),
                          (5.9, 5),
                          ('a', 1)])
def test_random_brewery(num, expected):
    url = f'https://api.openbrewerydb.org/breweries/random?size={num}'
    response = requests.get(url=url)
    assert response.status_code == 200
    assert len(response.json()) == expected
    for brew in response.json():
        parsed_response = Brewer.validate(brew)
        assert parsed_response


@pytest.mark.parametrize(['page', 'per_page'], [
    value_list for value_list in AllPairs([
        [0, 1, 2, 5.9, 'a'],
        [0, 1, 2, 5.9, 'a'],
    ])
])
def test_page_brewery(page, per_page):
    url = f'https://api.openbrewerydb.org/breweries?page={page}&per_page={per_page}'
    response = requests.get(url=url)
    assert response.status_code == 200
    for brew in response.json():
        parsed_response = Brewer.validate(brew)
        assert parsed_response


def test_single_brewery():
    url = f'https://api.openbrewerydb.org/breweries/madtree-brewing-cincinnati'
    response = requests.get(url=url)
    assert response.status_code == 200
    parsed_response = Brewer.validate(response.json())
    assert parsed_response


@pytest.mark.parametrize('city', ["San Diego",
                                  "Jung-gu", "Goyang-si"])
def test_by_city(city):
    url = f'https://api.openbrewerydb.org/breweries?by_city={city}'
    response = requests.get(url=url)
    assert response.status_code == 200
    for brew in response.json():
        parsed_response = Brewer.validate(brew)
        assert parsed_response.city == city
