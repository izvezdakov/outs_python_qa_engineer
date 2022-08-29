import pytest
import requests

from fourth_hw.data_models import CreateResourseModel


@pytest.mark.parametrize('userId', [-1, 0, 1, 2, 'a', 4.1])
def test_creating(userId):
    url = f'https://jsonplaceholder.typicode.com/posts'
    response = requests.post(url=url, json={
        'title': 'foo',
        'body': 'bar',
        'userId': userId,
      })
    assert response.ok
    parsed_response = CreateResourseModel.validate(response.json())
    assert parsed_response.userId == userId


@pytest.mark.parametrize('userId', [-1, 0, 1, 2, 'a', 4.1])
@pytest.mark.parametrize('post', [1, 2])
def test_updating(userId, post):
    url = f'https://jsonplaceholder.typicode.com/posts/{post}'
    response = requests.put(url=url, json={
        'title': 'foo',
        'body': 'bar',
        'userId': userId,
      })
    assert response.ok
    parsed_response = CreateResourseModel.validate(response.json())
    assert parsed_response.userId == userId


@pytest.mark.parametrize('title', ['a', 'b'])
@pytest.mark.parametrize('post', [1, 2])
def test_patching(title, post):
    url = f'https://jsonplaceholder.typicode.com/posts/{post}'
    response = requests.put(url=url, json={
        'title': title,
    })
    assert response.ok
    parsed_response = CreateResourseModel.validate(response.json())
    assert parsed_response.title == title
    assert parsed_response.resourse_id == post


@pytest.mark.parametrize('post', [1, 2])
def test_deleting(post):
    url = f'https://jsonplaceholder.typicode.com/posts/{post}'
    response = requests.delete(url=url)
    assert response.ok


@pytest.mark.parametrize('post', [1, 2])
def test_deleting(post):
    url = f'https://jsonplaceholder.typicode.com/posts/{post}/comments'
    response = requests.get(url=url)
    assert response.ok
