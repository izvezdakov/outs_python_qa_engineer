import pytest
import requests

from fourth_hw.data_models import DogImages, DogImage, AllBreeds


@pytest.mark.parametrize('subbreath', ["blenheim", "brittany", "cocker", "irish", "japanese", "sussex", "welsh"])
def test_spaniel_subbreeds(subbreath):
    breath = 'spaniel'
    url = f'https://dog.ceo/api/breed/{breath}/{subbreath}/images'
    response = requests.get(url=url)
    assert response.status_code == 200
    parsed_response = DogImages.validate(response.json())
    assert parsed_response.status == 'success'
    # for jpg_url in parsed_response.message: it works too long
    #     image_response = requests.get(url=jpg_url)
    #     assert image_response.status_code == 200

@pytest.mark.parametrize('breath',
                         ["affenpinscher", "borzoi", "cotondetulear", "hound", "mountain", "puggle", "spaniel"])
def test_by_bread(breath):
    url = f'https://dog.ceo/api/breed/{breath}/images'
    response = requests.get(url=url)
    assert response.status_code == 200
    parsed_response = DogImages.validate(response.json())
    assert parsed_response.status == 'success'


def test_random_image_is_working():
    url = f'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url=url)
    assert response.status_code == 200
    parsed_response = DogImage.validate(response.json())
    assert parsed_response.status == 'success'
    image_response = requests.get(url=parsed_response.message)
    assert image_response.status_code == 200


@pytest.mark.parametrize(('num', 'expected'),
                         [(-100500, 1),
                          (-1, 1),
                          (0, 1),
                          (1, 1),
                          (2, 2),
                          (5, 5),
                          (2.3, 2),
                          ('a', 1)])
def test_random_images_is_working(num, expected):
    url = f'https://dog.ceo/api/breeds/image/random/{num}'
    response = requests.get(url=url)
    assert response.status_code == 200
    parsed_response = DogImages.validate(response.json())
    assert parsed_response.status == 'success'
    assert len(parsed_response.message) == expected
    for image_url in parsed_response.message:
        image_response = requests.get(url=image_url)
        assert image_response.status_code == 200


def test_list_all_breeds():
    url = 'https://dog.ceo/api/breeds/list/all'
    response = requests.get(url=url)
    assert response.status_code == 200
    parsed_response = AllBreeds.validate(response.json())
    assert parsed_response.status == 'success'
