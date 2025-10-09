import requests
import pytest


@pytest.fixture()
def new_post_id():
    body = {"title":"testwords","body":"body body","userId":1}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
    )
    post_id = response.json()['id']
    yield post_id
    print('delete post')
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')