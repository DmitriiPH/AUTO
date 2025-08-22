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


#@pytest.mark.skip('No preconditions')
def test_get_one_post(new_post_id):   
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{new_post_id}').json()
    assert response['id'] == new_post_id
        

def test_geat_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    assert len(response) == 100

def test_add_post():
        body = {
            "title":"testwords",
            "body":"body body",
            "userId":1
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=body,
            headers=headers
        )
        assert response.status_code == 201
        assert response.json()['id'] == 101